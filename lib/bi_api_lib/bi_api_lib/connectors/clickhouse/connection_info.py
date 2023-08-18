from bi_api_connector.connection_info import ConnectionInfoProvider
from bi_api_lib.i18n.localizer import Translatable


class ClickHouseConnectionInfoProvider(ConnectionInfoProvider):
    title_translatable = Translatable('label_connector-clickhouse')
