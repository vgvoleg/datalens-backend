from bi_connector_mssql_tests.db.formula.base import (
    MSSQLTestBase,
)
from bi_formula_testing.testcases.operators import (
    DefaultOperatorFormulaConnectorTestSuite,
)


class TestOperatorMSSQL(MSSQLTestBase, DefaultOperatorFormulaConnectorTestSuite):
    pass