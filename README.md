# Github Sistemas Distribuidos
Lorenzo Alfaro, Milenko Espinoza, Cristián Maira

## Tarea 1: Cache y RPC

### Instalacion de dependencias
En un entorno virtual de python3, ejecutar el siguiente comando:

```sh
pip3 install redis grpcio grpcio-tools Flask
```

Y clonar el repositorio
```sh
git clone https://github.com/Edge2G/distribuidos.git
```

Por otra parte, se debe instalar la consola de comandos de redis (esto es para una distribucion basada en ubuntu):

```sh
sudo apt install redis-server
```

Luego, configurar redis para que corra con systemd (initsystem). Hay que editar el archivo **redis.conf** y cambiar la linea que dice **supervised no** por **supervised systemd**

```sh
sudo vim /etc/redis/redis.conf
```

Y reiniciar la configuracion

```sh
sudo systemctl restart redis.service
```

Con esto podemos usar **redis-cli** y configurarlo para que utilice una politica de remocion y limitar la ram:

```sh
redis-cli
```

```sh
config set maxmemory-policy volatile-lru
```

```sh
config set maxmemory 20M
```

###
Referencias

- Redis: [Sitio de referencia](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04)


- gRPC:
    * [Documentacion](https://grpc.io/docs/)
    * [Sitio de referencia](https://grpc.io/docs/languages/python/quickstart/)
