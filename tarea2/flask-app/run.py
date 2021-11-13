from app import app
from kafka import KafkaConsumer
from config import KAFKA_SERVER
from flask import Blueprint, request, json, url_for
import threading
    
def run_app():
    app.run(threaded = True, debug=True, use_reloader=False)

def habilitar_consumidor():

    consumer = KafkaConsumer('Ordenes', bootstrap_servers=[KAFKA_SERVER], value_deserializer=lambda m: json.loads(m.decode('ascii')))
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))

if __name__ == "__main__":
    try:
        t1 = threading.Thread(target=run_app).start()
        t2 = threading.Thread(target=habilitar_consumidor).start()
    except Exception as e:
        pass
    