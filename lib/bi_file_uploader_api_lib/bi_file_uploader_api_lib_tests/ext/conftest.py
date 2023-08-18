import os

import pytest

from bi_configs.enums import AppType
from bi_configs.settings_submodels import S3Settings, GoogleAppSettings

from bi_testing.env_params.generic import GenericEnvParamGetter
from bi_testing.files import get_file_loader
from bi_testing.tvm_info import TvmSecretReader

from bi_file_uploader_worker_lib.settings import FileUploaderWorkerSettings


@pytest.fixture(scope='function', autouse=True)
async def use_local_task_processor_auto(use_local_task_processor):
    yield


@pytest.fixture(scope='session')
def env_param_getter() -> GenericEnvParamGetter:
    filepath = os.path.join(os.path.dirname(__file__), 'params.yml')
    filepath = get_file_loader().resolve_path(filepath)
    return GenericEnvParamGetter.from_yaml_file(filepath)


@pytest.fixture(scope='session')
def tvm_secret_reader(env_param_getter) -> TvmSecretReader:
    return TvmSecretReader(env_param_getter)


# overriding top-level fixture to set google app settings that are only needed in ext tests
@pytest.fixture(scope='function')
def file_uploader_worker_settings(
        env_param_getter,
        redis_app_settings,
        redis_arq_settings,
        s3_settings,
        connectors_settings,
        us_config,
        crypto_keys_config,
):
    settings = FileUploaderWorkerSettings(
        APP_TYPE=AppType.TESTS,
        REDIS_APP=redis_app_settings,
        REDIS_ARQ=redis_arq_settings,
        S3=S3Settings(
            ENDPOINT_URL=s3_settings.ENDPOINT_URL,
            ACCESS_KEY_ID=s3_settings.ACCESS_KEY_ID,
            SECRET_ACCESS_KEY=s3_settings.SECRET_ACCESS_KEY,
        ),
        S3_TMP_BUCKET_NAME='bi-file-uploader-tmp',
        S3_PERSISTENT_BUCKET_NAME='bi-file-uploader',
        SENTRY_DSN=None,
        US_BASE_URL=us_config.base_url,
        US_MASTER_TOKEN=us_config.master_token,
        CONNECTORS=connectors_settings,
        GSHEETS_APP=GoogleAppSettings(
            API_KEY=env_param_getter.get_str_value('GOOGLE_API_KEY'),
            CLIENT_ID='dummy',  # TODO test auth properly
            CLIENT_SECRET='dummy',
        ),
        CRYPTO_KEYS_CONFIG=crypto_keys_config,
    )
    yield settings
