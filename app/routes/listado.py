from flask import Blueprint, render_template
perfil_ruta=Blueprint('libros_ruta',__name__)
import requests
from app.models.perfil import Perfil
from app.db import db

@perfil_ruta.route('/crear/<page>', methods=['GET'])
def index(page):  
    url='https://rickandmortyapi.com/api/character?page='+page
    
    r_perfil = requests.get(url)
    if r_perfil.ok:
        respuestaPerfil = r_perfil.json()
        nombre=respuestaPerfil["results"][0]["name"]
        estado=respuestaPerfil["results"][0]["estatus"]
        especie=respuestaPerfil["results"][0]["especies"]
        libro_obj=Perfil(nombre,estado,especie)
    db.libros.insert_one(libro_obj.to_json())     
    return render_template('index.html')

