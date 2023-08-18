from bi_connector_snowflake.formula.definitions.conditional_blocks import DEFINITIONS_COND_BLOCKS
from bi_connector_snowflake.formula.definitions.functions_aggregation import DEFINITIONS_AGG
from bi_connector_snowflake.formula.definitions.functions_datetime import DEFINITIONS_DATETIME
from bi_connector_snowflake.formula.definitions.functions_logical import DEFINITIONS_LOGICAL
from bi_connector_snowflake.formula.definitions.functions_string import DEFINITIONS_STRING
from bi_connector_snowflake.formula.definitions.operators_ternary import DEFINITIONS_TERNARY
from bi_connector_snowflake.formula.definitions.operators_unary import DEFINITIONS_UNARY
from bi_connector_snowflake.formula.definitions.operators_binary import DEFINITIONS_BINARY
from bi_connector_snowflake.formula.definitions.functions_markup import DEFINITIONS_MARKUP
from bi_connector_snowflake.formula.definitions.functions_math import DEFINITIONS_MATH
from bi_connector_snowflake.formula.definitions.functions_type import DEFINITIONS_TYPE

DEFINITIONS = [
    *DEFINITIONS_UNARY,
    *DEFINITIONS_BINARY,
    *DEFINITIONS_TERNARY,
    *DEFINITIONS_MARKUP,
    *DEFINITIONS_MATH,
    *DEFINITIONS_TYPE,
    *DEFINITIONS_LOGICAL,
    *DEFINITIONS_STRING,
    *DEFINITIONS_COND_BLOCKS,
    *DEFINITIONS_AGG,
    *DEFINITIONS_DATETIME,
]
