from bi_formula.connectors.base.testing.functions_logical import (
    DefaultLogicalFunctionFormulaConnectorTestSuite,
)

from bi_connector_oracle_tests.db.formula.base import (
    OracleTestBase,
)


class TestLogicalFunctionOracle(OracleTestBase, DefaultLogicalFunctionFormulaConnectorTestSuite):
    supports_iif = True