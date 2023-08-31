import os

import pytest

from bi_core_testing.initialization import initialize_core_test

from bi_testing.env_params.generic import GenericEnvParamGetter
from bi_testing.files import get_file_loader

from bi_formula.loader import load_bi_formula
from bi_formula.testing.forced_literal import forced_literal_use

from bi_connector_snowflake.core.testing.secrets import SnowFlakeSecretReader

from bi_connector_snowflake_tests.ext.config import CORE_TEST_CONFIG


pytest_plugins = (
    'aiohttp.pytest_plugin',  # and it, in turn, includes 'pytest_asyncio.plugin'
)


def pytest_configure(config):  # noqa
    initialize_core_test(pytest_config=config, core_test_config=CORE_TEST_CONFIG)
    load_bi_formula()


@pytest.fixture(scope='session')
def env_param_getter() -> GenericEnvParamGetter:
    filepath = os.path.join(os.path.dirname(__file__), 'params.yml')
    filepath = get_file_loader().resolve_path(filepath)
    return GenericEnvParamGetter.from_yaml_file(filepath)


@pytest.fixture(scope='session')
def sf_secrets(env_param_getter):
    return SnowFlakeSecretReader(env_param_getter)


__all__ = (
    # auto-use fixtures:
    'forced_literal_use',
)