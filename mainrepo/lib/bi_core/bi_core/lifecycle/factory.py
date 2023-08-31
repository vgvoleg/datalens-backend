from __future__ import annotations

from functools import singledispatchmethod
from typing import TYPE_CHECKING

from bi_core.lifecycle.dataset import DatasetLifecycleManager
from bi_core.us_dataset import Dataset
from bi_core.us_connection_base import ConnectionBase
from bi_core.us_connection import get_lifecycle_manager_cls
from bi_core.lifecycle.base import EntryLifecycleManager
from bi_core.lifecycle.factory_base import EntryLifecycleManagerFactoryBase
from bi_core.connectors.base.lifecycle import ConnectionLifecycleManager

if TYPE_CHECKING:
    from bi_core.services_registry import ServicesRegistry
    from bi_core.us_entry import USEntry
    from bi_core.us_manager.us_manager import USManagerBase


class DummyEntryLifecycleManagerFactory(EntryLifecycleManagerFactoryBase):
    def get_lifecycle_manager(
            self, entry: USEntry, us_manager: USManagerBase, service_registry: ServicesRegistry,
    ) -> EntryLifecycleManager:
        return EntryLifecycleManager(us_manager=us_manager, entry=entry, service_registry=service_registry)


class DefaultEntryLifecycleManagerFactory(EntryLifecycleManagerFactoryBase):
    def get_lifecycle_manager(
            self, entry: USEntry, us_manager: USManagerBase, service_registry: ServicesRegistry,
    ) -> EntryLifecycleManager:
        return self._get_lifecycle_manager(entry, us_manager=us_manager, service_registry=service_registry)

    @singledispatchmethod
    def _get_lifecycle_manager(
            self, entry: USEntry, us_manager: USManagerBase, service_registry: ServicesRegistry,
    ) -> EntryLifecycleManager:
        return EntryLifecycleManager(us_manager=us_manager, entry=entry, service_registry=service_registry)

    @_get_lifecycle_manager.register(Dataset)
    def _get_dataset_lifecycle_manager(
            self, entry: Dataset, us_manager: USManagerBase, service_registry: ServicesRegistry,
    ) -> DatasetLifecycleManager:
        return DatasetLifecycleManager(us_manager=us_manager, entry=entry, service_registry=service_registry)

    @_get_lifecycle_manager.register(ConnectionBase)
    def _get_connection_lifecycle_manager(
            self, entry: ConnectionBase, us_manager: USManagerBase, service_registry: ServicesRegistry,
    ) -> ConnectionLifecycleManager:
        lifecycle_manager_cls = get_lifecycle_manager_cls(conn_type=entry.conn_type)
        return lifecycle_manager_cls(us_manager=us_manager, entry=entry, service_registry=service_registry)