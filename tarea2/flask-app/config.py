import os
from kafka import KafkaConsumer, KafkaProducer

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

TOPIC_NAME = 'items'
KAFKA_SERVER = 'localhost:9092'

# ----------------------- Consumer ---------------------------------------------------------- #
consumer = KafkaConsumer(TOPIC_NAME)

for message in consumer:
    print(message)
# ----------------------- Producer ---------------------------------------------------------- #
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b'HOLAAAAAA')
producer.flush()