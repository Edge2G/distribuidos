import grpc
import protoBusqueda_pb2_grpc as pb2_grpc
import protoBusqueda_pb2 as pb2


class servicioCliente(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        self.stub = pb2_grpc.ServicioBusquedaStub(self.channel)

    def buscarResultados(self, nombre_producto):
        """
        Client function to call the rpc for GetServerResponse
        """
        print("Cliente buscando por: ", nombre_producto)
        nombre_pb2 = pb2.Nombre(nombre=nombre_producto)
        return self.stub.ObtenerRespuesta(nombre_pb2)


if __name__ == '__main__':
    cliente = servicioCliente()
    input_string = input("Que producto desea buscar?\n>>>")
    result = cliente.buscarResultados(nombre_producto = input_string)
    print(f'{result}')