from kafka import KafkaProducer
from kafka import KafkaConsumer

from flask import Blueprint, request, json, url_for
from config import KAFKA_SERVER



mod = Blueprint('rutas_resumen', __name__)

@mod.route("/resumen_d/", methods=['GET', 'POST'])
def resumen_diario():

    #Generar json del resumen
    #Hacer un send del json
    pass



@mod.route("/resumen_d/enviar_mail", methods=['GET','POST'])
def enviar_mail():
    consumer = KafkaConsumer('ResumenD', bootstrap_servers=[KAFKA_SERVER], value_deserializer=lambda m: json.loads(m.decode('ascii')))
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))
    pass
