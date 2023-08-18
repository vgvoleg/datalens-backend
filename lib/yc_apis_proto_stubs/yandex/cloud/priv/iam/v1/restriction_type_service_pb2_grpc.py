# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.priv.access import access_pb2 as yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2
from yandex.cloud.priv.iam.v1 import restriction_type_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__pb2
from yandex.cloud.priv.iam.v1 import restriction_type_service_pb2 as yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2
from yandex.cloud.priv.operation import operation_pb2 as yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2


class RestrictionTypeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RestrictionTypeService/Get',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.GetRestrictionTypeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__pb2.RestrictionType.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RestrictionTypeService/List',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypesRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypesResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RestrictionTypeService/Create',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.CreateRestrictionTypeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RestrictionTypeService/Update',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.UpdateRestrictionTypeRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListAccessBindings = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RestrictionTypeService/ListAccessBindings',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypeAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
                )
        self.SetAccessBindings = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RestrictionTypeService/SetAccessBindings',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.SetRestrictionTypeAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.UpdateAccessBindings = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RestrictionTypeService/UpdateAccessBindings',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.UpdateRestrictionTypeAccessBindingsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.ListOperations = channel.unary_unary(
                '/yandex.cloud.priv.iam.v1.RestrictionTypeService/ListOperations',
                request_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypeOperationsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypeOperationsResponse.FromString,
                )


class RestrictionTypeServiceServicer(object):
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

    def ListAccessBindings(self, request, context):
        """access

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateAccessBindings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOperations(self, request, context):
        """operations

        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RestrictionTypeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.GetRestrictionTypeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__pb2.RestrictionType.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypesRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypesResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.CreateRestrictionTypeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.UpdateRestrictionTypeRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypeAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.ListAccessBindingsResponse.SerializeToString,
            ),
            'SetAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.SetRestrictionTypeAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'UpdateAccessBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateAccessBindings,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.UpdateRestrictionTypeAccessBindingsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'ListOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypeOperationsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypeOperationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.priv.iam.v1.RestrictionTypeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RestrictionTypeService(object):
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RestrictionTypeService/Get',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.GetRestrictionTypeRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__pb2.RestrictionType.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RestrictionTypeService/List',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypesRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypesResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RestrictionTypeService/Create',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.CreateRestrictionTypeRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RestrictionTypeService/Update',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.UpdateRestrictionTypeRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RestrictionTypeService/ListAccessBindings',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypeAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_access_dot_access__pb2.ListAccessBindingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RestrictionTypeService/SetAccessBindings',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.SetRestrictionTypeAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateAccessBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RestrictionTypeService/UpdateAccessBindings',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.UpdateRestrictionTypeAccessBindingsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.priv.iam.v1.RestrictionTypeService/ListOperations',
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypeOperationsRequest.SerializeToString,
            yandex_dot_cloud_dot_priv_dot_iam_dot_v1_dot_restriction__type__service__pb2.ListRestrictionTypeOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
