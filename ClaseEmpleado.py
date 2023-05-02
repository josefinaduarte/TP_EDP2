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
        self.antiguedad=int(anio)-int(anioIngreso)
        self.telefono=telefono
    
    def Actualizar(self):
        try:
            campo=input('ingrese campo a actualizar')
            dato=input('ingrese el nuevo dato')
            empleado=input('ingrese dni')
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
    
    def Dar_alta(self):
        try:
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
        except:     
            return ("Ha habido un error y no se ha podido dar de alta el empleado pedido")
    
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