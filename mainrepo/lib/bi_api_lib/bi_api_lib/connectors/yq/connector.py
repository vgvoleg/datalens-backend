from __future__ import annotations

from bi_api_lib.connectors.yq.connection_info import YQConnectionInfoProvider
from bi_connector_yql.core.yq.connector import (
    YQCoreConnectionDefinition, YQCoreConnector,
    YQSubselectCoreSourceDefinition, YQTableCoreSourceDefinition,
)

from bi_api_connector.connector import (
    BiApiConnectionDefinition, BiApiConnector, BiApiSourceDefinition,
)
from bi_api_connector.api_schema.source_base import (
    SimpleDataSourceSchema, SimpleDataSourceTemplateSchema,
    SubselectDataSourceSchema, SubselectDataSourceTemplateSchema,
)

from bi_connector_yql.formula.constants import DIALECT_NAME_YQ
from bi_api_lib.connectors.yq.connection_form.form_config import YQConnectionFormFactory
from bi_api_lib.connectors.yq.schemas import YQConnectionSchema


class YQTableBiApiSourceDefinition(BiApiSourceDefinition):
    core_source_def_cls = YQTableCoreSourceDefinition
    api_schema_cls = SimpleDataSourceSchema
    template_api_schema_cls = SimpleDataSourceTemplateSchema


class YQSubselectBiApiSourceDefinition(BiApiSourceDefinition):
    core_source_def_cls = YQSubselectCoreSourceDefinition
    api_schema_cls = SubselectDataSourceSchema
    template_api_schema_cls = SubselectDataSourceTemplateSchema


class YQBiApiConnectionDefinition(BiApiConnectionDefinition):
    core_conn_def_cls = YQCoreConnectionDefinition
    api_generic_schema_cls = YQConnectionSchema
    form_factory_cls = YQConnectionFormFactory
    info_provider_cls = YQConnectionInfoProvider


class YQBiApiConnector(BiApiConnector):
    core_connector_cls = YQCoreConnector
    formula_dialect_name = DIALECT_NAME_YQ
    connection_definitions = (
        YQBiApiConnectionDefinition,
    )
    source_definitions = (
        YQTableBiApiSourceDefinition,
        YQSubselectBiApiSourceDefinition,
    )