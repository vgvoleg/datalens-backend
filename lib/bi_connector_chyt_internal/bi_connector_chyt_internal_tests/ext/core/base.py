from __future__ import annotations

import asyncio
from typing import Generic, Generator, TypeVar

import pytest
from multidict import CIMultiDict

from bi_constants.enums import ConnectionType, BIType

from bi_api_commons.base_models import RequestContextInfo

from bi_core.us_manager.us_manager_sync import SyncUSManager
from bi_connector_chyt_internal.core.us_connection import ConnectionCHYTInternalToken, ConnectionCHYTUserAuth
from bi_connector_chyt_internal.core.testing.connection import (
    make_saved_chyt_connection, make_saved_chyt_user_auth_connection
)
from bi_core_testing.testcases.connection import BaseConnectionTestClass
from bi_core_testing.database import Db, DbTable, make_table, C
from bi_core_testing.fixtures.sample_tables import TABLE_SPEC_SAMPLE_SUPERSTORE

import bi_connector_chyt_internal_tests.ext.config as common_test_config
import bi_connector_chyt_internal_tests.ext.core.config as test_config


_CONN_TV = TypeVar('_CONN_TV', ConnectionCHYTInternalToken, ConnectionCHYTUserAuth)


class CHYTTestSetup(BaseConnectionTestClass[_CONN_TV], Generic[_CONN_TV]):
    """
    CHYT has a completely external DB, so we need to skip
    DB initialization steps
    """

    @pytest.fixture(autouse=True)
    # FIXME: This fixture is a temporary solution for failing core tests when they are run together with api tests
    def loop(self, event_loop: asyncio.AbstractEventLoop) -> Generator[asyncio.AbstractEventLoop, None, None]:
        asyncio.set_event_loop(event_loop)
        yield event_loop
        # Attempt to cover an old version of pytest-asyncio:
        # https://github.com/pytest-dev/pytest-asyncio/commit/51d986cec83fdbc14fa08015424c79397afc7ad9
        asyncio.set_event_loop_policy(None)

    @pytest.fixture(scope='class')
    def db_url(self) -> str:
        return 'bi_chyt://...'

    @pytest.fixture(scope='class')
    def sample_table(self, db: Db) -> DbTable:
        # FIXME: Do this via a "smart" dispenser
        columns = [
            # Note: dates are stored as strings
            C(name=name, user_type=user_type if user_type != BIType.date else BIType.string)
            for name, user_type in TABLE_SPEC_SAMPLE_SUPERSTORE.table_schema
        ]
        return make_table(
            db=db,
            name=test_config.TEST_TABLES['sample_superstore'],
            columns=columns,
            create_in_db=False,
        )


class BaseCHYTTestClass(CHYTTestSetup[ConnectionCHYTInternalToken]):
    conn_type = ConnectionType.ch_over_yt
    core_test_config = common_test_config.CORE_TEST_CONFIG

    @pytest.fixture(scope='function')
    def connection_creation_params(self, yt_token: str) -> dict:
        return dict(
            token=yt_token,
            **test_config.DEFAULT_CONFIG
        )

    @pytest.fixture(scope='function')
    def saved_connection(
            self, sync_us_manager: SyncUSManager, connection_creation_params: dict,
    ) -> ConnectionCHYTInternalToken:
        return make_saved_chyt_connection(
            sync_usm=sync_us_manager,
            **connection_creation_params
        )


class CHYTInvalidTokenTestClass(BaseCHYTTestClass):
    @pytest.fixture(scope='function')
    def connection_creation_params(self) -> dict:
        return dict(
            token='invalid-token',
            **test_config.DEFAULT_CONFIG
        )


class CHYTNoRobotAccessTestClass(BaseCHYTTestClass):
    @pytest.fixture(scope='function')
    def connection_creation_params(self, yt_token: str) -> dict:
        return dict(
            token=yt_token,
            **test_config.NO_ROBOT_ACCESS_CONFIG
        )


class CHYTNotExistsTestClass(BaseCHYTTestClass):
    @pytest.fixture(scope='function')
    def connection_creation_params(self, yt_token: str) -> dict:
        return dict(
            token=yt_token,
            **test_config.NOT_EXISTS_CONFIG
        )


class BaseCHYTUserAuthTestClass(CHYTTestSetup[ConnectionCHYTUserAuth]):
    conn_type = ConnectionType.ch_over_yt_user_auth
    core_test_config = common_test_config.CORE_TEST_CONFIG

    @pytest.fixture(scope='session')
    def conn_bi_context(self, yt_token: str) -> RequestContextInfo:
        return RequestContextInfo.create_empty().clone(
            secret_headers=CIMultiDict({
                'Authorization': 'OAuth {}'.format(yt_token),
            }),
        )

    @pytest.fixture(scope='function')
    def connection_creation_params(self) -> dict:
        return test_config.DEFAULT_CONFIG

    @pytest.fixture(scope='function')
    def saved_connection(
            self, sync_us_manager: SyncUSManager, connection_creation_params: dict,
    ) -> ConnectionCHYTUserAuth:
        return make_saved_chyt_user_auth_connection(
            sync_usm=sync_us_manager,
            **connection_creation_params
        )
