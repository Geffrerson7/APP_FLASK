
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

![App Screenshot](https://drive.google.com/file/d/1CXZpqSZNdEP80mlknoS5byFLeVS11Huy/view?usp=share_link)

![App Screenshot](https://drive.google.com/file/d/1G27WnLDlo4semnR-SaWDcKAijAUWB0Lf/view?usp=sharing)

![App Screenshot](https://drive.google.com/file/d/13CccgGDKnsJTDHKovUP9zF-GwJM_B26v/view?usp=share_link)


## Variables de entorno

Para ejecutar este proyecto, necesitas agregar las siguientes
variables de entorno a tu archivo .env

`APP_FLASK`

`FLASK_DEBUG`

`FLASK_ENV`

`SECRET_KEY`


## Requirements

Si han clonado un proyecto de github y quieren instalar las dependencias, pueden usar el archivo requirements.txt

```
pip install -r requirements.txt
```
    
## Autores

- Raisa Vanessa Orellana Rios ([Raisa320](https://www.github.com/Raisa320))
- Gefferson Max Casasola Huamancusi ([Geffrerson7](https://www.github.com/Geffrerson7))
