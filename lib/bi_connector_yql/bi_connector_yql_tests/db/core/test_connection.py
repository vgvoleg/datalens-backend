from __future__ import annotations

from dl_core.us_connection_base import DataSourceTemplate
from dl_core_testing.testcases.connection import DefaultConnectionTestClass
from dl_testing.regulated_test import RegulatedTestParams

from bi_connector_yql.core.yq.us_connection import YQConnection
import bi_connector_yql_tests.db.config as test_config
from bi_connector_yql_tests.db.core.base import BaseYQTestClass


class TestYQConnection(
    BaseYQTestClass,
    DefaultConnectionTestClass[YQConnection],
):
    test_params = RegulatedTestParams(
        mark_tests_skipped={
            DefaultConnectionTestClass.test_connection_test: "Requires YC clients",
        }
    )

    def check_saved_connection(self, conn: YQConnection, params: dict) -> None:
        assert conn.uuid is not None
        assert conn.data.service_account_id == params["service_account_id"]
        assert conn.data.folder_id == params["folder_id"]
        assert conn.data.password == params["password"]

        conn_dto = conn.get_conn_dto()
        assert conn_dto.host == test_config.SR_CONNECTION_SETTINGS.HOST
        assert conn_dto.port == test_config.SR_CONNECTION_SETTINGS.PORT
        assert conn_dto.db_name == test_config.SR_CONNECTION_SETTINGS.DB_NAME

    def check_data_source_templates(self, conn: YQConnection, dsrc_templates: list[DataSourceTemplate]) -> None:
        assert not dsrc_templates
