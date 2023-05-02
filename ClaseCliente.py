from ClasePersonaTP import*
from datetime import date


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
        
    def Actualizar(self):
        try:
            campo=input('ingrese campo a actualizar')
            dato=input('ingrese el nuevo dato')
            cliente=input('ingrese DNI')
            clientes=open("ListaClientes.txt",'r')
            lista =clientes.readlines()
            clientes.close()
            cont=0
            with open("ListaClientes.txt",'w')as archivo:  
                for linea in lista:
                    if cliente in linea:
                        rotulo=linea.split(',')
                        if campo=='nombre':
                            rotulo[0]=dato
                        elif campo=='DNI':
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
                            rotulo[7]=int(anio)-int(dato)
                        else:
                            print('el campo ingresado no esta registrado')
                        cont=1
                        lineaNueva =  ','.join(rotulo)
                        archivo.write(lineaNueva)
                    else: 
                        archivo.write(linea)
                if cont==0:
                    print('el DNI ingresado no esta registrado')
        except:
            print("ha habido un error y no se pudo actualizar el cliente")

    def __str__(self):
        return 'El cliente se llama {},su DNI es{}, su genero es {}, su usario es {}, su contrasenia es {}, su telefono es {}, su direccion es {} y su antiguedad es {}'.format(self.nombre,self.DNI,self.genero,self.usuario,self.contrasenia,self.telefono,self.direccion,self.antiguedad)
    
    def Dar_alta(self):
        try:
            clientes=open(r"DatosClientes.unknown",'a')
            atributos=[self.nombre,self.DNI,self.genero,self.usuario,self.contrasenia,self.telefono,self.direccion,self.anioIngreso]
            for i in range(len(atributos)):
                if i!=len(atributos)-1:
                    clientes.write(str(atributos[i]))
                    clientes.write(',')
                else:
                    clientes.write(str(atributos[i]))
                    clientes.write('\n')
            clientes.close()
        except:     
            return ("Ha habido un error y no se ha podido dar de alta el usuario cliente pedido")

    def Dar_baja(self):
        try:
            dni=input("Ingrese el DNI del cliente que desea dar de baja:")
            clientes=open(r'DatosClientes.unknown','r')
            se_queda=""
            for fila in clientes:
                if dni not in fila:
                    se_queda+=(fila)
            clientes.close()
            clientes_w=open(r'DatosClientes.unknown','w')  
            clientes_w.write(se_queda)
            clientes_w.close()
            return ("Se ha dado de baja el usuario cliente con DNI:",str(dni))      
        except:     
            return ("Ha habido un error y no se ha podido dar de baja el usuario cliente pedido")