from __future__ import print_function
import logging
import grpc
import numpy as np
import pandas as pd
import json
from google.protobuf.struct_pb2 import Struct
import test_pb2
import test_pb2_grpc


_LOGGER = logging.getLogger(__name__)


def run(stub):

    df = pd.DataFrame(
        {
            'A': 1.,
            'B': pd.Timestamp('20130102'),
            'C': pd.Series(1, index=list(range(4)), dtype='float32'),
            'D': np.array([3] * 4, dtype='int32'),
            'E': pd.Categorical(["test", "train", "test", "train"]),
            'F': 'foo'
        }
    )

    result = df.to_json()

    parsed = json.loads(result)

    s = Struct()

    s.update(parsed)

    request = test_pb2.Request()

    request.event = "app"
    request.payload.Pack(s)
    
    try:
        response = stub.UnaryCall(request)
        print(response)
    except grpc.RpcError as rpc_error:
        print(rpc_error)


def main():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = test_pb2_grpc.TestServiceStub(channel)
        run(stub)


if __name__ == '__main__':
    logging.basicConfig()
    main()
