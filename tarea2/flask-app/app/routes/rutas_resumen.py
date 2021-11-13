from kafka import KafkaProducer
from scripts.email.sender import send_mail
from flask import Blueprint, request, json, url_for

def redirect_url(default='index'): # Redireccionamiento desde donde vino la request
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

mod = Blueprint('rutas_resumen', __name__)

@mod.route("/resumen_d/", methods=['GET', 'POST'])
def resumen_diario():
    #Generar json del resumen
    #Hacer un send del json
    pass

@mod.route("/resumen_d/enviar_mail", methods=['GET','POST'])
def enviar_mail():
    consumer = KafkaConsumer('ConsumerD', bootstrap_servers=['localhost:9092'], value_deserializer=lambda m: json.loads(m.decode('ascii')))
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))
    pass
