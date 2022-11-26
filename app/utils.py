import requests
from app.models.perfil import Personaje
from app.db import db
import hashlib

def insertar_personaje():
    
    if db.personajes.estimated_document_count()==0:    
        for i in range(1,22): 
                url='https://rickandmortyapi.com/api/character?page='+str(i)
                    
                r_perfil = requests.get(url)
                if r_perfil.ok:
                    respuestaPerfil = r_perfil.json()
                    for personaje in respuestaPerfil["results"]:
                        firstSeen=first_seen(personaje["episode"])
                        personaje_obj=Personaje(
                        personaje["id"],
                        personaje["name"],
                        personaje["status"],
                        personaje["species"],
                        personaje["type"],
                        personaje["gender"],
                        personaje["origin"]["name"],
                        personaje["location"]["name"],
                        personaje["image"],
                        firstSeen
                        )
                        db.personajes.insert_one(personaje_obj.to_json())
    lista_personajes=db.personajes.find().sort("id",-1)
    return lista_personajes

def first_seen(arrayEpisodio:list):
    urlEpisodio1=arrayEpisodio[0]
    requestUrl=requests.get(urlEpisodio1)
    if requestUrl.ok:
        respuesta=requestUrl.json()
        return respuesta["name"]
    return None

