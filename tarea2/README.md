## Tarea 2: Apache Kafka
---

### 1 - Instalacion y configuracion de Kafka y Python<br><br>

En una shell (de Ubuntu por ejemplo), ejecutar el siguiente comando para descargar los binarios (en este caso se descarga en la carpeta home)

```sh
wget https://dlcdn.apache.org/kafka/3.0.0/kafka_2.13-3.0.0.tgz
```

Y extraer los contenidos del .tgz con ```tar -xzf```

Si no funciona la descarga, de puede conseguir en el [Sitio oficial](https://kafka.apache.org/downloads)


Luego se clona el repositorio
```sh
git clone https://github.com/Edge2G/distribuidos.git
```

Y en la carpeta de tarea 2, se encuentra otro directorio llamado  **kafka_scripts** en donde primero se debe ejecutar el servicio de zookeeper, y luego el server de kafka (en consolas separadas)

```sh
./zookeeper_run.sh
```

```sh
./kafka_run.sh
```

ademas es necesario crear 2 topics que tienen la siguiente configuracion:

Ordenes 
```sh
--create \
--topic Ordenes -zookeeper localhost:2181 \
--replication-factor 1 \
--partitions 1
```
ResumenD

--create \
--topic ResumenD -zookeeper localhost:2181 \
--replication-factor 1 \
--partitions 1
```

Por otro lado, como se utiliza python3, es necesario instalar la libreria de kafka para python:

```sh
pip install kafka-python
```
