from bi_core.connectors.base.connector import (
    CoreConnector,
    CoreConnectionDefinition,
    CoreSourceDefinition,
)

from bi_connector_snowflake.core.constants import (
    BACKEND_TYPE_SNOWFLAKE, CONNECTION_TYPE_SNOWFLAKE,
    SOURCE_TYPE_SNOWFLAKE_TABLE, SOURCE_TYPE_SNOWFLAKE_SUBSELECT,
)
from bi_connector_snowflake.core.adapters import SnowFlakeDefaultAdapter
from bi_connector_snowflake.core.connection_executors import SnowFlakeSyncConnExecutor
from bi_connector_snowflake.core.data_source import (
    SnowFlakeTableDataSource,
    SnowFlakeSubselectDataSource,
)
from bi_connector_snowflake.core.data_source_spec import (
    SnowFlakeTableDataSourceSpec,
    SnowFlakeSubselectDataSourceSpec,
)
from bi_connector_snowflake.core.lifecycle import SnowFlakeConnectionLifecycleManager
from bi_connector_snowflake.core.storage_schemas.connection import SnowFlakeConnectionDataStorageSchema
from bi_connector_snowflake.core.storage_schemas.data_source_spec import SnowFlakeTableDataSourceSpecStorageSchema, \
    SnowFlakeSubselectDataSourceSpecStorageSchema
from bi_connector_snowflake.core.type_transformer import SnowFlakeTypeTransformer
from bi_connector_snowflake.core.us_connection import ConnectionSQLSnowFlake
from bi_connector_snowflake.core.notifications import SnowflakeRefreshTokenSoonToExpire


class SnowFlakeCoreConnectionDefinition(CoreConnectionDefinition):
    conn_type = CONNECTION_TYPE_SNOWFLAKE
    connection_cls = ConnectionSQLSnowFlake
    us_storage_schema_cls = SnowFlakeConnectionDataStorageSchema
    type_transformer_cls = SnowFlakeTypeTransformer
    sync_conn_executor_cls = SnowFlakeSyncConnExecutor
    lifecycle_manager_cls = SnowFlakeConnectionLifecycleManager
    dialect_string = 'snowflake'


class SnowFlakeCoreTableSourceDefinition(CoreSourceDefinition):
    source_type = SOURCE_TYPE_SNOWFLAKE_TABLE
    source_cls = SnowFlakeTableDataSource
    source_spec_cls = SnowFlakeTableDataSourceSpec
    us_storage_schema_cls = SnowFlakeTableDataSourceSpecStorageSchema


class SnowFlakeCoreSubselectSourceDefinition(CoreSourceDefinition):
    source_type = SOURCE_TYPE_SNOWFLAKE_SUBSELECT
    source_cls = SnowFlakeSubselectDataSource
    source_spec_cls = SnowFlakeSubselectDataSourceSpec
    us_storage_schema_cls = SnowFlakeSubselectDataSourceSpecStorageSchema


class SnowFlakeCoreConnector(CoreConnector):
    backend_type = BACKEND_TYPE_SNOWFLAKE
    connection_definitions = (SnowFlakeCoreConnectionDefinition,)
    source_definitions = (
        SnowFlakeCoreTableSourceDefinition,
        SnowFlakeCoreSubselectSourceDefinition,
    )
    rqe_adapter_classes = frozenset({SnowFlakeDefaultAdapter})
    notification_classes = (
        SnowflakeRefreshTokenSoonToExpire,
    )