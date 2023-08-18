from typing import Type

from bi_core.connection_executors.adapters.common_base import CommonBaseDirectAdapter
from bi_core.connection_executors.models.connection_target_dto_base import BaseSQLConnTargetDTO

from bi_connector_postgresql.core.postgresql_base.adapters_postgres import PostgresAdapter
from bi_connector_postgresql.core.postgresql_base.target_dto import PostgresConnTargetDTO

from bi_core_testing.executors import ExecutorFactoryBase


class PostgresExecutorFactory(ExecutorFactoryBase):
    def get_dto_class(self) -> Type[BaseSQLConnTargetDTO]:
        return PostgresConnTargetDTO

    def get_dba_class(self) -> Type[CommonBaseDirectAdapter]:
        return PostgresAdapter
