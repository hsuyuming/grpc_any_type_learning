# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import test_pb2 as test__pb2


class TestServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UnaryCall = channel.unary_unary(
                '/TestService/UnaryCall',
                request_serializer=test__pb2.Request.SerializeToString,
                response_deserializer=test__pb2.Response.FromString,
                )


class TestServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UnaryCall(self, request, context):
        """One request followed by one response.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UnaryCall': grpc.unary_unary_rpc_method_handler(
                    servicer.UnaryCall,
                    request_deserializer=test__pb2.Request.FromString,
                    response_serializer=test__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TestService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TestService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UnaryCall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TestService/UnaryCall',
            test__pb2.Request.SerializeToString,
            test__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
