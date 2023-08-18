# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.priv.iam.v1 import oauth_scope_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__pb2
from yandex.cloud.priv.iam.v1 import oauth_scope_service_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2
from yandex.cloud.priv.operation import operation_pb2 as yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2


class OAuthScopeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.OAuthScopeService/Get',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.GetOAuthScopeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__pb2.OAuthScope.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.OAuthScopeService/List',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.ListOAuthScopesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.ListOAuthScopesResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.OAuthScopeService/Create',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.CreateOAuthScopeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.OAuthScopeService/Update',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.UpdateOAuthScopeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.OAuthScopeService/Delete',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.DeleteOAuthScopeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )


class OAuthScopeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OAuthScopeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.GetOAuthScopeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__pb2.OAuthScope.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.ListOAuthScopesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.ListOAuthScopesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.CreateOAuthScopeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.UpdateOAuthScopeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.DeleteOAuthScopeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.iam.v1.OAuthScopeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OAuthScopeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.OAuthScopeService/Get',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.GetOAuthScopeRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__pb2.OAuthScope.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.OAuthScopeService/List',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.ListOAuthScopesRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.ListOAuthScopesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.OAuthScopeService/Create',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.CreateOAuthScopeRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.OAuthScopeService/Update',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.UpdateOAuthScopeRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.OAuthScopeService/Delete',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_oauth__scope__service__pb2.DeleteOAuthScopeRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
