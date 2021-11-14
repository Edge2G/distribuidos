#!/bin/bash

# Se importa la variable KAFKA_HOME
source kafka_home.sh

# Primero se ejecuta zookeper con el archivo de configuracion
$KAFKA_HOME/bin/zookeeper-server-start.sh $KAFKA_HOME/config/zookeeper.properties