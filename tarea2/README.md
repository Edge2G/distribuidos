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

Y en la carpeta de *tarea2/flask-app/app/scripts/kafka*, se encuentran los scripts de kafka. Primero se debe ejecutar el servicio de zookeeper, y luego el server de kafka (en consolas separadas)

```sh
./zookeeper_run.sh
```

```sh
./kafka_run.sh
```

ademas es necesario crear 2 topics:

Ordenes 
```sh
./create_topic_Ordenes.sh
```
ResumenD
```sh
./create_topic_ResumenD.sh
```

Por otro lado, como se utiliza python3, es necesario instalar la libreria de kafka para python:

```sh
pip install kafka-python flask
```

### 2 - Ejecucion de los modulos<br><br>

Para ejecutar los modulos, se debe correr el archivo run.py que se encuentra en flask-app/

```sh
python run.py
```

Y luego ir a:

```sh
http://127.0.0.1:5000/
```

- Para crear una nueva orden, simplemente se clickea en el link de **Nueva Orden**
  - Luego, se debe ir a la consola para ingresar los datos por stdin
- Para hacer un resumen diario, se clickea en **Resumen Diario**
