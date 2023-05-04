from ClasePersonaTP import*
from datetime import date
from random import *
from funciones import *
hoy=date.today()
anio=hoy.year

class Empleado(Persona):
    def __init__(self,nombre,DNI,genero,cargo,salario,legajo,anioIngreso,telefono):
        Persona.__init__(self,nombre,DNI,genero)
        self.cargo=cargo
        self.salario=salario
        self.legajo=legajo
        self.antiguedad=str(int(anio)-int(anioIngreso))
        self.telefono=telefono
    
    def Actualizar(self,listav,listaa,clientes,empleadoss):
        try:
            print('Campos disponibles a actualizar: nombre, DNIempleado, genero, cargo, salario, legajo, anioIngreso, telefono')
            campo=input('Ingrese campo a actualizar: ')
            dato=input('Ingrese el nuevo dato: ')
            dato=validacionesgrales(campo,dato,listav,listaa,clientes,empleadoss)
            empleado=input('Ingrese dni del empleado que quiere actualizar: ')
            empleados=open('DatosEmpleados.txt','r')
            lista =empleados.readlines()
            empleados.close()
            cont=0
            with open(r"DatosEmpleados.txt",'w')as archivo:  
                for linea in lista:
                    if empleado in linea:
                        rotulo=linea.split(',')
                        if campo=='nombre':
                            rotulo[0]=dato
                        elif campo=='DNIempleado':
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
                            rotulo[6]=int(anio)-int(dato)
                        elif campo=='telefono':
                            rotulo[7]=dato
                        else:
                            print('El campo ingresado no esta registrado.')
                        cont=1
                        lineaNueva = ','.join(rotulo)
                        archivo.write(lineaNueva)
                    else: 
                        archivo.write(linea)
                if cont==0:
                    print('El DNI ingresado no esta registrado.')
        except:
            print("Ha habido un error y no se pudo actualizar el empleado.")
    
    def __str__(self):
        return 'El empleado se llama {},su DNI es{}, su genero es {}, su cargo es {}, su contrasenia es {}, su telefono es {}, su direccion es {} y su antiguedad es {}'.format(self.nombre,self.DNI,self.genero,self.usuario,self.contrasenia,self.telefono,self.direccion,self.antiguedad)
        
    def Dar_alta(self,listav,listaa,clientes,lista_empleados):
        try:
            nuevo_nombre=input("Ingrese el nombre completo del empleado: ") 
            dni=input("Ingrese su numero de DNI: ")
            dni=validacionesgrales("DNIempleado",dni,listav,listaa,clientes,lista_empleados)
            genero=input("Ingrese 1 si es hombre, o 2 si es mujer: ")
            genero=validacionesgrales("genero",genero,listav,listaa,clientes,lista_empleados)
            telefono=input("Ingrese su numero de telefono: ")
            anio_ingreso=anio
            cargo=input("Ingrese el cargo del nuevo empleado: ")
            salario=str(randint(50000,500000))
            legajo=str(randint(10000,99999))
            legajo=validacionesgrales("legajo",legajo,listav,listaa,clientes,lista_empleados)
            empleados=open(r"DatosEmpleados.txt",'a')
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
            empleados=open(r'DatosEmpleados.txt','r')
            se_queda=""
            for fila in empleados:
                if legajo not in fila:
                    se_queda+=(fila)
            empleados.close()
            empleados_w=open(r'DatosEmpleados.txt','w')  
            empleados_w.write(se_queda)
            empleados_w.close()
            print("Se ha dado de baja el empleado con legajo:",str(legajo))      
        except:     
            print("Ha habido un error y no se ha podido dar de baja el empleado pedido")
