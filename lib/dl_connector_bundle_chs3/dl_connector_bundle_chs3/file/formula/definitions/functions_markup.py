from dl_connector_bundle_chs3.file.formula.utils import clickhouse_funcs_for_file_dialect
from dl_connector_clickhouse.formula.definitions.functions_markup import DEFINITIONS_MARKUP as CH_DEFINITIONS_MARKUP


DEFINITIONS_MARKUP = clickhouse_funcs_for_file_dialect(CH_DEFINITIONS_MARKUP)
