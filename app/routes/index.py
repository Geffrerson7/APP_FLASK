from flask import Blueprint, render_template,flash
from ..utils import insertar_personaje
from ..utils import gravatar

perfil_ruta=Blueprint('perfil_ruta',__name__)
@perfil_ruta.route('/')
def index():
     
    lista_personajes=insertar_personaje()
    return render_template('index2.html',lista=lista_personajes)

@perfil_ruta.route('/perfil')
def perfil():
    
    lista_personajes=insertar_personaje()
    return render_template('perfil.html',lista=lista_personajes)