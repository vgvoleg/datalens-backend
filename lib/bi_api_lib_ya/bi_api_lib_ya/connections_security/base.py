from __future__ import annotations

import logging
from typing import ClassVar, Type

import attr

from bi_core import exc
from bi_core.connection_models import ConnDTO, DefaultSQLDTO
from bi_core.connections_security.base import GenericConnectionSecurityManager, ConnectionSafetyChecker


LOGGER = logging.getLogger(__name__)


@attr.s
class CloudConnectionSecurityManager(GenericConnectionSecurityManager):
    _samples_ch_hosts: frozenset[str] = attr.ib()

    # TODO FIX: https://st.yandex-team.ru/BI-2582
    #  Generalize code with .is_safe_connection() after checking if logic is fully compatible
    def is_internal_connection(self, conn_dto: ConnDTO) -> bool:
        # TODO FIX: Move on top after moving MDB utils in dedicated module (right now will cause import loop)
        from bi_core.mdb_utils import MDBDomainManager

        mdb_man = MDBDomainManager.from_env()

        if isinstance(conn_dto, DefaultSQLDTO):
            all_hosts = conn_dto.get_all_hosts()

            if all(mdb_man.host_in_mdb(host) for host in all_hosts):
                return True

            if all(host in self._samples_ch_hosts for host in all_hosts):
                return True

        return False


@attr.s
class InternalConnectionSecurityManager(GenericConnectionSecurityManager):
    def is_internal_connection(self, conn_dto: ConnDTO) -> bool:
        return True


@attr.s(kw_only=True)
class MDBConnectionSafetyChecker(ConnectionSafetyChecker):
    """ MDB hosts """

    _DTO_TYPES: ClassVar[set[Type[ConnDTO]]] = set()

    def is_safe_connection(self, conn_dto: ConnDTO) -> bool:
        if isinstance(conn_dto, DefaultSQLDTO) and type(conn_dto) in self._DTO_TYPES:
            # TODO FIX: Move on top after moving MDB utils in dedicated module (right now will cause import loop)
            from bi_core.mdb_utils import MDBDomainManager

            mdb_man = MDBDomainManager.from_env()

            hosts = conn_dto.get_all_hosts()
            LOGGER.info('Checking if hosts %r belong to mdb', hosts)
            if all(mdb_man.host_in_mdb(host) for host in hosts):
                LOGGER.info('All hosts (%r) look like mdb hosts', hosts)
                return True
            else:
                LOGGER.info('Hosts (%r) do not belong to mdb (%r)', hosts, mdb_man.settings.mdb_domains)

            if len(set(mdb_man.host_in_mdb(host) for host in hosts)) > 1:
                raise exc.ConnectionConfigurationError(
                    'Internal (MDB) hosts and external hosts can not be mixed in multihost configuration')

        return False