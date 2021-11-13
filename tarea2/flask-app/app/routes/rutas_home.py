from flask import Blueprint, request, json, url_for, render_template
from config import BASE_DIR

def redirect_url(default='index'): # Redireccionamiento desde donde vino la request
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

mod = Blueprint('rutas_home', __name__)

@mod.route("/", methods=['GET'])
def home(id):
    return render_template("home.html")