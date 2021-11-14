from kafka import KafkaProducer
from flask import Blueprint, json, request, url_for
from app import redirect_url
from config import KAFKA_SERVER, TOPIC_NAME_RESUMEN
from app.scripts.email.sender import enviar_mail

from run import SALES

mod = Blueprint('rutas_resumen', __name__)


def redirect_url(default='index'): # Redireccionamiento desde donde vino la request
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)


@mod.route("/resumen_d/", methods=['GET', 'POST'])
def resumen_diario():
    producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'), bootstrap_servers=[KAFKA_SERVER])
    print(SALES)
    ventas = json.loads(SALES)
    print(ventas)
    return redirect_url()
    cocineros = {}
    for venta in ventas:
        if cocineros.fromkeys(venta["email_cocinero"]) is None:
            cocineros[venta["email_cocinero"]] = 1
        else:
            cocineros[venta["email_cocinero"]] +=1

    for index, data in enumerate(cocineros):
        producer.send(TOPIC_NAME_RESUMEN, {'email_cocinero': data[index][0], 'venta_diaria': data[index][1]})

    producer.flush()
    enviar_mail()