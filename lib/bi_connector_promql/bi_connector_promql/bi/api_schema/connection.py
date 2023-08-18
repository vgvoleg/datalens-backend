from __future__ import annotations

from marshmallow import fields as ma_fields

from bi_connector_promql.core.us_connection import PromQLConnection

from bi_api_connector.api_schema.extras import FieldExtra
from bi_api_connector.api_schema.connection_base_fields import secret_string_field
from bi_api_connector.api_schema.connection_base import (
    ConnectionMetaMixin,
)
from bi_api_connector.api_schema.connection_sql import ClassicSQLConnectionSchema


class PromQLConnectionSchema(ConnectionMetaMixin, ClassicSQLConnectionSchema):
    TARGET_CLS = PromQLConnection  # type: ignore

    secure = ma_fields.Boolean(attribute='data.secure', bi_extra=FieldExtra(editable=True))
    username = ma_fields.String(
        attribute='data.username',
        required=False,
        allow_none=True,
        dump_default=None,
        bi_extra=FieldExtra(editable=True),
    )
    password = secret_string_field(
        attribute='data.password',
        required=False,
        allow_none=True,
        bi_extra=FieldExtra(editable=True),
    )
