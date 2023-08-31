from __future__ import annotations

import asyncio
import uuid

from bi_constants.enums import FileProcessingStatus
from bi_connector_clickhouse.db_testing.engine_wrapper import ClickhouseDbEngineConfig

from bi_core.us_manager.us_manager_sync import SyncUSManager
from bi_core_testing.database import DbTable
from bi_core.mdb_utils import MDBDomainManagerFactory

from bi_connector_bundle_chs3.file.core.constants import CONNECTION_TYPE_FILE


def make_saved_file_connection(  # type: ignore  # TODO: fix
    sync_usm: SyncUSManager,
    clickhouse_table: DbTable,
    filename: str,
    **kwargs
):
    from bi_connector_bundle_chs3.file.core.us_connection import FileS3Connection
    from bi_core.connection_executors import SyncWrapperForAsyncConnExecutor
    from bi_core.connectors.clickhouse_base.connection_executors import ClickHouseSyncAdapterConnExecutor
    from bi_core.connection_executors import ExecutionMode
    from bi_core.connection_models import TableIdent
    from bi_core.connectors.clickhouse_base.conn_options import CHConnectOptions
    from bi_core.connectors.clickhouse_base.dto import ClickHouseConnDTO
    from bi_core.connections_security.base import InsecureConnectionSecurityManager

    conn_name = 'file conn %s' % uuid.uuid4()
    engine_config = clickhouse_table.db.engine_config
    assert isinstance(engine_config, ClickhouseDbEngineConfig)
    cluster = engine_config.cluster
    assert cluster is not None
    with SyncWrapperForAsyncConnExecutor(
        async_conn_executor=ClickHouseSyncAdapterConnExecutor(  # type: ignore  # TODO: fix
            conn_dto=ClickHouseConnDTO(
                conn_id=None,
                protocol='http',
                endpoint=None,
                cluster_name=cluster,
                multihosts=clickhouse_table.db.get_conn_hosts(),  # type: ignore  # TODO: fix
                **clickhouse_table.db.get_conn_credentials(full=True),
            ),
            conn_options=CHConnectOptions(max_execution_time=None, connect_timeout=None, total_timeout=None),
            req_ctx_info=None,
            exec_mode=ExecutionMode.DIRECT,
            sec_mgr=InsecureConnectionSecurityManager(),
            mdb_mgr=MDBDomainManagerFactory().get_manager(),
            remote_qe_data=None,
            tpe=None,
            conn_hosts_pool=clickhouse_table.db.get_conn_hosts(),
            host_fail_callback=lambda h: None,
        ),
        loop=asyncio.get_event_loop(),
    ) as ce:
        raw_schema = ce.get_table_schema_info(TableIdent(
            db_name=clickhouse_table.db.name, schema_name=None, table_name=clickhouse_table.name,
        )).schema
    data_dict = FileS3Connection.DataModel(
        sources=[
            FileS3Connection.FileDataSource(
                id=str(uuid.uuid4()),
                file_id=str(uuid.uuid4()),
                title=f'Title -- {filename.upper()}',
                s3_filename=filename,
                raw_schema=raw_schema,
                status=FileProcessingStatus.ready,
            ),
        ],
    )
    conn = FileS3Connection.create_from_dict(
        data_dict,
        ds_key=conn_name,
        type_=CONNECTION_TYPE_FILE.name,
        us_manager=sync_usm,
        **kwargs)
    sync_usm.save(conn)
    return conn