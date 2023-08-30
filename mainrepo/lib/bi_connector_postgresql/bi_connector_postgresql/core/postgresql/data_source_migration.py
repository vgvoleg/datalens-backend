from bi_core.connectors.sql_base.data_source_migration import DefaultSQLDataSourceMigrator

from bi_connector_postgresql.core.postgresql.constants import SOURCE_TYPE_PG_TABLE, SOURCE_TYPE_PG_SUBSELECT


class PostgreSQLDataSourceMigrator(DefaultSQLDataSourceMigrator):
    table_source_type = SOURCE_TYPE_PG_TABLE
    subselect_source_type = SOURCE_TYPE_PG_SUBSELECT
    default_schema_name = 'public'