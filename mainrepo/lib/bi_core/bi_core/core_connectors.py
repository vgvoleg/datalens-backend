from typing import Collection, Optional, Type

from bi_core.connectors.registry import get_all_connectors
from bi_core.connectors.base.registrator import CONN_REG_CORE
from bi_core.connectors.base.connector import CoreConnector


def _register_connector(connector_cls: Type[CoreConnector]) -> None:
    CONN_REG_CORE.register_connector(connector_cls)


def register_all_connectors(connector_ep_names: Optional[Collection[str]] = None) -> None:
    for ep_name, connector_cls in sorted(get_all_connectors().items()):
        if connector_ep_names is not None and ep_name not in connector_ep_names:
            continue
        _register_connector(connector_cls)