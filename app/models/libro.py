import datetime
class Libro:
    def __init__(self,titulo,autor,pagina,publicacion,descripcion,isbn):
        self.titulo=titulo
        self.autor=autor
        self.pagina=pagina
        self.publicacion=publicacion
        self.descripcion=descripcion
        self.isbn = isbn

    def to_json(self):
        return {
            'titulo':self.titulo,
            'autor':self.autor,
            'pagina':self.pagina,
            'publicacion':datetime.datetime.strptime(str(self.publicacion),"%Y-%m-%d"),
            'descripcion':self.descripcion,
            'isbn':self.isbn
        }
