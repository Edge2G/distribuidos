## Tarea 2: Apache Kafka
---

### 1 - Instalacion y configuracion de Kafka <br><br>

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

Y en la carpeta de tarea 2, se encuentra otro directorio llamado  **kafka_scripts** en donde primero se debe ejecutar el servicio de zookeeper, y luego el server de kafka

```sh
./zookeeper_run.sh
```

```sh
./kafka_run.sh
```