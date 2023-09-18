import logging
import os

from aiohttp import web

from dl_configs.settings_loaders.fallback_cfg_resolver import YEnvFallbackConfigResolver
from dl_core.logging_config import configure_logging
from dl_configs.settings_loaders.loader_env import load_settings_from_env_with_fallback_legacy
from bi_defaults.environments import InstallationsMap, EnvAliasesMap
from bi_file_uploader_worker.app_health_check_lib import FileUploaderWorkerHealthCheckAppFactory

from dl_file_uploader_worker_lib.settings import FileUploaderWorkerSettings


LOGGER = logging.getLogger(__name__)


async def create_gunicorn_app() -> web.Application:
    fallback_resolver = YEnvFallbackConfigResolver(
        installation_map=InstallationsMap,
        env_map=EnvAliasesMap,
    )
    settings = load_settings_from_env_with_fallback_legacy(
        FileUploaderWorkerSettings,
        fallback_cfg_resolver=fallback_resolver,
    )
    configure_logging(app_name='bi_file_uploader_worker_health_check', sentry_dsn=settings.SENTRY_DSN)
    try:
        LOGGER.info("Creating application instance...")
        app_factory = FileUploaderWorkerHealthCheckAppFactory()
        app = app_factory.create_app()
        LOGGER.info("Application instance was created")
        return app
    except Exception:
        LOGGER.exception("Exception during app creation")
        raise


def main() -> None:
    current_app = create_gunicorn_app()
    web.run_app(
        current_app,
        host=os.environ["APP_HOST"],
        port=int(os.environ["APP_PORT"]),
    )


if __name__ == '__main__':
    main()
