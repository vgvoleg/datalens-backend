from pytest import Config
from statcommons.logs import LOGMUTATORS

from bi_core.loader import (
    CoreLibraryConfig,
    load_bi_core,
)
from bi_core.logging_config import add_log_context_scoped
from bi_core_testing.configuration import CoreTestEnvironmentConfigurationBase
from bi_core_testing.environment import prepare_united_storage_from_config
from bi_db_testing.loader import load_bi_db_testing


def initialize_core_test(pytest_config: Config, core_test_config: CoreTestEnvironmentConfigurationBase) -> None:
    # Configure pytest itself
    pytest_config.addinivalue_line("markers", "slow: ...")
    pytest_config.addinivalue_line("markers", "yt: ...")

    # Add Log context to logging records (not only in format phase)
    LOGMUTATORS.apply(require=False)
    # TODO FIX: Replace with add_log_context after all tests will be refactored to use unscoped log context
    LOGMUTATORS.add_mutator("log_context_scoped", add_log_context_scoped)

    # Prepare US
    prepare_united_storage_from_config(core_test_config.get_us_config())

    # Initialize this and other libraries
    load_bi_db_testing()
    load_bi_core(CoreLibraryConfig(core_connector_ep_names=core_test_config.core_connector_whitelist))
