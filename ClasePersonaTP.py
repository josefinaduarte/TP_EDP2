

class Persona():
    def __init__(self,nombre,DNI=0,genero='H'):
        self.nombre=nombre
        self.DNI=DNI
        self.genero=genero
    def __str__(self):
        return 'La persona se llama {},su DNI es{}, su genero es {}, su cargo es {}, su contrasenia es {}, su telefono es {}, su direccion es {} y su antiguedad es {}'.format(self.nombre,self.DNI,self.genero,self.usuario,self.contrasenia,self.telefono,self.direccion,self.antiguedad)
