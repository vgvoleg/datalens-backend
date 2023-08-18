from bi_connector_mssql_tests.db.formula.base import (
    MSSQLTestBase,
)
from bi_formula.connectors.base.testing.functions_logical import (
    DefaultLogicalFunctionFormulaConnectorTestSuite,
)


class TestLogicalFunctionMSSQL(MSSQLTestBase, DefaultLogicalFunctionFormulaConnectorTestSuite):
    supports_iif = True
