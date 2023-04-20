from ClasePersonaTP import*
from datetime import date


hoy=date.today()
anio=hoy.year
class Cliente(Persona):
    def __init__(self,nombre,DNI,genero,usuario,contrasenia,telefono,direccion,anioIngreso):
        Persona.__init__(self,nombre,DNI,genero)
        self.usuario=usuario
        self.contrasenia=contrasenia
        self.telefono=telefono
        self.direccion=direccion
        self.antiguedad=anio-anioIngreso
        
    def Actualizar(self):
        campo=input('ingrese campo a actualizar')
        dato=input('ingrese el nuevo dato')
        if campo=='nombre':
            self.nombre=dato
        elif campo=='DNI':
            self.DNI=dato
        elif campo=='genero':
            self.genero=dato
        elif campo=='usuario':
            self.usuario=dato
        elif campo=='contrasenia':
            self.contrasenia=dato
        elif campo=='telefono':
            self.telefono=dato
        elif campo=='direccion':
            self.direccion=dato
        elif campo=='antiguedad':
            self.antiguedad=dato
        else:
            print('el campo ingresado no esta registrado')
    
    def __str__(self):
        return 'El cliente se llama {},su DNI es{}, su genero es {}, su usario es {}, su contrasenia es {}, su telefono es {}, su direccion es {} y su antiguedad es {}'.format(self.nombre,self.DNI,self.genero,self.usuario,self.contrasenia,self.telefono,self.direccion,self.antiguedad)
    
    def Dar_alta(self):
        clientes=open(r"DatosEmpleados.unknown",'a')
        atributos=[self.nombre,self.DNI,self.genero,self.usuario,self.contrasenia,self.telefono,self.direccion,self.anioIngreso]
        for i in range(len(atributos)):
            if i!=len(atributos)-1:
                clientes.write(str(atributos[i]))
                clientes.write(',')
            else:
                clientes.write(atributos[i])
                clientes.write('\n')
        clientes.close()
