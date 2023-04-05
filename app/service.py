import requests
from app.models.perfil import Personaje
from app.models.episode import Episodio
from app.db import db


def insertar_personaje(page):
    """Función que almacena los datos de los personajes ordenados de forma
    descendente por su id y agrupados de 20 en 20 en la colección "personajes"
    de la base de datos, si es que no está en ella y retorna una lista con los
    datos de los personajes almacenados para luego mostrarlos en una página del
    template index.html que tendrá 42 páginas"""
    page = 43 - page  # 42 -> 1
    url = "https://rickandmortyapi.com/api/character?page=" + str(page)
    r_perfil = requests.get(url)
    
    if r_perfil.ok:
        respuestaPerfil = r_perfil.json()
        for personaje in respuestaPerfil["results"]:
            if db.personajes.find_one({"id": personaje["id"]}) is None:
                firstSeen = first_seen(personaje["episode"])
                personaje_obj = Personaje(
                        personaje["id"],
                        personaje["name"],
                        personaje["status"],
                        personaje["species"],
                        personaje["type"],
                        personaje["gender"],
                        personaje["origin"]["name"],
                        personaje["location"]["name"],
                        personaje["image"],
                        firstSeen,
                    )
                db.personajes.insert_one(personaje_obj.to_json())
            ultimo = personaje["id"] + 1
    lista_personajes = (
        db.personajes.find({"id": {"$lt": ultimo}}).sort("id", -1).limit(20)
    )
    return list(lista_personajes)


def first_seen(arrayEpisodio: list):
    """Función cuyo parametro es la lista de las urls de los episodios donde
    aparece el personaje y que retorna un string con el nombre del primer
    capítulo donde aparece el personaje"""
    urlEpisodio1 = arrayEpisodio[0]
    requestUrl = requests.get(urlEpisodio1)
    if requestUrl.ok:
        respuesta = requestUrl.json()
        return respuesta["name"]
    return None


def insertar_episodio(id):
    """Función cuyo parámetro es el id del capítulo y almacena los datos
    de los capitulos en la coleccion "episodios" de la base de datos,
    si es que aun no están almacenados en ella"""
    if db.episodios.find_one({"id": id}) is None:
        url = "https://rickandmortyapi.com/api/episode/" + str(id)
        r_episodio = requests.get(url)
        if r_episodio.ok:
            episodio = r_episodio.json()
            episodio_obj = Episodio(
                episodio["id"],
                episodio["name"],
                episodio["air_date"],
                episodio["episode"],
                episodio["characters"],
                episodio["url"],
                episodio["created"],
            )
            db.episodios.insert_one(episodio_obj.to_json())


def personajes_de_episodio(id_ep):
    """Función, cuyo parámetro es el id del capítulo, que almacena los datos de sus personajes
    en la colección "personajes", si es que no están en la base de datos y al final retorna
    una lista con los datos de los personajes almacenados del capítulo"""
    lista_personajes = []
    episodio = db.episodios.find_one({"id": id_ep})
    for url in episodio["characters"]:
        id = url.split("/")[-1]
        if db.personajes.find_one({"id": int(id)}) is None:
            url_x = "https://rickandmortyapi.com/api/character/" + str(id)
            r_perfil = requests.get(url_x)
            if r_perfil.ok:
                respuestaPerfil = r_perfil.json()
                firstSeen = first_seen(respuestaPerfil["episode"])
                personaje_obj = Personaje(
                    respuestaPerfil["id"],
                    respuestaPerfil["name"],
                    respuestaPerfil["status"],
                    respuestaPerfil["species"],
                    respuestaPerfil["type"],
                    respuestaPerfil["gender"],
                    respuestaPerfil["origin"]["name"],
                    respuestaPerfil["location"]["name"],
                    respuestaPerfil["image"],
                    firstSeen,
                )
                db.personajes.insert_one(personaje_obj.to_json())
                lista_personajes.append(
                    db.personajes.find_one({"id": respuestaPerfil["id"]})
                )
        else:
            lista_personajes.append(db.personajes.find_one({"id": int(id)}))
    return lista_personajes
