from dl_api_lib_testing.connector.complex_queries import DefaultBasicComplexQueryTestSuite
from dl_constants.enums import QueryProcessingMode

from dl_connector_clickhouse_tests.db.api.base import ClickHouseDataApiTestBase


class TestClickHouseBasicComplexQueries(ClickHouseDataApiTestBase, DefaultBasicComplexQueryTestSuite):
    query_processing_mode = QueryProcessingMode.native_wf