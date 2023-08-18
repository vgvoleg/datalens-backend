from __future__ import annotations

import pytest

from bi_configs.connectors_settings import ConnectorsSettingsByType, SchoolbookConnectorSettings

from bi_core.us_manager.us_manager_sync import SyncUSManager

from bi_connector_bundle_ch_filtered_ya_cloud.ch_ya_music_podcast_stats.core.constants import (
    CONNECTION_TYPE_CH_YA_MUSIC_PODCAST_STATS,
)
from bi_connector_bundle_ch_filtered_ya_cloud.schoolbook.core.us_connection import ConnectionClickhouseSchoolbook
from bi_connector_bundle_ch_filtered_ya_cloud.schoolbook.core.testing.connection import (
    make_saved_schoolbook_journal_connection,
)

import bi_connector_bundle_ch_filtered_ya_cloud_tests.ext.config as test_config
from bi_connector_bundle_ch_filtered_ya_cloud_tests.ext.base import (
    BaseClickhouseFilteredSubselectByPuidTestClass, ClickhouseFilteredSubselectByPuidTestClassWithWrongAuth,
)


class BaseSchoolbookTestClass(BaseClickhouseFilteredSubselectByPuidTestClass[ConnectionClickhouseSchoolbook]):
    conn_type = CONNECTION_TYPE_CH_YA_MUSIC_PODCAST_STATS
    connection_settings = ConnectorsSettingsByType(
        SCHOOLBOOK=SchoolbookConnectorSettings(**test_config.SR_CONNECTION_SETTINGS_PARAMS)
    )

    @pytest.fixture(scope='function')
    def saved_connection(
            self, sync_us_manager: SyncUSManager, connection_creation_params: dict
    ) -> ConnectionClickhouseSchoolbook:
        conn = make_saved_schoolbook_journal_connection(
            sync_usm=sync_us_manager,
            **connection_creation_params
        )
        return sync_us_manager.get_by_id(conn.uuid)  # to invoke a lifecycle manager


class SchoolbookTestClassWithWrongAuth(
        BaseSchoolbookTestClass,
        ClickhouseFilteredSubselectByPuidTestClassWithWrongAuth[ConnectionClickhouseSchoolbook],
):
    pass
