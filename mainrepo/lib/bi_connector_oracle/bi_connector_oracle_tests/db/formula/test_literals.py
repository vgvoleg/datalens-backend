from bi_formula.connectors.base.testing.literals import (
    DefaultLiteralFormulaConnectorTestSuite,
)

from bi_connector_oracle_tests.db.formula.base import (
    OracleTestBase,
)


class TestConditionalBlockOracle(OracleTestBase, DefaultLiteralFormulaConnectorTestSuite):
    supports_microseconds = False
    supports_utc = False
    supports_custom_tz = False