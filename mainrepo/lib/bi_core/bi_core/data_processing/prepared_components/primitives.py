from __future__ import annotations

from typing import Any, Collection, Optional, Sequence, TYPE_CHECKING

import attr

from bi_constants.enums import BIType, JoinType

from bi_core.connectors.base.query_compiler import QueryCompiler
from bi_core.query.bi_query import SqlSourceType

if TYPE_CHECKING:
    import bi_core.data_source
    from bi_core.base_models import ConnectionRef


@attr.s(frozen=True)
class PreparedFromInfo:
    """
    Represents an entity that can be used in a ``FROM`` clause of a ``SELECT`` statement.
    In the simplest case - an SQL data source (database table),
    but can also itself be a ``SELECT`` statement.
    Can reflect a static ``SourceAvatar`` as well as a dynamic combination of avatars
    created during the formation of complex ``SELECT`` statements.
    """

    sql_source: Optional[SqlSourceType] = attr.ib(kw_only=True)
    query_compiler: QueryCompiler = attr.ib(kw_only=True)
    supported_join_types: Collection[JoinType] = attr.ib(kw_only=True)
    data_source_list: Optional[tuple[bi_core.data_source.BaseSQLDataSource, ...]] = attr.ib(kw_only=True)
    db_name: Optional[str] = attr.ib(kw_only=True)
    connect_args: dict[str, Any] = attr.ib(kw_only=True)
    pass_db_query_to_user: bool = attr.ib(kw_only=True)
    target_connection_ref: Optional[ConnectionRef] = attr.ib(kw_only=True)

    def supports_join_type(self, join_type: JoinType) -> bool:
        return join_type in self.supported_join_types

    @property
    def non_null_sql_source(self) -> SqlSourceType:
        assert self.sql_source is not None
        return self.sql_source


@attr.s(frozen=True)
class PreparedMultiFromInfo(PreparedFromInfo):
    pass


@attr.s(frozen=True)
class PreparedSingleFromInfo(PreparedFromInfo):
    """
    Represents an entity that can be used in a ``FROM`` clause of a ``SELECT`` statement.
    In the simplest case - an SQL data source (database table),
    but can also itself be a ``SELECT`` statement.
    Can reflect a static ``SourceAvatar`` as well as a dynamic combination of avatars
    created during the formation of complex ``SELECT`` statements.
    """

    id: str = attr.ib(kw_only=True)
    alias: str = attr.ib(kw_only=True)
    col_names: Sequence[str] = attr.ib(kw_only=True)
    user_types: Sequence[BIType] = attr.ib(kw_only=True)