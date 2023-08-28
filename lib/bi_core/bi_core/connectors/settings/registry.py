from typing import Type

from bi_configs.connectors_settings import ConnectorSettingsBase
from bi_constants.enums import ConnectionType

from bi_core.connectors.settings.primitives import SettingsFallbackType

CONNECTORS_SETTINGS_CLASSES: dict[ConnectionType, Type[ConnectorSettingsBase]] = {}
CONNECTORS_SETTINGS_FALLBACKS: dict[ConnectionType, SettingsFallbackType] = {}


def register_connector_settings_class(
        conn_type: ConnectionType,
        settings_class: Type[ConnectorSettingsBase],
        fallback: SettingsFallbackType,
) -> None:
    if (registered_settings_class := CONNECTORS_SETTINGS_CLASSES.get(conn_type)) is not None:
        assert registered_settings_class == settings_class
        assert CONNECTORS_SETTINGS_FALLBACKS[conn_type] == fallback
    else:
        assert conn_type not in CONNECTORS_SETTINGS_FALLBACKS
        CONNECTORS_SETTINGS_CLASSES[conn_type] = settings_class
        CONNECTORS_SETTINGS_FALLBACKS[conn_type] = fallback