from bi_connector_mssql.bi.connection_form.form_config import MSSQLConnectionFormFactory

from bi_api_connector.form_config.testing.test_connection_form_base import ConnectionFormTestBase
from bi_api_connector.i18n.localizer import CONFIGS as BI_API_CONNECTOR_CONFIGS

from bi_connector_mssql.bi.i18n.localizer import CONFIGS as BI_CONNECTOR_MSSQL_CONFIGS


class TestMSSQLConnectionForm(ConnectionFormTestBase):
    CONN_FORM_FACTORY_CLS = MSSQLConnectionFormFactory
    TRANSLATION_CONFIGS = BI_API_CONNECTOR_CONFIGS + BI_CONNECTOR_MSSQL_CONFIGS
