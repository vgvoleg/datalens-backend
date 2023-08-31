from __future__ import annotations

import abc
import logging
from typing import ClassVar, Generic, TypeVar, Sequence, Union

import attr
import sqlalchemy as sa
from sqlalchemy.engine.default import DefaultDialect
from sqlalchemy.sql.base import Executable
from sqlalchemy.dialects.postgresql.psycopg2 import PGDialect_psycopg2

from bi_constants.enums import BIType

from bi_core.data_processing.streaming import AsyncChunkedBase
from bi_core.data_processing.processing.db_base.exec_adapter_base import ProcessorDbExecAdapterBase
from bi_core.db.sa_types import make_sa_type
from bi_connector_postgresql.core.postgresql_base.type_transformer import PostgreSQLTypeTransformer


LOGGER = logging.getLogger(__name__)

_CONN_TV = TypeVar("_CONN_TV")


@attr.s
class PostgreSQLExecAdapterAsync(Generic[_CONN_TV], ProcessorDbExecAdapterBase, metaclass=abc.ABCMeta):  # noqa
    """
    PG-CompEng-specific adapter.
    Adds DDL functionality and PostgreSQL specificity to the base DB adapter.
    """

    _conn: _CONN_TV = attr.ib(kw_only=True)
    _tt: PostgreSQLTypeTransformer = attr.ib(factory=PostgreSQLTypeTransformer, init=False)

    _log: ClassVar[logging.Logger] = LOGGER.getChild('PostgreSQLExecAdapterAsync')  # type: ignore  # TODO: fix

    @property
    def dialect(self) -> DefaultDialect:
        # Note: not necessarily psycopg2, but should be close enough
        # (especially for debug-compile).
        return PGDialect_psycopg2()

    @abc.abstractmethod
    async def _execute(self, query: Union[str, Executable]) -> None:
        """Execute query without (necessarily) fetching data"""

    async def _execute_ddl(self, query: Union[str, Executable]) -> None:
        """ Execute a DDL statement """
        await self._execute(query)

    def _make_sa_table(self, table_name: str, names: Sequence[str], user_types: Sequence[BIType]) -> sa.Table:
        assert len(names) == len(user_types)
        columns = [
            sa.Column(
                name=name,
                type_=make_sa_type(native_type=self._tt.type_user_to_native(user_t=user_t))
            )
            for name, user_t in zip(names, user_types)
        ]
        return sa.Table(table_name, sa.MetaData(), *columns, prefixes=['TEMPORARY'])

    async def create_table(
            self, *, table_name: str, names: Sequence[str], user_types: Sequence[BIType],
    ) -> sa.sql.selectable.TableClause:
        """Create table in database"""

        table = self._make_sa_table(table_name=table_name, names=names, user_types=user_types)
        self._log.info(f'Creating PG processor table {table_name}: {table}')
        await self._execute_ddl(sa.schema.CreateTable(table))
        return table

    async def _drop_table(self, table_name: str) -> None:
        await self._execute_ddl(sa.schema.DropTable(sa.table(table_name)))  # type: ignore

    async def drop_table(self, table_name: str) -> None:
        """Drop table in database"""

        self._log.info(f'Dropping PG processor table {table_name}')
        await self._drop_table(table_name=table_name)

    @abc.abstractmethod
    async def insert_data_into_table(
            self, *,
            table_name: str,
            names: Sequence[str],
            user_types: Sequence[BIType],
            data: AsyncChunkedBase,
    ) -> None:
        """ ,,, """