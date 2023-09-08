import pytest

from bi_formula_testing.testcases.base import (
    FormulaConnectorTestBase
)


from bi_connector_oracle.formula.constants import OracleDialect as D

from bi_connector_oracle_tests.db.config import DB_URLS


class OracleTestBase(FormulaConnectorTestBase):
    dialect = D.ORACLE_12_0
    supports_arrays = False
    supports_uuid = False
    bool_is_expression = True
    empty_str_is_null = True  # '' and NULL are the same thing
    null_casts_to_number = True

    @pytest.fixture(scope='class')
    def db_url(self, initdb_ready) -> str:
        return DB_URLS[self.dialect]
