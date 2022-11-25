from flask import Blueprint, render_template, request, flash
libros_ruta=Blueprint('libros_ruta',__name__)
from app.forms import LibroForm
from app.models.libro import Libro
from app.db import db

@libros_ruta.route('/')
def index():
    return render_template('index.html')

@libros_ruta.route('/crear-libro', methods=['GET', 'POST'])
def crear_libro():
    formulario=LibroForm()
    
    if request.method=='POST':
        if formulario.validate_on_submit():

            libro_obj=Libro(
                formulario.titulo.data,
                formulario.autor.data,
                formulario.pagina.data,
                formulario.publicacion.data,
                formulario.descripcion.data,
                formulario.isbn.data)
        
            db.libros.insert_one(libro_obj.to_json())
            flash("Libros registrados", "success")

    return render_template('crear_libro.html', formulario=formulario)