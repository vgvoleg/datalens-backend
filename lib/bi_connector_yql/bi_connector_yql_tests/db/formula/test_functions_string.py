from bi_formula.connectors.base.testing.functions_string import (
    DefaultStringFunctionFormulaConnectorTestSuite,
)
from bi_connector_yql_tests.db.formula.base import (
    YQLTestBase,
)


class TestStringFunctionYQL(YQLTestBase, DefaultStringFunctionFormulaConnectorTestSuite):
    datetime_str_separator = 'T'
    datetime_str_ending = 'Z'
    supports_trimming_funcs = False
    supports_regex_extract = False
    supports_regex_extract_nth = False
    supports_regex_replace = False
    supports_regex_match = False
