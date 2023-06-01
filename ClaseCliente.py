from ClasePersonaTP import *
from datetime import date
from funciones import *

# coding=utf-8
hoy=date.today()
anio=hoy.year
class Cliente(Persona):
    def __init__(self,nombre,DNI,genero,usuario,contrasenia,telefono,direccion,anioIngreso,email):
        Persona.__init__(self,nombre,DNI,genero)
        self.usuario=usuario
        self.contrasenia=contrasenia
        self.telefono=telefono
        self.direccion=direccion
        self.antiguedad=int(anio)-int(anioIngreso)
        self.email=email
        
    def Actualizar(self,listav,listaa,clientess,empleadoss):
        try:
            campos={'nombre', 'DNIcliente', 'genero', 'usuario', 'contrasenia', 'telefono', 'direccion', 'anioIngreso',' email'}
            print('Campos disponibles a actualizar:',','.join(campos))
            campo=input('Ingrese campo a actualizar: ')
            if campo not in campos:
                campo=input('Ingrese campo a actualizar: ')
            dato=input('Ingrese el nuevo dato: ')
            dato=validacionesgrales(campo,dato,listav,listaa,clientess,empleadoss)
            cliente=input('Ingrese DNI del cliente que quiere actualizar: ')
            clientes=open(r"DatosClientes.txt",'r')
            lista =clientes.readlines()
            clientes.close()
            cont=0
            with open(r"DatosClientes.txt",'w')as archivo:  
                for linea in lista:
                    if cliente in linea:
                        rotulo=linea.split(',')
                        if campo=='nombre':
                            rotulo[0]=dato
                        elif campo=='DNIcliente':
                            rotulo[1]=dato
                        elif campo=='genero':
                            rotulo[2]=dato  
                        elif campo=='usuario':
                            rotulo[3]=dato
                        elif campo=='contrasenia':
                            rotulo[4]=dato
                        elif campo=='telefono':
                            rotulo[5]=anio-dato
                        elif campo=='direccion':
                            rotulo[6]=dato
                        elif campo=='anioIngreso':
                            rotulo[7]= int(anio)-int(dato)
                        elif campo=='email':
                            rotulo[8]=dato
                        else:
                            print('El campo ingresado no esta registrado.')
                        cont=1
                        lineaNueva =  ','.join(rotulo)
                        archivo.write(lineaNueva)
                    else: 
                        archivo.write(linea)
                if cont==0:
                    print('El DNI ingresado no esta registrado.')
        except:
            print("ha habido un error y no se pudo actualizar el cliente")

    def __str__(self):
        return 'El cliente se llama {},su DNI es{}, su genero es {}, su usario es {}, su contrasenia es {}, su telefono es {}, su direccion es {} y su antiguedad es {}'.format(self.nombre,self.DNI,self.genero,self.usuario,self.contrasenia,self.telefono,self.direccion,self.antiguedad)
        
    def Dar_alta(self,listav,listaa,list_clientes,empleadoss):
        try:
            print("Ha seleccionado registrarse")
            nuevo_usuario=input("Ingrese un nombre de usuario: ") 
            nuevo_usuario=validacionesgrales("usuario",nuevo_usuario,listav,listaa,list_clientes,empleadoss)
            contrasenia=input("Ingrese una contrasenia: ")
            nombre=input("Ingrese su nombre completo: ")
            dni=input("Ingrese su numero de DNI: ")
            dni=validacionesgrales("DNIcliente",dni,listav,listaa,list_clientes,empleadoss)
            genero=input("Ingrese 1 si es hombre, o 2 si es mujer o 3 si desea no aclarar : ")
            genero=validacionesgrales("genero",genero,listav,listaa,list_clientes,empleadoss)
            telefono=input("Ingrese su numero de telefono: ")
            direccion=input("Ingrese su direccion: ")
            anio_ingreso=anio
            email=input("Ingrese su email: ")
            clientes=open(r"DatosClientes.txt",'a')
            atributos=[nombre,dni,genero,nuevo_usuario,contrasenia,telefono,direccion,anio_ingreso,email]
            for i in range(len(atributos)):
                if i!=len(atributos)-1:
                    clientes.write(str(atributos[i]))
                    clientes.write(',')
                else:
                    clientes.write(str(atributos[i]))
                    clientes.write('\n')
            clientes.close()
            print("Se ha creado el usuario.")
        except:
            print("Ha habido un error y no se pudo crear el usuario.")
    
    def Dar_baja(self):
        try:
            print("Ha seleccionado eliminar un cliente del sistema.")
            dni=input("Ingrese el dni del cliente que desea eliminar: ")
            clientes=open(r'DatosClientes.unknown','r')
            se_queda=""
            for fila in clientes:
                if dni not in fila:
                    se_queda+=(fila)
            clientes.close()
            clientes_w=open(r'DatosClientes.txt','w')  
            clientes_w.write(se_queda)
            clientes_w.close()
            print("Se ha dado de baja el usuario cliente con DNI:",str(dni))      
        except:     
            print("Ha habido un error y no se ha podido dar de baja el usuario cliente pedido")