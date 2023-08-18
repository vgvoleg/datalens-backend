# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.priv.iam.v1.backoffice import access_binding_service_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_backoffice_dot_access__binding__service__pb2


class AccessBindingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListBySubject = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.backoffice.AccessBindingService/ListBySubject',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_backoffice_dot_access__binding__service__pb2.ListSubjectAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_backoffice_dot_access__binding__service__pb2.ListSubjectAccessBindingsResponse.FromString,
                )


class AccessBindingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListBySubject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccessBindingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListBySubject': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBySubject,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_backoffice_dot_access__binding__service__pb2.ListSubjectAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_backoffice_dot_access__binding__service__pb2.ListSubjectAccessBindingsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.iam.v1.backoffice.AccessBindingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AccessBindingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListBySubject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.backoffice.AccessBindingService/ListBySubject',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_backoffice_dot_access__binding__service__pb2.ListSubjectAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_backoffice_dot_access__binding__service__pb2.ListSubjectAccessBindingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
