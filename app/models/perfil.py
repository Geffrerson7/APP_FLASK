class Perfil:
    def __init__(self,nombre, estado, especie):
        self.nombre=nombre
        self.estado=estado
        self.especie=especie

def to_json(self):
        return {
            'nombre':self.nombre,
            'estado':self.estado,
            'especie':self.especie,
            
        }