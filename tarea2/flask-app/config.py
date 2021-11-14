import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
KAFKA_SERVER = 'localhost:9092'
TOPIC_NAME_ORDENES = 'Ordenes'
TOPIC_NAME_RESUMEN = 'ResumenD'