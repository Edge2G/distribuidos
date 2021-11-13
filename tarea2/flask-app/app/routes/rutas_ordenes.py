import os
from kafka import KafkaProducer
from flask import Blueprint, request, json, url_for
from config import BASE_DIR, KAFKA_SERVER

def redirect_url(default='index'): # Redireccionamiento desde donde vino la request
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

mod = Blueprint('rutas_ordenes', __name__)

@mod.route("/new_order", methods=['GET', 'POST'])
def newOrder():

    json_url = os.path.join(BASE_DIR, "static/js", "data.json")
    data = json.load(open(json_url))
    print(data)
    producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'), bootstrap_servers=[KAFKA_SERVER])
    producer.send('Ordenes', data)
    producer.flush()

    return redirect_url()
