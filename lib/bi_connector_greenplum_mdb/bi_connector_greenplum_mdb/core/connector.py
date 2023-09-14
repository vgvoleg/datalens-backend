from bi_connector_greenplum.core.connector import (
    GreenplumCoreConnectionDefinition,
    GreenplumCoreConnector,
    GreenplumTableCoreSourceDefinition,
    GreenplumSubselectCoreSourceDefinition,
)
from bi_connector_greenplum_mdb.core.data_source import GreenplumMDBTableDataSource, GreenplumMDBSubselectDataSource
from bi_connector_greenplum_mdb.core.us_connection import GreenplumMDBConnection
from bi_connector_greenplum_mdb.core.storage_schemas import GreenplumMDBConnectionDataStorageSchema
from bi_connector_greenplum_mdb.core.settings import GreenplumMDBSettingDefinition
from bi_connector_greenplum.core.dto import GreenplumConnDTO


class GreenplumMDBCoreConnectionDefinition(GreenplumCoreConnectionDefinition):
    connection_cls = GreenplumMDBConnection
    us_storage_schema_cls = GreenplumMDBConnectionDataStorageSchema
    settings_definition = GreenplumMDBSettingDefinition


class GreenplumMDBTableCoreSourceDefinition(GreenplumTableCoreSourceDefinition):
    source_cls = GreenplumMDBTableDataSource


class GreenplumMDBSubselectCoreSourceDefinition(GreenplumSubselectCoreSourceDefinition):
    source_cls = GreenplumMDBSubselectDataSource


class GreenplumMDBCoreConnector(GreenplumCoreConnector):
    connection_definitions = (
        GreenplumMDBCoreConnectionDefinition,
    )
    source_definitions = (
        GreenplumMDBTableCoreSourceDefinition,
        GreenplumMDBSubselectCoreSourceDefinition,
    )
    mdb_dto_classes = frozenset({GreenplumConnDTO})