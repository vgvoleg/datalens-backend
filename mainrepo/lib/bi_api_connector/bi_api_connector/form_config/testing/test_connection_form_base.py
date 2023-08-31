import json
from typing import ClassVar, Optional, Type, final

import pytest

from bi_configs.connectors_settings import ConnectorSettingsBase

from bi_api_commons.base_models import TenantDef, TenantYCFolder

from bi_i18n.localizer_base import LocalizerLoader, TranslationConfig

from bi_api_connector.form_config.models.base import ConnectionFormMode, ConnectionFormFactory, ConnectionForm


class ConnectionFormTestBase:
    CONN_FORM_FACTORY_CLS: ClassVar[Type[ConnectionFormFactory]]
    TRANSLATION_CONFIGS: ClassVar[list[TranslationConfig]]

    @pytest.fixture
    def connectors_settings(self) -> Optional[ConnectorSettingsBase]:
        """ Parametrize if a form has extra settings """

        return None

    @pytest.fixture
    def tenant(self) -> TenantDef:
        """ Parametrize if a form depends on tenant type """

        return TenantYCFolder(folder_id='some_folder_id')

    @final
    @pytest.fixture(
        params=[mode.name for mode in ConnectionFormMode],
    )
    def mode(self, request) -> ConnectionFormMode:  # type: ignore
        return ConnectionFormMode(request.param)

    @pytest.fixture
    def form_config(
            self,
            connectors_settings: Optional[ConnectorSettingsBase],
            tenant: TenantDef,
            mode: ConnectionFormMode
    ) -> ConnectionForm:
        loader = LocalizerLoader(
            configs=self.TRANSLATION_CONFIGS,
        )
        factory = loader.load()
        localizer = factory.get_for_locale('ru')
        form_factory = self.CONN_FORM_FACTORY_CLS(mode=mode, localizer=localizer)
        form_config = form_factory.get_form_config(connectors_settings, tenant)
        return form_config

    def test_validate_conditional_fields(self, form_config: ConnectionForm) -> None:
        form_config.validate_conditional_fields()

    def test_validate_api_schema_fields(self, form_config: ConnectionForm) -> None:
        form_config.validate_api_schema_fields()

    def test_serialize(self, form_config: ConnectionForm) -> None:
        serializable = form_config.as_dict()
        json.dumps(serializable)