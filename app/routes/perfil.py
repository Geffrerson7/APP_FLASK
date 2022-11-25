from flask import Blueprint, render_template,flash
import requests
from app.models.perfil import Personaje
from app.db import db

perfil_ruta=Blueprint('libros_ruta',__name__)
@perfil_ruta.route('/')
def index():
     
    lista_personajes=[]                
    for personaje in db.personajes.find().sort("id", -1):
        personaje_obj=Personaje(
                    personaje["id"],
                    personaje["name"],
                    personaje["status"],
                    personaje["species"],
                    personaje["type"],
                    personaje["gender"],
                    personaje["origin"]["name"],
                    personaje["location"]["name"],
                    personaje["image"]
                    )
        lista_personajes.append(personaje_obj.to_json())

    return render_template('index2.html',lista=lista_personajes)

@perfil_ruta.route('/insert', methods=['GET'])
def insertar_personaje():    
    for i in range(1,22): 
            url='https://rickandmortyapi.com/api/character?page='+str(i)
                
            r_perfil = requests.get(url)
            if r_perfil.ok:
                respuestaPerfil = r_perfil.json()
                for datos in respuestaPerfil["results"]:
                    db.personajes.insert_one(datos)

    flash("Personajes insertados", "success")

    return "Personajes insertados"