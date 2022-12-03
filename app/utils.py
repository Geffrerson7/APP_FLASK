import requests
from app.models.perfil import Personaje
from app.models.episode import Episodio
from app.db import db


def insertar_personaje(page):
    page = 22 - page
    ultimo = (page * 20) + 1
    ultimoPersonaje = db.personajes.find_one({"id": page * 20})
    if ultimoPersonaje is None:
        url = "https://rickandmortyapi.com/api/character?page=" + str(page)
        r_perfil = requests.get(url)
        if r_perfil.ok:
            respuestaPerfil = r_perfil.json()
            for personaje in respuestaPerfil["results"]:
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
    return lista_personajes


def first_seen(arrayEpisodio: list):
    urlEpisodio1 = arrayEpisodio[0]
    requestUrl = requests.get(urlEpisodio1)
    if requestUrl.ok:
        respuesta = requestUrl.json()
        return respuesta["name"]
    return None


def insertar_episodio():
    for id_ep in range(1, 52):
        url = "https://rickandmortyapi.com/api/episode/" + str(id_ep)
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
    lista_personajes = []
    episodio = db.episodios.find_one({"id": id_ep})
    for url in episodio["characters"]:

        r_personaje = requests.get(url)
        if r_personaje.ok:
            personaje = r_personaje.json()
            if db.personajes.find_one({"id": personaje["id"]}) is None:
                url_x = "https://rickandmortyapi.com/api/character/" + str(
                    personaje["id"]
                )
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
            lista_personajes.append(db.personajes.find_one({"id": personaje["id"]}))

    return lista_personajes
