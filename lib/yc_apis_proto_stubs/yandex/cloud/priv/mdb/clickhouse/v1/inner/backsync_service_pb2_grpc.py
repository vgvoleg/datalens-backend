# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.priv.mdb.clickhouse.v1.inner import backsync_service_pb2 as yandex_dot_cloud_dot_priv_dot_mdb_dot_clickhouse_dot_v1_dot_inner_dot_backsync__service__pb2


class BacksyncServiceStub(object):
    """A set of internal methods for managing pillar backsync of ClickHouse clusters.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Update = channel.unary_unary(
                '/yandex.cloud.priv.mdb.clickhouse.v1.inner.BacksyncService/Update',
                request_serializer=yandex_dot_cloud_dot_priv_dot_mdb_dot_clickhouse_dot_v1_dot_inner_dot_backsync__service__pb2.BacksyncRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_mdb_dot_clickhouse_dot_v1_dot_inner_dot_backsync__service__pb2.BacksyncResponse.FromString,
                )


class BacksyncServiceServicer(object):
    """A set of internal methods for managing pillar backsync of ClickHouse clusters.
    """

    def Update(self, request, context):
        """Updates pillar of specified ClickHouse cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BacksyncServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_mdb_dot_clickhouse_dot_v1_dot_inner_dot_backsync__service__pb2.BacksyncRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_mdb_dot_clickhouse_dot_v1_dot_inner_dot_backsync__service__pb2.BacksyncResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.mdb.clickhouse.v1.inner.BacksyncService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BacksyncService(object):
    """A set of internal methods for managing pillar backsync of ClickHouse clusters.
    """

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.mdb.clickhouse.v1.inner.BacksyncService/Update',
            yandex_dot_cloud_dot_priv_dot_mdb_dot_clickhouse_dot_v1_dot_inner_dot_backsync__service__pb2.BacksyncRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_mdb_dot_clickhouse_dot_v1_dot_inner_dot_backsync__service__pb2.BacksyncResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)