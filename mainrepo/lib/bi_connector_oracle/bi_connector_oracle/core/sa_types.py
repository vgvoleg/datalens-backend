from __future__ import annotations

import sqlalchemy as sa
from sqlalchemy.dialects.oracle import base as or_types  # not all data types are imported in init in older SA versions

from bi_core.db.sa_types_base import (
    make_native_type, simple_instantiator, lengthed_instantiator,
)

from bi_connector_oracle.core.constants import CONNECTION_TYPE_ORACLE

SQLALCHEMY_ORACLE_BASE_TYPES = (
    or_types.NUMBER, or_types.BINARY_FLOAT, or_types.BINARY_DOUBLE,
    or_types.DATE, or_types.TIMESTAMP,
)
SQLALCHEMY_ORACLE_LENGTHED_TYPES = (
    or_types.CHAR, sa.NCHAR,
    or_types.VARCHAR, or_types.NVARCHAR,
    or_types.VARCHAR2, or_types.NVARCHAR2,
)
SQLALCHEMY_ORACLE_TYPES = {
    **{make_native_type(CONNECTION_TYPE_ORACLE, typecls): simple_instantiator(typecls)
       for typecls in SQLALCHEMY_ORACLE_BASE_TYPES},
    # A tricky substitution (possibly in the wrong place):
    make_native_type(CONNECTION_TYPE_ORACLE, sa.Integer): simple_instantiator(or_types.NUMBER),
    **{make_native_type(CONNECTION_TYPE_ORACLE, typecls): lengthed_instantiator(typecls)
       for typecls in SQLALCHEMY_ORACLE_LENGTHED_TYPES}
}