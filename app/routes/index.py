from flask import Blueprint, render_template
from ..utils import insertar_personaje, insertar_episodio, personajes_de_episodio

from app.db import db

perfil_ruta=Blueprint('perfil_ruta',__name__)
@perfil_ruta.route('/<int:page>')
@perfil_ruta.route('/')
def index(page=1):
    paginas={"inicio":1,"fin":22}
    lista_personajes=insertar_personaje(page)
    return render_template('index.html',lista=lista_personajes,paginas=paginas)

@perfil_ruta.route('/perfil/<int:id>')
def perfil(id):
    personaje=db.personajes.find_one({'id':id})
    
    return render_template('perfil.html',personaje=personaje)

@perfil_ruta.route('/capitulo/<int:id>')
def episodio(id):
   insertar_episodio()
   lista_personajes=personajes_de_episodio(id)
   return render_template('episodio.html',lista_personajes=lista_personajes)