import requests
from app.models.perfil import Personaje
from app.db import db
import hashlib

def insertar_personaje():    
    for i in range(1,22): 
            url='https://rickandmortyapi.com/api/character?page='+str(i)
                
            r_perfil = requests.get(url)
            if r_perfil.ok:
                respuestaPerfil = r_perfil.json()
                for personaje in respuestaPerfil["results"]:
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
                    db.personajes.insert_one(personaje_obj.to_json())


    lista_personajes=db.personajes.find().sort("id",-1)
    return lista_personajes

