#!/bin/bash

python -m grpc_tools.protoc -I . --python_out=grpc_map --grpc_python_out=grpc_map  proto/route.proto