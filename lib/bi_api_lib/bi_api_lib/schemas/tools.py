from __future__ import annotations

from typing import Any, Dict, Optional

from bi_core.us_manager.us_manager import USManagerBase

from bi_api_connector.api_schema.extras import OperationsMode
from bi_api_connector.api_schema.top_level import BaseTopLevelSchema, USEntryBaseSchema


def prepare_schema_context(
    usm: Optional[USManagerBase] = None,
    op_mode: Optional[OperationsMode] = None,
    editable_object: Optional[Any] = None,
) -> Dict[Any, Any]:
    return {
        BaseTopLevelSchema.CTX_KEY_EDITABLE_OBJECT: editable_object,
        BaseTopLevelSchema.CTX_KEY_OPERATIONS_MODE: op_mode,
        USEntryBaseSchema.CTX_KEY_USM: usm
    }
