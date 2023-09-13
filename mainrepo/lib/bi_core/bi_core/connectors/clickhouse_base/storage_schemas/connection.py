from typing import TypeVar, Generic

from marshmallow import fields as ma_fields

from bi_core.connectors.clickhouse_base.us_connection import ConnectionClickhouseBase
from bi_core.us_manager.storage_schemas.connection import ConnectionSQLDataStorageSchema
from bi_connector_mdb_base.core.storage_schemas import ConnectionMDBStorageDataSchemaMixin


_CH_CONN_DATA_TV = TypeVar('_CH_CONN_DATA_TV', bound=ConnectionClickhouseBase.DataModel)


class ConnectionClickHouseBaseDataStorageSchema(
        ConnectionMDBStorageDataSchemaMixin,
        ConnectionSQLDataStorageSchema[_CH_CONN_DATA_TV], Generic[_CH_CONN_DATA_TV],
):
    secure = ma_fields.Boolean(allow_none=False, required=False, load_default=False, dump_default=False)
    ssl_ca = ma_fields.String(required=False, allow_none=True, load_default=None, dump_default=None)
    endpoint = ma_fields.String(required=False, allow_none=True, load_default=None, dump_default=None)
    cluster_name = ma_fields.String(required=False, allow_none=True, load_default=None, dump_default=None)
    max_execution_time = ma_fields.Integer(required=False, allow_none=True, load_default=None, dump_default=None)
