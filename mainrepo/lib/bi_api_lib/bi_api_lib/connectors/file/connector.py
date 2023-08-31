from __future__ import annotations

from bi_connector_bundle_chs3.file.core.connector import (
    FileS3TableCoreSourceDefinition,
    FileS3CoreConnectionDefinition,
    FileS3CoreConnector,
)

from bi_api_lib.connectors.chs3_base.connector import (
    BaseFileS3TableBiApiSourceDefinition,
    BaseFileS3BiApiConnectionDefinition,
    BaseFileS3BiApiConnector,
)
from bi_api_lib.connectors.file.connection_info import FileS3ConnectionInfoProvider
from bi_api_lib.connectors.file.schemas import FileS3ConnectionSchema


class FileS3TableBiApiSourceDefinition(BaseFileS3TableBiApiSourceDefinition):
    core_source_def_cls = FileS3TableCoreSourceDefinition


class FileS3BiApiConnectionDefinition(BaseFileS3BiApiConnectionDefinition):
    core_conn_def_cls = FileS3CoreConnectionDefinition
    api_generic_schema_cls = FileS3ConnectionSchema
    info_provider_cls = FileS3ConnectionInfoProvider


class FileS3BiApiConnector(BaseFileS3BiApiConnector):
    core_connector_cls = FileS3CoreConnector
    connection_definitions = (
        FileS3BiApiConnectionDefinition,
    )
    source_definitions = (
        FileS3TableBiApiSourceDefinition,
    )