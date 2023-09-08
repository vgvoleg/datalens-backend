from bi_formula_testing.testcases.functions_datetime import (
    DefaultDateTimeFunctionFormulaConnectorTestSuite,
)

from bi_connector_bigquery_tests.ext.formula.base import BigQueryTestBase


class TestDateTimeFunctionBigQuery(BigQueryTestBase, DefaultDateTimeFunctionFormulaConnectorTestSuite):
    pass
