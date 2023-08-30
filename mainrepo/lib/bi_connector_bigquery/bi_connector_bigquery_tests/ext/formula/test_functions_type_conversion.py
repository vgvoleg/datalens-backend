from bi_formula.connectors.base.testing.functions_type_conversion import (
    DefaultStrTypeFunctionFormulaConnectorTestSuite,
    DefaultFloatTypeFunctionFormulaConnectorTestSuite,
    DefaultBoolTypeFunctionFormulaConnectorTestSuite,
    DefaultIntTypeFunctionFormulaConnectorTestSuite,
    DefaultDateTypeFunctionFormulaConnectorTestSuite,
    DefaultGenericDatetimeTypeFunctionFormulaConnectorTestSuite,
    DefaultGeopointTypeFunctionFormulaConnectorTestSuite,
    DefaultGeopolygonTypeFunctionFormulaConnectorTestSuite,
)
from bi_connector_bigquery_tests.ext.formula.base import (
    BigQueryTestBase,
)


# STR

class TestStrTypeFunctionBigQuery(BigQueryTestBase, DefaultStrTypeFunctionFormulaConnectorTestSuite):
    skip_custom_tz = True


# FLOAT

class TestFloatTypeFunctionBigQuery(BigQueryTestBase, DefaultFloatTypeFunctionFormulaConnectorTestSuite):
    pass


# BOOL

class TestBoolTypeFunctionBigQuery(BigQueryTestBase, DefaultBoolTypeFunctionFormulaConnectorTestSuite):
    pass


# INT

class TestIntTypeFunctionBigQuery(BigQueryTestBase, DefaultIntTypeFunctionFormulaConnectorTestSuite):
    pass


# DATE

class TestDateTypeFunctionBigQuery(BigQueryTestBase, DefaultDateTypeFunctionFormulaConnectorTestSuite):
    pass


# GENERICDATETIME (& DATETIME)

class TestGenericDatetimeTypeFunctionBigQuery(
        BigQueryTestBase, DefaultGenericDatetimeTypeFunctionFormulaConnectorTestSuite,
):
    pass


# GEOPOINT

class TestGeopointTypeFunctionBigQuery(
        BigQueryTestBase, DefaultGeopointTypeFunctionFormulaConnectorTestSuite,
):
    pass


# GEOPOLYGON

class TestGeopolygonTypeFunctionBigQuery(
        BigQueryTestBase, DefaultGeopolygonTypeFunctionFormulaConnectorTestSuite,
):
    pass