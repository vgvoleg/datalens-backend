from dl_formula_testing.testcases.functions_aggregation import DefaultMainAggFunctionFormulaConnectorTestSuite

from dl_connector_bigquery_tests.ext.formula.base import BigQueryTestBase


class TestMainAggFunctionBigQuery(BigQueryTestBase, DefaultMainAggFunctionFormulaConnectorTestSuite):
    supports_countd_approx = True