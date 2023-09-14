import asyncio
from typing import Generator

import pytest

import bi_connector_oracle_tests.db.config as test_config
from bi_core_testing.testcases.connection import BaseConnectionTestClass
from bi_core.us_manager.us_manager_sync import SyncUSManager

from bi_connector_oracle.core.constants import CONNECTION_TYPE_ORACLE
from bi_connector_oracle.core.testing.connection import make_oracle_saved_connection
from bi_connector_oracle.core.us_connection import ConnectionSQLOracle


class BaseOracleTestClass(BaseConnectionTestClass[ConnectionSQLOracle]):
    conn_type = CONNECTION_TYPE_ORACLE
    core_test_config = test_config.CORE_TEST_CONFIG

    @pytest.fixture(autouse=True)
    # FIXME: This fixture is a temporary solution for failing core tests when they are run together with api tests
    def loop(self, event_loop: asyncio.AbstractEventLoop) -> Generator[asyncio.AbstractEventLoop, None, None]:
        asyncio.set_event_loop(event_loop)
        yield event_loop
        # Attempt to cover an old version of pytest-asyncio:
        # https://github.com/pytest-dev/pytest-asyncio/commit/51d986cec83fdbc14fa08015424c79397afc7ad9
        asyncio.set_event_loop_policy(None)

    @pytest.fixture(scope='class')
    def db_url(self, initdb_ready) -> str:
        return test_config.DB_CORE_URL

    @pytest.fixture(scope='function')
    def connection_creation_params(self) -> dict:
        return dict(
            db_name=test_config.CoreConnectionSettings.DB_NAME,
            host=test_config.CoreConnectionSettings.HOST,
            port=test_config.CoreConnectionSettings.PORT,
            username=test_config.CoreConnectionSettings.USERNAME,
            password=test_config.CoreConnectionSettings.PASSWORD,
            **(dict(raw_sql_level=self.raw_sql_level) if self.raw_sql_level is not None else {}),
        )

    @pytest.fixture(scope='function')
    def saved_connection(
            self, sync_us_manager: SyncUSManager, connection_creation_params: dict,
    ) -> ConnectionSQLOracle:
        conn = make_oracle_saved_connection(
            sync_usm=sync_us_manager,
            **connection_creation_params
        )
        return conn