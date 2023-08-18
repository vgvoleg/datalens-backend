from __future__ import annotations

import uuid
from typing import Optional, TypeVar, TYPE_CHECKING, Union

import attr
from bi_cloud_integration.yc_client_base import DLYCServiceConfig

import bi_cloud_integration
import grpc
from bi_cloud_integration.yc_as_client import DLASClient

from bi_cloud_integration.iam_rm_client import IAMRMClient
from bi_testing.cloud_tokens import CloudCredentialsConverter
from bi_testing.factories import FolderServiceFactory

if TYPE_CHECKING:
    from bi_configs.environments import CommonExternalInstallation, DataCloudExposedInstallation, \
        CommonInternalInstallation, IntegrationTestConfig


_EXT_SYS_HELPER_TV = TypeVar('_EXT_SYS_HELPER_TV', bound='ExternalSystemsHelperBase')


@attr.s
class ExternalSystemsHelperBase:
    _root_certs_file_content: bytes = attr.ib()
    _caches_dir: Optional[str] = attr.ib()

    def __enter__(self: _EXT_SYS_HELPER_TV) -> _EXT_SYS_HELPER_TV:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass


@attr.s
class ExternalSystemsHelperInternalInstallation(ExternalSystemsHelperBase):
    _ext_sys_requisites: CommonInternalInstallation = attr.ib()

    @property
    def ext_sys_requisites(self) -> CommonInternalInstallation:
        return self._ext_sys_requisites


@attr.s
class ExternalSystemsHelperCloud(ExternalSystemsHelperBase):
    _ext_sys_requisites: Union[CommonExternalInstallation,
                               DataCloudExposedInstallation, IntegrationTestConfig] = attr.ib()

    _yc_access_service_channel: Optional[grpc.Channel] = attr.ib(init=False, default=None)
    yc_credentials_converter: CloudCredentialsConverter = attr.ib(init=False, default=None)
    _yc_folder_service_factory: FolderServiceFactory = attr.ib(init=False, default=None)

    def __attrs_post_init__(self):
        self.yc_credentials_converter = CloudCredentialsConverter(
            as_grpc_channel=self.yc_access_service_channel,
            yc_ts_endpoint=self._ext_sys_requisites.YC_TS_ENDPOINT,
            caches_dir=self._caches_dir,
        )
        self._yc_folder_service_factory = FolderServiceFactory(
            self._ext_sys_requisites.YC_API_ENDPOINT_RM,
        )

    @property
    def ext_sys_requisites(self) -> Union[CommonExternalInstallation, DataCloudExposedInstallation]:
        return self._ext_sys_requisites

    @property
    def yc_folder_service_factory(self) -> FolderServiceFactory:
        assert self._yc_folder_service_factory is not None
        return self._yc_folder_service_factory

    @property
    def yc_access_service_channel(self) -> grpc.Channel:
        if self._yc_access_service_channel is None:
            credentials = grpc.ssl_channel_credentials(root_certificates=self._root_certs_file_content)
            self._yc_access_service_channel = grpc.secure_channel(
                self._ext_sys_requisites.YC_AS_ENDPOINT,
                credentials,
            )

        return self._yc_access_service_channel

    @property
    def yc_access_service_client(self) -> DLASClient:
        return bi_cloud_integration.yc_as_client.DLASClient(
            service_config=DLYCServiceConfig(
                endpoint=self.ext_sys_requisites.YC_AS_ENDPOINT
            )
        )

    def get_iam_rm_client(self, iam_token: str, req_id: Optional[str] = None):
        return IAMRMClient(
            iam_endpoint=self._ext_sys_requisites.YC_API_ENDPOINT_IAM,
            rm_endpoint=self._ext_sys_requisites.YC_API_ENDPOINT_RM,
            iam_token=iam_token,
            request_id=req_id or str(uuid.uuid4())
        )

    def __enter__(self) -> ExternalSystemsHelperCloud:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._yc_folder_service_factory.close_all()
