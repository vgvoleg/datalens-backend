from bi_connector_mssql_tests.db.formula.base import (
    MSSQLTestBase,
)
from bi_formula_testing.testcases.conditional_blocks import (
    DefaultConditionalBlockFormulaConnectorTestSuite,
)


class TestConditionalBlockMSSQL(MSSQLTestBase, DefaultConditionalBlockFormulaConnectorTestSuite):
    pass