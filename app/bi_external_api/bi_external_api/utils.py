import logging
from typing import Optional

import bi_external_api


def init_sentry(secret_sentry_dsn: Optional[str]) -> None:
    if secret_sentry_dsn is not None:
        import sentry_sdk
        from sentry_sdk.integrations.aiohttp import AioHttpIntegration
        from sentry_sdk.integrations.atexit import AtexitIntegration
        from sentry_sdk.integrations.excepthook import ExcepthookIntegration
        from sentry_sdk.integrations.stdlib import StdlibIntegration
        from sentry_sdk.integrations.modules import ModulesIntegration
        from sentry_sdk.integrations.argv import ArgvIntegration
        from sentry_sdk.integrations.logging import LoggingIntegration
        from sentry_sdk.integrations.threading import ThreadingIntegration

        from bi_api_commons.logging_sentry import cleanup_common_secret_data

        sentry_sdk.init(
            dsn=secret_sentry_dsn,
            default_integrations=False,
            before_send=cleanup_common_secret_data,
            integrations=[
                # # Default
                AtexitIntegration(),
                ExcepthookIntegration(),
                StdlibIntegration(),
                ModulesIntegration(),
                ArgvIntegration(),
                LoggingIntegration(event_level=logging.WARNING),
                ThreadingIntegration(),
                #  # Custom
                AioHttpIntegration(),
            ],
            release=bi_external_api.__version__,
        )
