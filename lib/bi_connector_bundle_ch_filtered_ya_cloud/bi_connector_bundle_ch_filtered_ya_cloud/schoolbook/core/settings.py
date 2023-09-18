from typing import ClassVar, Optional

import attr

from dl_configs.connectors_data import ConnectorsDataBase
from dl_configs.connectors_settings import ConnectorsConfigType, ConnectorSettingsBase
from dl_configs.settings_loaders.meta_definition import required

from dl_core.connectors.settings.primitives import ConnectorSettingsDefinition, get_connectors_settings_config

from bi_connector_bundle_ch_filtered.base.core.settings import ServiceConnectorSettingsBase


@attr.s(frozen=True)
class SchoolbookConnectorSettings(ServiceConnectorSettingsBase):
    """"""


class ConnectorsDataSchoolbookBase(ConnectorsDataBase):
    CONN_SCHOOLBOOK_HOST: ClassVar[Optional[str]] = None
    CONN_SCHOOLBOOK_PORT: ClassVar[Optional[int]] = None
    CONN_SCHOOLBOOK_DB_MAME: ClassVar[Optional[str]] = None
    CONN_SCHOOLBOOK_USERNAME: ClassVar[Optional[str]] = None
    CONN_SCHOOLBOOK_USE_MANAGED_NETWORK: ClassVar[Optional[bool]] = None
    CONN_SCHOOLBOOK_ALLOWED_TABLES: ClassVar[Optional[list[str]]] = None
    CONN_SCHOOLBOOK_SUBSELECT_TEMPLATES: ClassVar[Optional[tuple[dict[str, str], ...]]] = None

    @classmethod
    def connector_name(cls) -> str:
        return 'SCHOOLBOOK'


def schoolbook_settings_fallback(full_cfg: ConnectorsConfigType) -> dict[str, ConnectorSettingsBase]:
    cfg = get_connectors_settings_config(
        full_cfg, object_like_config_key='SCHOOLBOOK', connector_data_class=ConnectorsDataSchoolbookBase,
    )
    if cfg is None:
        return {}
    return dict(
        SCHOOLBOOK_JOURNAL=SchoolbookConnectorSettings(  # type: ignore
            HOST=cfg.CONN_SCHOOLBOOK_HOST,
            PORT=cfg.CONN_SCHOOLBOOK_PORT,
            DB_NAME=cfg.CONN_SCHOOLBOOK_DB_MAME,
            USERNAME=cfg.CONN_SCHOOLBOOK_USERNAME,
            USE_MANAGED_NETWORK=cfg.CONN_SCHOOLBOOK_USE_MANAGED_NETWORK,
            ALLOWED_TABLES=cfg.CONN_SCHOOLBOOK_ALLOWED_TABLES,
            SUBSELECT_TEMPLATES=tuple(cfg.CONN_SCHOOLBOOK_SUBSELECT_TEMPLATES),  # type: ignore
            PASSWORD=required(str),
        )
    )


class CHSchoolbookSettingDefinition(ConnectorSettingsDefinition):
    settings_class = SchoolbookConnectorSettings
    fallback = schoolbook_settings_fallback
