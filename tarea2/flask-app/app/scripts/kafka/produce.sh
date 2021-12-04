#!/bin/bash

source kafka_home.sh

$KAFKA_HOME/bin/kafka-console-producer.sh --broker-list localhost:9092,localhost:9093,localhost:9094 --topic Ordenes