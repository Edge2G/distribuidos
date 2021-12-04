#!/bin/bash

source kafka_home.sh

$KAFKA_HOME/bin/kafka-topics.sh --create \
--topic ResumenD -zookeeper localhost:2181 \
--replication-factor 1 \
--partitions 1