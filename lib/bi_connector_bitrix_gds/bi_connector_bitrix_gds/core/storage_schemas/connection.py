from marshmallow import fields as ma_fields

from bi_connector_bitrix_gds.core.us_connection import BitrixGDSConnection
from bi_core.us_manager.storage_schemas.connection import (
    CacheableConnectionDataSchemaMixin,
    ConnectionBaseDataStorageSchema,
)


class BitrixGDSConnectionDataStorageSchema(
        CacheableConnectionDataSchemaMixin,
        ConnectionBaseDataStorageSchema[BitrixGDSConnection.DataModel],
):
    TARGET_CLS = BitrixGDSConnection.DataModel

    portal = ma_fields.String(required=True, allow_none=False)
    token = ma_fields.String(required=True, allow_none=False)
