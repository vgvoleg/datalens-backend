import csv
import datetime
import io
import random
from typing import Any, Callable, ClassVar, Optional, Sequence

import attr
import shortuuid

from bi_constants.enums import BIType

from bi_core_testing.database import Db, DbTable, C, make_table


def _int_or_none(v: Optional[str]) -> Optional[int]:
    return int(v) if v is not None else None


def _float_or_none(v: Optional[str]) -> Optional[float]:
    return float(v) if v is not None else None


def _date_or_none(v: Optional[str]) -> Optional[datetime.date]:
    return datetime.date.fromisoformat(v) if v is not None else None


def _datetime_or_none(v: Optional[str]) -> Optional[datetime.datetime]:
    return datetime.datetime.fromisoformat(v) if v is not None else None


@attr.s
class CsvTableDumper:
    db: Db = attr.ib(kw_only=True)

    _PY_CONVERTERS_BY_BITYPE: ClassVar[dict[BIType, Callable[[Optional[str]], Any]]] = {
        BIType.string: lambda v: v,
        BIType.integer: _int_or_none,
        BIType.float: _float_or_none,
        BIType.date: _date_or_none,
        BIType.datetime: _datetime_or_none,
    }

    def _convert_value(self, value: Optional[str], user_type: BIType) -> Any:
        return self._PY_CONVERTERS_BY_BITYPE[user_type](value)

    def _convert_row(self, row: Sequence[Optional[str]], type_schema: Sequence[BIType]) -> list[Any]:
        return [
            self._convert_value(v, t)
            for v, t in zip(row, type_schema)
        ]

    def _load_table_data(self, raw_csv_data: str, type_schema: Sequence[BIType]) -> list[list[Any]]:
        reader = csv.reader(io.StringIO(raw_csv_data))
        return [
            self._convert_row(row=row, type_schema=type_schema)
            for row in reader
        ]

    def make_table_from_csv(
            self,
            raw_csv_data: str,
            table_schema: Sequence[tuple[str, BIType]],
            table_name_prefix: Optional[str] = None,
    ) -> DbTable:

        table_name_prefix = table_name_prefix or 'table_'
        if not table_name_prefix.endswith('_'):
            table_name_prefix = f'{table_name_prefix}_'
        table_name = f'{table_name_prefix}{shortuuid.uuid()}'

        type_schema = [user_type for col_name, user_type in table_schema]
        data = self._load_table_data(raw_csv_data=raw_csv_data, type_schema=type_schema)

        def _value_gen_factory(_col_idx: int) -> Callable[[int, datetime.datetime, random.Random], Any]:
            def _value_gen(rn: int, ts: datetime.datetime, rnd: random.Random) -> Any:
                return data[rn][_col_idx]

            return _value_gen

        columns = [
            C(name=name, user_type=user_type, vg=_value_gen_factory(_col_idx=col_idx))  # type: ignore
            for col_idx, (name, user_type) in enumerate(table_schema)
        ]

        db_table = make_table(db=self.db, name=table_name, columns=columns, rows=len(data))
        return db_table