from __future__ import annotations

from dl_connector_postgresql.core.postgresql.data_source import PostgreSQLDataSource, PostgreSQLSubselectDataSource


class PostgreSQLMDBDataSource(PostgreSQLDataSource):
    """ MDB PG table """


class PostgreSQLMDBSubselectDataSource(PostgreSQLSubselectDataSource):
    """ MDB PG subselect """
