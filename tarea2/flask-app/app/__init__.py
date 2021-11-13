from flask import Flask, request, url_for

def redirect_url(default='index'): # Redireccionamiento desde donde vino la request
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

# Define the WSGI application object
app = Flask(__name__, template_folder='template')

# ============================================================================
# Blueprints (Routes)
from app.routes.rutas_ordenes import mod
from app.routes.rutas_resumen import mod

app.register_blueprint(routes.rutas_ordenes.mod)
app.register_blueprint(routes.rutas_resumen.mod)

# Configuraciones desde config.py
app.config.from_object('config')