from __future__ import annotations

from bi_api_connector.api_schema.source_base import SubselectDataSourceSchema, SubselectDataSourceTemplateSchema

from bi_formula.core.dialect import DialectName

from bi_connector_chyt.core.connector import (
    CHYTCoreConnectionDefinition,
    CHYTTableCoreSourceDefinition,
    CHYTTableListCoreSourceDefinition,
    CHYTTableRangeCoreSourceDefinition,
    CHYTTableSubselectCoreSourceDefinition,
    CHYTCoreConnector,
)

from bi_api_connector.connector import (
    BiApiConnectionDefinition, BiApiConnector, BiApiSourceDefinition,
)
from bi_api_connector.api_schema.source_base import (
    SQLDataSourceSchema,
    SQLDataSourceTemplateSchema,
)

from bi_api_lib.connectors.chyt.api_schema.connection import CHYTConnectionSchema
from bi_api_lib.connectors.chyt.api_schema.source import (
    CHYTTableListDataSourceSchema,
    CHYTTableListDataSourceTemplateSchema,
    CHYTTableRangeDataSourceSchema,
    CHYTTableRangeDataSourceTemplateSchema,
)

from bi_api_lib.connectors.chyt.connection_form.form_config import CHYTConnectionFormFactory
from bi_api_lib.connectors.chyt.connection_info import CHYTConnectionInfoProvider


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
    formula_dialect_name = DialectName.CLICKHOUSE
    connection_definitions = (
        CHYTBiApiConnectionDefinition,
    )
    source_definitions = (
        CHYTTableBiApiSourceDefinition,
        CHYTTableListBiApiSourceDefinition,
        CHYTTableRangeBiApiSourceDefinition,
        CHYTSubselectBiApiSourceDefinition,
    )
