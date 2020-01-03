#!/bin/bash

python -m grpc_tools.protoc -I . --python_out=grpc_route --grpc_python_out=grpc_route  proto/route.proto