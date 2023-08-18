from cryptography import fernet

from bi_api_commons.base_models import RequestContextInfo
from bi_core.united_storage_client import USAuthContextMaster
from bi_core.services_registry.top_level import ServicesRegistry, DummyServiceRegistry
from bi_core.us_manager.us_manager import USManagerBase
from bi_configs.crypto_keys import CryptoKeysConfig


class DummyUSManager(USManagerBase):
    def __init__(
            self,
            bi_context: RequestContextInfo = RequestContextInfo.create_empty(),
            services_registry: ServicesRegistry = DummyServiceRegistry(rci=RequestContextInfo.create_empty()),
    ):
        super().__init__(
            bi_context=bi_context,
            us_base_url="http://localhost:66000",
            us_api_prefix="dummy",
            crypto_keys_config=CryptoKeysConfig(  # type: ignore  # TODO: fix
                map_id_key={"dummy_usm_key": fernet.Fernet.generate_key().decode('ascii')},
                actual_key_id="dummy_usm_key",
            ),
            us_auth_context=USAuthContextMaster("FakeKey"),
            services_registry=services_registry,
        )
