from __future__ import annotations

from bi_api_connector.api_schema.source_base import SubselectDataSourceSchema, SubselectDataSourceTemplateSchema

from bi_api_connector.connector import (
    BiApiConnectionDefinition, BiApiConnector, BiApiSourceDefinition,
)
from bi_api_connector.api_schema.source_base import (
    SQLDataSourceSchema,
    SQLDataSourceTemplateSchema,
)

from bi_connector_clickhouse.formula.constants import DIALECT_NAME_CLICKHOUSE

from bi_connector_chyt.bi.api_schema.connection import CHYTConnectionSchema
from bi_connector_chyt.bi.api_schema.source import (
    CHYTTableListDataSourceSchema,
    CHYTTableListDataSourceTemplateSchema,
    CHYTTableRangeDataSourceSchema,
    CHYTTableRangeDataSourceTemplateSchema,
)
from bi_connector_chyt.bi.connection_form.form_config import CHYTConnectionFormFactory
from bi_connector_chyt.bi.connection_info import CHYTConnectionInfoProvider
from bi_connector_chyt.bi.i18n.localizer import CONFIGS

from bi_connector_chyt.core.connector import (
    CHYTCoreConnectionDefinition,
    CHYTTableCoreSourceDefinition,
    CHYTTableListCoreSourceDefinition,
    CHYTTableRangeCoreSourceDefinition,
    CHYTTableSubselectCoreSourceDefinition,
    CHYTCoreConnector,
)


class CHYTBiApiConnectionDefinition(BiApiConnectionDefinition):
    core_conn_def_cls = CHYTCoreConnectionDefinition
    api_generic_schema_cls = CHYTConnectionSchema
    info_provider_cls = CHYTConnectionInfoProvider
    form_factory_cls = CHYTConnectionFormFactory


class CHYTTableBiApiSourceDefinition(BiApiSourceDefinition):
    core_source_def_cls = CHYTTableCoreSourceDefinition
    api_schema_cls = SQLDataSourceSchema
    template_api_schema_cls = SQLDataSourceTemplateSchema


class CHYTTableListBiApiSourceDefinition(BiApiSourceDefinition):
    core_source_def_cls = CHYTTableListCoreSourceDefinition
    api_schema_cls = CHYTTableListDataSourceSchema
    template_api_schema_cls = CHYTTableListDataSourceTemplateSchema


class CHYTTableRangeBiApiSourceDefinition(BiApiSourceDefinition):
    core_source_def_cls = CHYTTableRangeCoreSourceDefinition
    api_schema_cls = CHYTTableRangeDataSourceSchema
    template_api_schema_cls = CHYTTableRangeDataSourceTemplateSchema


class CHYTSubselectBiApiSourceDefinition(BiApiSourceDefinition):
    core_source_def_cls = CHYTTableSubselectCoreSourceDefinition
    api_schema_cls = SubselectDataSourceSchema
    template_api_schema_cls = SubselectDataSourceTemplateSchema


class CHYTBiApiConnector(BiApiConnector):
    core_connector_cls = CHYTCoreConnector
    formula_dialect_name = DIALECT_NAME_CLICKHOUSE
    connection_definitions = (
        CHYTBiApiConnectionDefinition,
    )
    source_definitions = (
        CHYTTableBiApiSourceDefinition,
        CHYTTableListBiApiSourceDefinition,
        CHYTTableRangeBiApiSourceDefinition,
        CHYTSubselectBiApiSourceDefinition,
    )
    translation_configs = frozenset(CONFIGS)