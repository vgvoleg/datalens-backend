from dl_api_connector.connection_info import ConnectionInfoProvider
from bi_connector_yql.bi.yql_base.i18n.localizer import Translatable


class YDBConnectionInfoProvider(ConnectionInfoProvider):
    title_translatable = Translatable('label_connector-ydb')
