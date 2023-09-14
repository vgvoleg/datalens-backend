from enum import Enum, unique

from bi_constants.enums import ConnectionType, SourceBackendType, CreateDSFrom


BACKEND_TYPE_ORACLE = SourceBackendType.declare('ORACLE')
CONNECTION_TYPE_ORACLE = ConnectionType.declare('oracle')
SOURCE_TYPE_ORACLE_TABLE = CreateDSFrom.declare('ORACLE_TABLE')
SOURCE_TYPE_ORACLE_SUBSELECT = CreateDSFrom.declare('ORACLE_SUBSELECT')


@unique
class OracleDbNameType(Enum):
    sid = 'sid'
    service_name = 'service_name'