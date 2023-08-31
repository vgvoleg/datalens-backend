from bi_constants.enums import SourceBackendType

from bi_core.connectors.base.connector import (
    CoreConnectionDefinition, CoreConnector, CoreSourceDefinition,
)
from bi_connector_bundle_chs3.chs3_base.core.dto import BaseFileS3ConnDTO
from bi_connector_bundle_chs3.chs3_base.core.type_transformer import FileTypeTransformer


class BaseFileS3CoreConnectionDefinition(CoreConnectionDefinition):
    type_transformer_cls = FileTypeTransformer
    dialect_string = 'bi_clickhouse'


class BaseFileS3TableCoreSourceDefinition(CoreSourceDefinition):
    pass


class BaseFileS3CoreConnector(CoreConnector):
    backend_type = SourceBackendType.CHS3
    safe_dto_classes = frozenset({BaseFileS3ConnDTO})