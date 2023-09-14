import abc
from typing import TYPE_CHECKING

import attr

from bi_core.rls import BaseSubjectResolver
from bi_core.utils import FutureRef

if TYPE_CHECKING:
    from bi_core.services_registry.top_level import ServicesRegistry  # noqa


@attr.s
class InstallationSpecificServiceRegistry(metaclass=abc.ABCMeta):
    _service_registry_ref: FutureRef["ServicesRegistry"] = attr.ib()

    @property
    def service_registry(self) -> "ServicesRegistry":
        return self._service_registry_ref.ref

    @abc.abstractmethod
    async def get_subject_resolver(self) -> BaseSubjectResolver:
        raise NotImplementedError()


class InstallationSpecificServiceRegistryFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_inst_specific_sr(self, sr_ref: FutureRef["ServicesRegistry"]) -> InstallationSpecificServiceRegistry:
        raise NotImplementedError()
