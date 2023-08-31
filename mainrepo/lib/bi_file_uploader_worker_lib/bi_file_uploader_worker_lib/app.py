import os

import attr

from bi_api_commons.tenant_resolver import TenantResolver, CommonTenantResolver
from bi_api_commons_ya_cloud.tenant_resolver import TenantResolverYC, TenantResolverDC
from bi_configs.enums import AppType
from bi_utils.aio import ContextVarExecutor
from bi_core.aio.web_app_services.gsheets import GSheetsSettings
from bi_core.aio.web_app_services.s3 import S3Service
from bi_core.loader import load_bi_core
from bi_file_uploader_task_interface.context import FileUploaderTaskContext
from bi_file_uploader_task_interface.tasks import CleanS3LifecycleRulesTask
from bi_task_processor.arq_wrapper import create_redis_pool, create_arq_redis_settings, make_cron_task, CronSchedule
from bi_task_processor.context import BaseContextFabric
from bi_task_processor.executor import ExecutorFabric
from bi_task_processor.state import TaskState, DummyStateImpl
from bi_task_processor.worker import ArqWorker, WorkerSettings

from bi_file_uploader_lib.settings_utils import init_redis_service

from bi_file_uploader_worker_lib.settings import FileUploaderWorkerSettings
from bi_file_uploader_worker_lib.tasks import REGISTRY


@attr.s
class FileUploaderContextFab(BaseContextFabric):
    _settings: FileUploaderWorkerSettings = attr.ib()

    async def make(self) -> FileUploaderTaskContext:
        load_bi_core()

        redis_service = init_redis_service(self._settings)
        s3_service = S3Service(
            access_key_id=self._settings.S3.ACCESS_KEY_ID,
            secret_access_key=self._settings.S3.SECRET_ACCESS_KEY,
            endpoint_url=self._settings.S3.ENDPOINT_URL,
            tmp_bucket_name=self._settings.S3_TMP_BUCKET_NAME,
            persistent_bucket_name=self._settings.S3_PERSISTENT_BUCKET_NAME,
        )
        await redis_service.initialize()
        await s3_service.initialize()
        redis_pool = await create_redis_pool(create_arq_redis_settings(self._settings.REDIS_ARQ))
        return FileUploaderTaskContext(
            settings=self._settings,
            s3_service=s3_service,
            redis_service=redis_service,
            tpe=ContextVarExecutor(max_workers=min(32, (os.cpu_count() or 0) * 3 + 4)),
            gsheets_settings=GSheetsSettings(
                api_key=self._settings.GSHEETS_APP.API_KEY,
                client_id=self._settings.GSHEETS_APP.CLIENT_ID,
                client_secret=self._settings.GSHEETS_APP.CLIENT_SECRET,
            ),
            redis_pool=redis_pool,
            crypto_keys_config=self._settings.CRYPTO_KEYS_CONFIG,
            secure_reader_socket=self._settings.SECURE_READER_SOCKET,
            tenant_resolver=self.get_tenant_resolver(),
        )

    # TODO FIX: Inject appropriate resolver in app for particular contour
    def get_tenant_resolver(self) -> TenantResolver:
        return {
            AppType.CLOUD: TenantResolverYC(),
            AppType.DATA_CLOUD: TenantResolverDC(),
            AppType.NEBIUS: TenantResolverYC(),
        }.get(self._settings.APP_TYPE, CommonTenantResolver())

    async def tear_down(self, inst: FileUploaderTaskContext) -> None:  # type: ignore
        await inst.s3_service.tear_down()
        await inst.redis_service.tear_down()
        inst.tpe.shutdown()


@attr.s(kw_only=True)
class FileUploaderWorkerFactory:
    _settings: FileUploaderWorkerSettings = attr.ib()

    def create_worker(self, state: TaskState = None) -> ArqWorker:
        if state is None:
            state = TaskState(DummyStateImpl())
        cron_tasks = []
        if self._settings.ENABLE_REGULAR_S3_LC_RULES_CLEANUP:
            cron_tasks.append(make_cron_task(
                CleanS3LifecycleRulesTask(),
                schedule=CronSchedule(hour={23}, minute={0}, second={0}),
            ))
        worker = ArqWorker(
            redis_settings=create_arq_redis_settings(self._settings.REDIS_ARQ),
            executor_fab=ExecutorFabric(
                registry=REGISTRY,
                state=state,
            ),
            context_fab=FileUploaderContextFab(self._settings),
            worker_settings=WorkerSettings(),
            cron_tasks=cron_tasks,
        )
        return worker