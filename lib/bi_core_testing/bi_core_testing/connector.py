from bi_constants.enums import ConnectionType, CreateDSFrom

from bi_core.connectors.base.connector import CoreConnector, CoreConnectionDefinition, CoreSourceDefinition
from bi_core.db.conversion_base import TypeTransformer
from bi_core.us_connection_base import ConnectionBase
from bi_core.us_manager.storage_schemas.connection import BaseConnectionDataStorageSchema


CONNECTION_TYPE_TESTING = ConnectionType.declare('testing')
SOURCE_TYPE_TESTING = CreateDSFrom.declare('TESTING')


class TestingConnection(ConnectionBase):
    pass


class TestingTypeTransformer(TypeTransformer):
    conn_type = CONNECTION_TYPE_TESTING


class TestingConnectionDataStorageSchema(BaseConnectionDataStorageSchema):
    TARGET_CLS = TestingConnection.DataModel


class TestingCoreSourceDefinition(CoreSourceDefinition):
    source_type = SOURCE_TYPE_TESTING


class TestingCoreConnectionDefinition(CoreConnectionDefinition):
    connection_cls = TestingConnection
    conn_type = CONNECTION_TYPE_TESTING
    type_transformer_cls = TestingTypeTransformer
    us_storage_schema_cls = TestingConnectionDataStorageSchema
    dialect_string = 'testing'  # No such dialect


class TestingCoreConnector(CoreConnector):
    connection_definitions = (
        TestingCoreConnectionDefinition,
    )
    source_definitions = (
        TestingCoreSourceDefinition,
    )
