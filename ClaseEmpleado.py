from ClasePersonaTP import*
from datetime import date
from random import *
hoy=date.today()
anio=hoy.year

class Empleado(Persona):
    def __init__(self,nombre,DNI,genero,cargo,salario,legajo,anioIngreso,telefono):
        Persona.__init__(self,nombre,DNI,genero)
        self.cargo=cargo
        self.salario=salario
        self.legajo=legajo
        self.antiguedad=int(anio)-int(anioIngreso)
        self.telefono=telefono
    
    def Actualizar(self):
        try:
            campo=input('ingrese campo a actualizar')
            dato=input('ingrese el nuevo dato')
            empleado=input('ingrese dni del empleado que quiere actualizar')
            empleados=open("DatosEmpleados.unknown",'r')
            lista =empleados.readlines()
            empleados.close()
            cont=0
            with open("DatosEmpleados.unknown",'w')as archivo:  
                for linea in lista:
                    if empleado in linea:
                        rotulo=linea.split(',')
                        if campo=='nombre':
                            rotulo[0]=dato
                        elif campo=='DNI':
                            rotulo[1]=dato
                        elif campo=='genero':
                            rotulo[2]=dato  
                        elif campo=='cargo':
                            rotulo[3]=dato 
                        elif campo=='salario':
                            rotulo[4]=dato 
                        elif campo=='legajo':
                            rotulo[5]=dato
                        elif campo=='anioIngreso':
                            rotulo[8]=int(anio)-int(dato)
                        elif campo=='telefono':
                            rotulo[6]=dato
                        else:
                            print('el campo ingresado no esta registrado')
                        cont=1
                        lineaNueva = ','.join(rotulo)
                        archivo.write(lineaNueva)
                    else: 
                        archivo.write(linea)
                if cont==0:
                    print('el DNI ingresado no esta registrado')
        except:
            print("ha habido un error y no se pudo dar de baja el empleado")
    
    def __str__(self):
        return 'El empleado se llama {},su DNI es{}, su genero es {}, su cargo es {}, su contrasenia es {}, su telefono es {}, su direccion es {} y su antiguedad es {}'.format(self.nombre,self.DNI,self.genero,self.usuario,self.contrasenia,self.telefono,self.direccion,self.antiguedad)
        
    def Dar_alta(self,lista_empleados):
        try:
            nuevo_nombre=input("Ingrese el nombre completo del empleado") 
            dni=input("Ingrese su numero de DNI")
            while not dni.isdigit() or len(dni)!=8:
                dni=input("El dni no es valido, ingreselo nuevamente: ")
            for i in range(len(lista_empleados)):
                if lista_empleados[i][1]==dni:
                    nuevo_=input("El empleado ya esta registrado, ingrese otro:")
            genero=input("Ingrese 1 si es hombre, o 2 si es mujer: ")
            while genero not in "12":
                genero=input("Lo ingresado no es valido, intentelo nuevamente.Ingrese 1 si es hombre, o 2 si es mujer: ")
            if genero=="1":
                genero="Male"
            else:
                genero="Female"
            telefono=input("Ingrese su numero de telefono: ")
            while not telefono.isdigit():
                telefono=input("El numero de telefono no es valido, ingrese nuevamente un numero de telefono: ")
            anio_ingreso=anio
            cargo=input("Ingrese el cargo del nuevo empleado: ")
            salario=str(randint(50000,500000))
            legajo=str(randint(10000,99999))
            lista_legajos=[]
            for i in range(len(lista_empleados)):
                lista_legajos.append(lista_empleados[i][5])
            while legajo in lista_legajos:
                legajo=str(randint(10000,99999))
            empleados=open(r"C:\Users\consu\OneDrive\Documents\GitHub\TP_EDP2\DatosEmpleados.unknown",'a')
            atributos=[nuevo_nombre,dni,genero,cargo,salario,legajo,anio_ingreso,telefono]
            for i in range(len(atributos)):
                if i!=len(atributos)-1:
                    empleados.write(str(atributos[i]))
                    empleados.write(',')
                else:
                    empleados.write(str(atributos[i]))
                    empleados.write('\n')
            empleados.close()
            print("Se ha creado el empleado.")
        except:
            print("Ha habido un error y no se pudo ingresar al empleado al sistema.")

    def Dar_baja(self,legajo):
        try:
            empleados=open(r'DatosEmpleados.unknown','r')
            se_queda=""
            for fila in empleados:
                if legajo not in fila:
                    se_queda+=(fila)
            empleados.close()
            empleados_w=open(r'DatosEmpleados.unknown','w')  
            empleados_w.write(se_queda)
            empleados_w.close()
            print("Se ha dado de baja el empleado con legajo:",str(legajo))      
        except:     
            print("Ha habido un error y no se ha podido dar de baja el empleado pedido")