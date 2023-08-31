from bi_constants.enums import ConnectionType

from bi_api_lib.connector_availability.base import (
    ConnectorAvailabilityConfig,
    Connector,
)

from bi_connector_postgresql.core.postgresql.constants import CONNECTION_TYPE_POSTGRES


CONFIG = ConnectorAvailabilityConfig(
    uncategorized=[
        Connector(conn_type=ConnectionType.clickhouse, hidden=False),
        Connector(conn_type=CONNECTION_TYPE_POSTGRES, hidden=False),
    ],
)