from bi_api_lib_testing.connector.connection_suite import DefaultConnectorConnectionTestSuite

from bi_connector_bigquery_tests.ext.api.base import BigQueryConnectionTestBase


class TestBigQueryConnection(BigQueryConnectionTestBase, DefaultConnectorConnectionTestSuite):
    pass
