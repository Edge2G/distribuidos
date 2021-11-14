from app import app
from kafka import KafkaConsumer
from config import KAFKA_SERVER, TOPIC_NAME_ORDENES, TOPIC_NAME_RESUMEN
from flask import json
import threading

SALES = []
SUMMARIES = []

def run_app():
    app.run(threaded = True, debug=True, use_reloader=False)

def habilitar_consumidor():

    consumer = KafkaConsumer(TOPIC_NAME_ORDENES, bootstrap_servers=[KAFKA_SERVER], value_deserializer=lambda m: json.loads(m.decode('ascii')))
    for message in consumer:
        SALES.append(message.value)
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))
        
def habilitar_consumidor2():

    consumer2 = KafkaConsumer(TOPIC_NAME_RESUMEN, bootstrap_servers=[KAFKA_SERVER], value_deserializer=lambda m: json.loads(m.decode('ascii')))
    for message in consumer2:
        print(message.value)
        SUMMARIES.append(message.value)

if __name__ == "__main__":
    try:
        t1 = threading.Thread(target=run_app).start()
        t2 = threading.Thread(target=habilitar_consumidor).start()
        t3 = threading.Thread(target=habilitar_consumidor2).start()
    except Exception as e:
        pass
    