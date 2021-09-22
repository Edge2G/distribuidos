#! /bin/bash
python3 -m grpc_tools.protoc --proto_path=. ./protoBusqueda.proto --python_out=. --grpc_python_out=.