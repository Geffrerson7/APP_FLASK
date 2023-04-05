
# FLASK_APP_RICK_AND_MORTY


## Descripción
Es una aplicación que extrae los datos de los personajes 
de la API "Rick and Morty", los almacena en la colección "personajes" 
de la base de datos "rick_y_morty" y los muestra ordenados por el id de forma 
descendente en la ruta raiz en grupos de 20 por cada página, en un total de 42 páginas. 

También extrae los datos de los capítulos, los almacena en la colección "episodios" y muestra los datos de los personajes que aparecen en dicho capitulo en la ruta dinámica
"capitulo/id". 

En ambos casos, se puede acceder a mas datos de la personaje haciendo click
en su nombre.

## Screenshots

![rick-and-morty-2](https://user-images.githubusercontent.com/61089189/230173717-5be97d79-48b5-419c-8f8c-7ace22be5a2a.png)

![rick-and-morty-3](https://user-images.githubusercontent.com/61089189/230173723-4b2f88f8-d235-4798-bf85-a106ffdee432.png)

![rick-and-morty-4](https://user-images.githubusercontent.com/61089189/230173725-62211d17-2d78-4657-8b38-a4deddff05d2.png)


## Rutas de la aplicación
Carga cada página del listado general de personajes:
```
http://127.0.0.1:5000/
http://127.0.0.1:5000/<int:id>
```
Muestra Perfil de un personaje en especifico
```
http://127.0.0.1:5000/perfil/<int:id>
```
Muestra los personajes de un capitulo en especifico
```
http://127.0.0.1:5000/capitulo/<int:id>
```
Muestra el perfil de un personaje en especifico desde un episodio en especifico
```
http://127.0.0.1:5000/perfil_ep/<int:id>
```

## Instalación local

Clonar el repositorio
```bash
  $ clone git https://github.com/Geffrerson7/FLASK-APP-RICK-AND-MORTY.git
```
Ir al directorio del proyecto
```bash
  $ cd FLASK-APP-RICK-AND-MORTY
```
Crear un entorno virtual

```sh
$ virtualenv venv
Axctivar el entorno virtual
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Crear las variables de entorno en el archivo .env

`APP_FLASK`

`FLASK_DEBUG`

`FLASK_ENV`

`SECRET_KEY`


Instalar las dependencias
```
(env)$ pip install -r requirements.txt
```

Una vez concluido todo eso, procedemos a iniciar la app
```sh
(env)$ flask run
```

Y navegar a la ruta
```sh
http://127.0.0.1:5000/
```
## Tecnologías y lenguajes utilizados

* **Python** (v. 3.10.7) [Source](https://www.python.org/)
* **Flask** (v. 2.2.3)  [Source](https://flask.palletsprojects.com/en/2.2.x/)
* **Pymongo** (v. 4.3.3) [Source](https://pymongo.readthedocs.io/en/stable/)
* **Jinja 2** (v. 3.1.2) [Source](https://jinja.palletsprojects.com/en/3.1.x/)
* **Bootstrap** (v. 5.2.3) [Source](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* **python-dotenv** (v. 1.0.0) [Source](https://pypi.org/project/python-dotenv/)
* **Rick and Morty API** [Source](https://rickandmortyapi.com/documentation)

    
## Autores

- [Raisa Vanessa Orellana Rios](https://www.github.com/Raisa320)
- [Gefferson Max Casasola Huamancusi ](https://www.github.com/Geffrerson7)
