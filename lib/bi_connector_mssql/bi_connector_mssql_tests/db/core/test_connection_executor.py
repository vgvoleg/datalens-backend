from typing import Optional

import pytest

from bi_testing.regulated_test import RegulatedTestParams

from bi_core.connection_models.common_models import DBIdent

from bi_core_testing.testcases.connection_executor import (
    DefaultSyncAsyncConnectionExecutorCheckBase,
    DefaultSyncConnectionExecutorTestSuite, DefaultAsyncConnectionExecutorTestSuite,
)

from bi_connector_mssql.core.us_connection import ConnectionMSSQL

from bi_connector_mssql_tests.db.config import CoreConnectionSettings
from bi_connector_mssql_tests.db.core.base import BaseMSSQLTestClass


class MSSQLSyncAsyncConnectionExecutorCheckBase(
        BaseMSSQLTestClass,
        DefaultSyncAsyncConnectionExecutorCheckBase[ConnectionMSSQL],
):

    test_params = RegulatedTestParams(
        mark_tests_failed={
            DefaultAsyncConnectionExecutorTestSuite.test_get_table_schema_info_for_nonexistent_table: (
                'Empty schema is returned instead of an error'),  # FIXME
        },
    )

    @pytest.fixture(scope='function')
    def db_ident(self) -> DBIdent:
        return DBIdent(db_name=CoreConnectionSettings.DB_NAME)

    def check_db_version(self, db_version: Optional[str]) -> None:
        assert db_version is not None
        assert '.' in db_version


class TestMSSQLSyncConnectionExecutor(
        MSSQLSyncAsyncConnectionExecutorCheckBase,
        DefaultSyncConnectionExecutorTestSuite[ConnectionMSSQL],
):
    pass


class TestMSSQLAsyncConnectionExecutor(
        MSSQLSyncAsyncConnectionExecutorCheckBase,
        DefaultAsyncConnectionExecutorTestSuite[ConnectionMSSQL],
):
    pass