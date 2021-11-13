from kafka import KafkaProducer
from flask import Blueprint, request, url_form, json, url_for

def redirect_url(default='index'): # Redireccionamiento desde donde vino la request
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

mod = Blueprint('rutas_ordenes', __name__)

@mod.route("/newOrder/<string:id>", methods=['GET', 'POST'])
def newOrder(id):

    

    producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'), bootstrap_servers=['localhost:9092'])
    return "<p>Hello, World!</p>"
