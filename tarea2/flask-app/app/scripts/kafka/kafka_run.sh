#!/bin/bash

# Se importa la variable KAFKA_HOME
source kafka_home.sh

# Despues de ejecuta kafka con el archivo de configuracion
$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties &