from __future__ import annotations

import datetime
import math
import random
import uuid
from typing import (
    TYPE_CHECKING, Any, Callable, NamedTuple,
    Optional, Sequence,
)

import attr
import shortuuid
import sqlalchemy as sa
from sqlalchemy.sql.type_api import TypeEngine

from bi_constants.enums import BIType, ConnectionType

from bi_db_testing.database.base import DbBase, DbTableBase, DbConfig
from bi_db_testing.database.dispenser import DbDispenserBase, ReInitableDbDispenser
from bi_db_testing.database.engine_wrapper import get_engine_wrapper_cls_for_url

from bi_core.db import make_sa_type, get_type_transformer

if TYPE_CHECKING:
    from bi_core.db.conversion_base import TypeTransformer


@attr.s(frozen=True)
class CoreDbConfig(DbConfig):
    conn_type: ConnectionType = attr.ib(kw_only=True)


@attr.s
class Db(DbBase[CoreDbConfig]):
    """ An executable interface """

    @property
    def conn_type(self) -> ConnectionType:
        return self.config.conn_type

    def eval(
            self, expr: sa.sql.ClauseElement,
            from_: Optional[sa.sql.ClauseElement] = None,
            user_t: Optional[BIType] = None,
    ) -> Any:
        value = self.base_eval(expr, from_=from_)
        if user_t is not None:
            value = get_type_transformer(self.conn_type).cast_for_output(value, user_t=user_t)
        return value


def make_db_config(
        conn_type: ConnectionType,
        url: str,
        cluster: Optional[str] = None,
) -> CoreDbConfig:

    engine_config_kwargs: dict[str, Any] = {}
    if conn_type == ConnectionType.clickhouse:
        engine_config_kwargs['cluster'] = cluster
    db_eng_config_cls = get_engine_wrapper_cls_for_url(url).CONFIG_CLS
    db_eng_config = db_eng_config_cls(url=url, **engine_config_kwargs)

    db_config = CoreDbConfig(
        engine_config=db_eng_config,
        conn_type=conn_type,
    )
    return db_config


def make_db_from_config(db_config: CoreDbConfig) -> Db:
    ew_cls = get_engine_wrapper_cls_for_url(db_config.engine_config.url)
    engine_wrapper = ew_cls(config=db_config.engine_config)
    return Db(config=db_config, engine_wrapper=engine_wrapper)


def make_db(
        conn_type: ConnectionType,
        url: str,
        cluster: Optional[str] = None,
) -> Db:
    # FIXME: Switch to accepting a fully ready config here
    db_config = make_db_config(conn_type=conn_type, url=url, cluster=cluster)
    return make_db_from_config(db_config)


class CoreDbDispenser(DbDispenserBase[CoreDbConfig, Db]):
    def make_database(self, db_config: CoreDbConfig) -> Db:
        return make_db_from_config(db_config)


class CoreReInitableDbDispenser(ReInitableDbDispenser[CoreDbConfig, Db], CoreDbDispenser):
    pass


@attr.s(frozen=True)
class DbTable(DbTableBase):
    db: Db = attr.ib(kw_only=True)  # Redefine type to Db from DbBase


@attr.s()
class C:
    name: str = attr.ib()
    user_type: BIType = attr.ib()
    nullable: Optional[bool] = attr.ib(default=None)
    _sa_type: TypeEngine = attr.ib(default=None)
    _vg: Callable[[int, datetime.datetime], Any] = attr.ib(default=None)

    DEFAULT_VALUE_GENERATORS = {
        BIType.string: lambda rn, **kwargs: f"str_значение_{rn}",
        BIType.integer: lambda rn, **kwargs: rn,
        BIType.float: lambda rn, **kwargs: rn + (rn / 10),
        BIType.date: lambda rn, ts, **kwargs: ts.date() + datetime.timedelta(days=rn),
        BIType.datetime: lambda rn, ts, **kwargs: ts + datetime.timedelta(days=rn / math.pi),
        BIType.genericdatetime: lambda rn, ts, **kwargs: ts + datetime.timedelta(days=rn / math.pi),
        BIType.boolean: lambda rn, **kwargs: bool(int(rn) % 2),
        BIType.uuid: lambda rn, **kwargs: str(uuid.UUID(int=rn)),
        BIType.array_int: lambda rn, **kwargs: [rn * idx for idx in range(5)],
        BIType.array_str: lambda rn, **kwargs: [f"str_{str(rn * idx)}" for idx in range(5)],
        BIType.array_float: lambda rn, **kwargs: [float(rn * idx) * 1.1 for idx in range(5)],
    }

    @attr.s(auto_attribs=True, frozen=True)
    class ArrayDataGetter:
        _data_container: Sequence[Sequence[Any]]

        def __getitem__(self, col_idx: int) -> Callable[[int, datetime.datetime], Any]:
            return lambda rn, **kwargs: self._data_container[rn][col_idx]

    @property
    def vg(self) -> Callable[[int, datetime.datetime], Any]:
        if self._vg is not None:
            return self._vg
        try:
            return self.DEFAULT_VALUE_GENERATORS[self.user_type]
        except KeyError as e:
            raise ValueError(f"No default value generator for user type {e}")

    def get_sa_type(self, tt: TypeTransformer) -> TypeEngine:
        if self._sa_type is not None:
            return self._sa_type
        native_type = tt.type_user_to_native(user_t=self.user_type)
        return make_sa_type(native_type, nullable=self.nullable)

    @classmethod
    def array_data_getter(cls, data_container) -> 'C.ArrayDataGetter':  # type: ignore  # TODO: fix
        return cls.ArrayDataGetter(data_container)

    @classmethod
    def int_value(cls, name: str = 'int_value'):  # type: ignore  # TODO: fix
        return cls(name, BIType.integer)

    @classmethod
    def datetime_value(cls, name: str = 'datetime_value'):  # type: ignore  # TODO: fix
        return cls(name, BIType.datetime)

    @classmethod
    def full_house(cls) -> list[C]:
        return [
            cls('string_value', BIType.string, nullable=False),
            cls('n_string_value', BIType.string, nullable=True),
            cls('int_value', BIType.integer, nullable=False),
            cls('n_int_value', BIType.integer, nullable=True),
            cls('float_value', BIType.float),
            cls('datetime_value', BIType.genericdatetime, nullable=False),
            cls('n_datetime_value', BIType.genericdatetime, nullable=True),
            cls('date_value', BIType.date),
            cls('boolean_value', BIType.boolean),
            cls('uuid_value', BIType.uuid),
            # Not included: arrays, geopoint, geopolygon, markup (not db-types, generally).
        ]

    @classmethod
    def array_columns(cls):  # type: ignore  # TODO: fix
        return [
            cls('array_int_value', BIType.array_int),
            cls('array_str_value', BIType.array_str),
            cls('array_float_value', BIType.array_float),
        ]


TEST_SEED = random.getrandbits(128)


def make_sample_data(
        columns: list[C] = None,
        rows: int = 10,
        seed: int = TEST_SEED,
        start_value: int = 0
) -> list[dict[str, Any]]:
    rnd = random.Random(seed)

    # 2017-01-01 .. 2020-04-17
    ts_uts = rnd.randrange(1483228800000000, 1587137765807968)
    ts = (
        datetime.datetime(1970, 1, 1) +
        datetime.timedelta(seconds=ts_uts / 1000000))
    if columns is None:
        columns = C.full_house()
    result = [
        {col.name: col.vg(rn=idx, ts=ts, rnd=rnd)  # type: ignore  # TODO: fix
         for col in columns}
        for idx in range(start_value, start_value + rows)
    ]
    return result


# TODO FIX: Implement option to provide data via arguments
def make_table(
        db: Db, schema: Optional[str] = None, rows: int = 10, start_value: int = 0,
        columns: Optional[list[C]] = None, name: Optional[str] = None,
        data: Optional[list[dict[str, Any]]] = None,
        create_in_db: bool = True,
) -> DbTable:
    columns = columns or C.full_house()
    tt = get_type_transformer(db.conn_type)
    table = db.table_from_columns(
        [
            sa.Column(name=col.name, type_=col.get_sa_type(tt))
            for col in columns
        ],
        schema=schema,
        table_name=name,
    )
    db_table = DbTable(db=db, table=table, schema=schema)  # type: ignore  # TODO: fix
    # now = datetime.datetime.utcnow().replace(tzinfo=None, microsecond=0)
    if data is None:
        data = make_sample_data(columns=columns, rows=rows, start_value=start_value)
        data_reproduce = make_sample_data(columns=columns, rows=rows, start_value=start_value)
        assert data == data_reproduce, 'should be reproducible'

    if create_in_db:
        db.create_table(table)
        db_table.insert(data)

    return db_table


def make_pg_table_with_enums(  # TODO: move to pg connector package
        db: Db, schema: Optional[str] = None, name: Optional[str] = None,
) -> DbTable:
    table = db.table_from_columns(
        [
            sa.Column(name=name, type_=type_)
            for name, type_ in [
                ('col1', sa.Enum('var1', 'var2', name=str(uuid.uuid4()))),
                ('col2', sa.TEXT),
                ('col3', sa.INTEGER),
            ]
        ],
        schema=schema,
        table_name=name,
    )
    db.create_table(table)
    db_table = DbTable(db=db, table=table, schema=schema)  # type: ignore  # TODO: fix
    db_table.insert(
        [
            {'col1': 'var1', 'col2': 'str1', 'col3': 1},
            {'col1': 'var1', 'col2': 'str2', 'col3': 2},
            {'col1': 'var2', 'col2': 'str3', 'col3': 3},
        ]
    )
    return db_table


def make_table_with_arrays(
    db: Db, schema: Optional[str] = None, rows: int = 10, start_value: int = 0,
    columns: Optional[list[C]] = None, name: Optional[str] = None,
    data: Optional[list[dict[str, Any]]] = None,
) -> DbTable:
    if columns is None:
        columns = C.full_house() + C.array_columns()
    return make_table(db=db, schema=schema, rows=rows, start_value=start_value, columns=columns, name=name, data=data)


def make_schema(db: Db, schema_name: Optional[str] = None) -> str:
    schema_name = schema_name or f'sch_{shortuuid.uuid()}'
    assert schema_name is not None
    db.create_schema(schema_name=schema_name)
    return schema_name


class DbView(NamedTuple):
    db: Db
    name: str
    query: str
    schema: str = None  # type: ignore  # TODO: fix

    @property
    def as_table(self) -> DbTable:
        return DbTable(
            db=self.db,
            table=self.db.load_table(schema=self.schema, table_name=self.name),
            schema=self.schema,
            can_insert=False,
        )


def make_view(db: Db, query: str, schema: str = None, name: str = None) -> DbView:
    name = name or 'test_view_{}'.format(uuid.uuid4().hex[:10])
    db.create_view(query=query, schema=schema, name=name)
    return DbView(db=db, schema=schema, name=name, query=query)  # type: ignore  # TODO: fix


def make_view_from_table(db_table: DbTable, name: str = None, schema: str = None) -> DbView:
    return make_view(
        db=db_table.db, query=db_table.select_all_query,
        schema=schema or db_table.schema, name=name
    )


class MultiTables(NamedTuple):
    users: DbTable
    posts: DbTable
    comments: DbTable


def make_multiple_db_tables(db):  # type: ignore  # TODO: fix
    """Basic table for all db types"""
    string_kwargs = {} if db.conn_type == ConnectionType.clickhouse else {'length': 255}
    sa_tables = [
        db.table_from_columns([  # users
            sa.Column(name='id', type_=sa.Integer()),
            sa.Column(name='name', type_=sa.String(**string_kwargs)),
        ]),
        db.table_from_columns([  # posts
            sa.Column(name='id', type_=sa.Integer()),
            sa.Column(name='author_id', type_=sa.Integer()),
            sa.Column(name='text', type_=sa.String(**string_kwargs)),
        ]),
        db.table_from_columns([  # comments
            sa.Column(name='id', type_=sa.Integer()),
            sa.Column(name='post_id', type_=sa.Integer()),
            sa.Column(name='from_id', type_=sa.Integer()),
            sa.Column(name='to_id', type_=sa.Integer()),
            sa.Column(name='text', type_=sa.String(**string_kwargs)),
        ]),
    ]

    def create(table):  # type: ignore  # TODO: fix
        db.create_table(table)
        return DbTable(db=db, table=table)

    tables = MultiTables(*[create(t) for t in sa_tables])
    tables.users.insert([
        {'id': 1, 'name': 'Clark Kent'},
        {'id': 2, 'name': 'Gaius Marius'},
        {'id': 3, 'name': 'Charlie Chaplin'},
        {'id': 4, 'name': 'Rosalind Franklin'},
    ])
    tables.posts.insert([
        {'id': 1, 'author_id': 2, 'text': 'Let it be'},
        {'id': 2, 'author_id': 4, 'text': 'Help'},
    ])
    tables.comments.insert([
        {'id': 1, 'post_id': 1, 'from_id': 1, 'to_id': 2, 'text': 'first'},
        {'id': 2, 'post_id': 1, 'from_id': 2, 'to_id': 1, 'text': 'second'},
        {'id': 3, 'post_id': 1, 'from_id': 3, 'to_id': 2, 'text': 'third'},
        {'id': 4, 'post_id': 2, 'from_id': 3, 'to_id': 4, 'text': 'first'},
        {'id': 5, 'post_id': 2, 'from_id': 4, 'to_id': 3, 'text': 'second'},
        {'id': 6, 'post_id': 2, 'from_id': 1, 'to_id': 4, 'text': 'third'},
    ])

    return tables
