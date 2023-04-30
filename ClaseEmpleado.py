from ClasePersonaTP import*
from datetime import date
hoy=date.today()
anio=hoy.year

class Empleado(Persona):
    def __init__(self,nombre,DNI,genero,cargo,salario,legajo,anioIngreso,telefono):
        Persona.__init__(self,nombre,DNI,genero)
        self.cargo=cargo
        self.salario=salario
        self.legajo=legajo
        self.telefono=telefono
        self.antiguedad=int(anio)-int(anioIngreso)
        
    def Actualizar(self):
        campo=input('ingrese campo a actualizar')
        dato=input('ingrese el nuevo dato')
        if campo=='nombre':
            self.nombre=dato
        elif campo=='DNI':
            self.DNI=dato
        elif campo=='genero':
            self.genero=dato
        if campo=='cargo':
            self.cargo=dato
        elif campo=='salario':
            self.salario=dato
        elif campo=='legajo':
            self.legajo=dato
        elif campo=='anioIngreso':
            self.anioIngreso=dato
        elif campo=='telefono':
            self.telefono=dato
        else:
            print('el campo ingresado no esta registrado')
    def __str__(self):
        return 'El empleado se llama {},su DNI es{}, su genero es {}, su cargo es {}, su contrasenia es {}, su telefono es {}, su direccion es {} y su antiguedad es {}'.format(self.nombre,self.DNI,self.genero,self.usuario,self.contrasenia,self.telefono,self.direccion,self.antiguedad)
    def Dar_alta(self):
        empleados=open(r"DatosEmpleados.unknown",'a')
        atributos=[self.nombre,self.DNI,self.genero,self.cargo,self.salario,self.legajo,self.antiguedad,self.telefono]
        for i in range(len(atributos)):
            if i!=len(atributos)-1:
                empleados.write(str(atributos[i]))
                empleados.write(',')
            else:
                empleados.write(str(atributos[i]))
                empleados.write('\n')
        empleados.close()

    def Dar_baja(self):
        try:
            dni=input("Ingrese el legajo del empleado que desea dar de baja:")
            empleados=open(r'DatosEmpleados.unknown','r')
            se_queda=""
            for fila in empleados:
                if dni not in fila:
                    se_queda+=(fila)
            empleados.close()
            empleados_w=open(r'DatosEmpleados.unknown','w')  
            empleados_w.write(se_queda)
            empleados_w.close()
            return ("Se ha dado de baja el empleado con DNI:",str(dni))      
        except:     
            return ("Ha habido un error y no se ha podido dar de baja el empleado pedido")