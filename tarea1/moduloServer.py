import grpc
from concurrent import futures
import time
import protoBusqueda_pb2_grpc as pb2_grpc
import protoBusqueda_pb2 as pb2
import json
import re 



class servicioBusqueda(pb2_grpc.ServicioBusquedaServicer):

    def __init__(self, *args, **kwargs):
        pass

    def ObtenerRespuesta(self, request, context):
        string_de_busqueda = request.nombre
        result = f'Servidor buscando el item: "{string_de_busqueda}"'

        Listresult=[]
        
        nombre=string_de_busqueda

        with open('inventario.json') as file:
            data = json.load(file)

            for producto in data['productos']:

                if re.search(nombre, producto['nombre']):
                    result = {'id': producto['id'], 'nombre': producto['nombre'] , 'marca': producto['marca'], 'precio':producto['precio'] }
                    Listresult.append(result)

        search_res = {'item': Listresult}
        print(type(search_res))

        return pb2.ListaResultante(**search_res)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ServicioBusquedaServicer_to_server(servicioBusqueda(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()