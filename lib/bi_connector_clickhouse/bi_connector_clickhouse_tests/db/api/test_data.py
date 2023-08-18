from bi_api_lib_testing.connector.data_api_suites import (
    DefaultConnectorDataResultTestSuite,
    DefaultConnectorDataGroupByFormulaTestSuite,
    DefaultConnectorDataRangeTestSuite,
    DefaultConnectorDataDistinctTestSuite,
    DefaultConnectorDataPreviewTestSuite,
)

from bi_connector_clickhouse_tests.db.api.base import ClickHouseDataApiTestBase


class TestClickHouseDataResult(ClickHouseDataApiTestBase, DefaultConnectorDataResultTestSuite):
    do_test_arrays = True


class TestClickHouseDataGroupBy(ClickHouseDataApiTestBase, DefaultConnectorDataGroupByFormulaTestSuite):
    pass


class TestClickHouseDataRange(ClickHouseDataApiTestBase, DefaultConnectorDataRangeTestSuite):
    pass


class TestClickHouseDataDistinct(ClickHouseDataApiTestBase, DefaultConnectorDataDistinctTestSuite):
    pass


class TestClickHouseDataPreview(ClickHouseDataApiTestBase, DefaultConnectorDataPreviewTestSuite):
    pass
