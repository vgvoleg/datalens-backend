from bi_formula_testing.testcases.conditional_blocks import (
    DefaultConditionalBlockFormulaConnectorTestSuite,
)

from bi_connector_bigquery_tests.ext.formula.base import BigQueryTestBase


class TestConditionalBlockBigQuery(BigQueryTestBase, DefaultConditionalBlockFormulaConnectorTestSuite):
    pass
