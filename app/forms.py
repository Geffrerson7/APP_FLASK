from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,DateField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class LibroForm(FlaskForm):
    titulo=StringField('Titulo', validators=[DataRequired()])
    autor=StringField('Autor', validators=[DataRequired()])
    pagina=IntegerField('Número de páginas', validators=[DataRequired()])
    publicacion=DateField('Publicación', validators=[DataRequired()])
    descripcion=TextAreaField('Descripción', validators=[DataRequired()])
    isbn=StringField('ISBN', validators=[DataRequired()])
    boton=SubmitField('Guardar libro')