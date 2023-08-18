from typing import Optional

import pytest

from bi_configs.connectors_settings import ConnectorsSettingsByType, GreenplumConnectorSettings

from bi_api_commons.base_models import TenantDef, TenantYCFolder, TenantYCOrganization
from bi_api_connector.form_config.testing.test_connection_form_base import ConnectionFormTestBase
from bi_api_connector.i18n.localizer import CONFIGS as BI_API_CONNECTOR_CONFIGS

from bi_api_lib.connectors.greenplum.connection_form.form_config import GreenplumConnectionFormFactory
from bi_api_lib.i18n.localizer import CONFIGS as BI_API_LIB_CONFIGS


class TestGreenplumConnectionForm(ConnectionFormTestBase):
    CONN_FORM_FACTORY_CLS = GreenplumConnectionFormFactory
    TRANSLATION_CONFIGS = BI_API_CONNECTOR_CONFIGS + BI_API_LIB_CONFIGS

    @pytest.fixture(
        params=(True, False),
        ids=('with_mdb', 'no_mdb'),
    )
    def connectors_settings(self, request) -> Optional[ConnectorsSettingsByType]:
        return ConnectorsSettingsByType(GREENPLUM=GreenplumConnectorSettings(USE_MDB_CLUSTER_PICKER=request.param))

    @pytest.fixture(
        params=(TenantYCFolder(folder_id='some_folder_id'), TenantYCOrganization(org_id='some_org_id')),
        ids=('in_folder', 'in_org'),
    )
    def tenant(self, request) -> TenantDef:
        return request.param
