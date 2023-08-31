from __future__ import annotations

import logging

from bi_app_tools import ylog
from bi_core.maintenance.logging_config import configure_logging_for_shell
from bi_core.maintenance.us_crawler_base import USEntryCrawler
from bi_core.us_manager.us_manager_async import AsyncUSManager

from bi_api_lib.maintenance.common import MaintenanceEnvironmentManager


LOGGER = logging.getLogger(__name__)


async def run_crawler(crawler: USEntryCrawler, usm: AsyncUSManager = None, configure_logging: bool = True, use_sr_factory: bool = False) -> None:
    """Runner to run crawler in interactive shell"""
    red = "\x1b[31m"
    nc = "\x1b[0m"

    if configure_logging:
        configure_logging_for_shell()
    try:
        if usm is None:
            usm = MaintenanceEnvironmentManager().get_async_usm_from_env(use_sr_factory=use_sr_factory)
        crawler.set_usm(usm)
        req_id = "__".join(
            req_id
            for req_id in (
                ylog.context.get_log_context().get('request_id'),
                f"cr.{crawler.run_id}",
            )
            if req_id is not None
        )
        with ylog.context.log_context(request_id=req_id):
            await crawler.run()
    finally:
        if configure_logging:
            print('\n'.join((
                red,
                '!!! LOGGING WAS CONFIGURED TO SEND LOGS TO CENTRAL STORAGE !!!',
                '!!! NOTICE THAT ALL FURTHER LOGS WILL BE SENT TO CENTRAL STORAGE !!!',
                nc,
            )))