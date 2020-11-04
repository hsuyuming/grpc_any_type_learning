from concurrent import futures
import logging
import threading

import grpc
import google.protobuf.json_format
from google.protobuf import any_pb2
from google.protobuf.struct_pb2 import Struct
import test_pb2_grpc
import test_pb2
import pandas as pd 
import json


class TestService(test_pb2_grpc.TestServiceServicer):

    def __init__(self):
        self._lock = threading.RLock()

    def UnaryCall(self, request, context):
        with self._lock:
            s = Struct()
            print(request.event)
            request.payload.Unpack(s)
            data = google.protobuf.json_format.MessageToJson(s)
            data = json.loads(data)
            print(data)
            print(pd.DataFrame.from_dict(data))
        return test_pb2.Response(status=True)


def create_server(server_address):
    server = grpc.server(futures.ThreadPoolExecutor())
    test_pb2_grpc.add_TestServiceServicer_to_server(TestService(), server)
    port = server.add_insecure_port(server_address)
    return server, port


def serve(server):
    server.start()
    server.wait_for_termination()


def main():
    server, unused_port = create_server('[::]:50051')
    serve(server)


if __name__ == '__main__':
    logging.basicConfig()
    main()