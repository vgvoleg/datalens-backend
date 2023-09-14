import abc
from typing import (
    ClassVar,
    Optional,
    Tuple,
    Type,
)

from bi_api_connector.api_schema.connection_base import ConnectionSchema
from bi_api_connector.api_schema.source_base import (
    DataSourceBaseSchema,
    DataSourceTemplateBaseSchema,
)
from bi_api_connector.connection_info import ConnectionInfoProvider
from bi_api_connector.dashsql import (
    DashSQLParamLiteralizer,
    DefaultDashSQLParamLiteralizer,
)
from bi_api_connector.form_config.models.base import ConnectionFormFactory
from bi_core.connectors.base.connector import (
    CoreConnectionDefinition,
    CoreConnector,
    CoreSourceDefinition,
)
from bi_formula.core.dialect import (
    DialectCombo,
    DialectName,
)
from bi_i18n.localizer_base import TranslationConfig
from bi_query_processing.compilation.filter_compiler import (
    FilterFormulaCompiler,
    MainFilterFormulaCompiler,
)
from bi_query_processing.legacy_pipeline.planning.planner import (
    ExecutionPlanner,
    WindowToCompengExecutionPlanner,
)
from bi_query_processing.multi_query.factory import (
    DefaultMultiQueryMutatorFactory,
    MultiQueryMutatorFactoryBase,
)


class BiApiSourceDefinition(abc.ABC):
    core_source_def_cls: ClassVar[Type[CoreSourceDefinition]]
    api_schema_cls: ClassVar[Type[DataSourceBaseSchema]] = DataSourceBaseSchema
    template_api_schema_cls: ClassVar[Type[DataSourceTemplateBaseSchema]] = DataSourceTemplateBaseSchema


class BiApiConnectionDefinition(abc.ABC):
    core_conn_def_cls: ClassVar[Type[CoreConnectionDefinition]]
    api_generic_schema_cls: ClassVar[Type[ConnectionSchema]]
    alias: ClassVar[Optional[str]] = None
    info_provider_cls: ClassVar[Type[ConnectionInfoProvider]]
    form_factory_cls: ClassVar[Optional[Type[ConnectionFormFactory]]] = None


class BiApiConnector(abc.ABC):
    # backend_type-bound properties - TODO: move to a separate entity
    formula_dialect_name: ClassVar[DialectName] = DialectName.DUMMY
    default_multi_query_mutator_factory_cls: ClassVar[
        Type[MultiQueryMutatorFactoryBase]
    ] = DefaultMultiQueryMutatorFactory
    legacy_initial_planner_cls: ClassVar[
        Type[ExecutionPlanner]
    ] = WindowToCompengExecutionPlanner  # TODO: Remove with old LODs
    is_forkable: ClassVar[bool] = True
    is_compeng_executable: ClassVar[bool] = False
    filter_formula_compiler_cls: ClassVar[Type[FilterFormulaCompiler]] = MainFilterFormulaCompiler
    dashsql_literalizer_cls: ClassVar[Type[DashSQLParamLiteralizer]] = DefaultDashSQLParamLiteralizer
    # others
    core_connector_cls: ClassVar[Type[CoreConnector]]
    connection_definitions: ClassVar[Tuple[Type[BiApiConnectionDefinition], ...]] = ()
    source_definitions: ClassVar[Tuple[Type[BiApiSourceDefinition], ...]] = ()
    translation_configs: ClassVar[frozenset[TranslationConfig]] = frozenset()
    compeng_dialect: Optional[DialectCombo] = None
