from kafka import KafkaProducer
from flask import Blueprint, request, json, url_for, redirect
from config import KAFKA_SERVER, TOPIC_NAME_ORDENES

def redirect_url(default='index'): # Redireccionamiento desde donde vino la request
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

mod = Blueprint('rutas_ordenes', __name__)

@mod.route("/new_order", methods=['GET', 'POST'])
def newOrder():

    id = input('Ingrese id:')
    mail1 = input('Ingrese mail del vendedor:')
    mail2 = input('Ingrese mail del cocinero:')
    sopaipillas = input('Ingrese la cantidad de sopaipillas vendidas:')

    producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'), bootstrap_servers=[KAFKA_SERVER])
    producer.send(TOPIC_NAME_ORDENES, {'order_id': id, 'email_vendedor': mail1, 'email_cocinero': mail2, 'numero_sopaipillas': sopaipillas})
    producer.flush()
    return redirect("/")
