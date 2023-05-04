
from datetime import *
from random import *
from funciones import *
hoy = date.today()
anio = hoy.year
    
class Propiedad():
    estados_validos = ['en venta', 'en alquiler', 'alquilado', 'vendido']
    def __init__(self,cliente, m2,direccion,barrio,id,numambientes,tipo,anioconstruccion,estado,precio,fechainicio,inquilino,fechafin):
        if estado not in Propiedad.estados_validos:
            raise ValueError("el estado no es valido")
        self.cliente=cliente
        self.m2=m2
        self.direccion=direccion
        self.barrio=barrio
        self.numambientes=numambientes
        self.tipo=tipo
        self.estado=estado
        self.id=id
        self.precio=precio
        self.antiguedad=int(anio)-int(anioconstruccion)
        self.fechainicio = fechainicio
        self.inquilino = inquilino
        self.fechafin = fechafin
    def __str__(self):
        return 'La propiedad tiene{} m2, la direccion es{}, la cantidad de ambientes que tiene es {}, es de tipo {}, se construyo en {} y se encuentra {}'.format(self.m2,self.direccion,self.numambientes,self.tipo,self.antiguedad,self.estado)

    
    def Dar_alta(self,listav,listaa,clientess,empleadoss):
        try:
            print("Ha seleccionado ingresar una propiedad.")
            propietario=input("Ingrese el nombre del propietario: ")
            m2=input("Ingrese el numero de metros cuadrados de la propiedad: ")
            m2=validacionesgrales("m2",m2,listav,listaa,clientess,empleadoss)
            direccion=input("Ingrese la direccion de la propiedad: ")
            barrio=input("Ingrese el barrio donde se encuantra la propiedad: ")
            id=str(randint(100,999))
            id=validacionesgrales("id",id,listav,listaa,clientess,empleadoss)
            num_ambientes=input("Ingrese el numero de ambientes de la propiedad: ")
            num_ambientes=validacionesgrales("numambientes",num_ambientes,listav,listaa,clientess,empleadoss)
            tipo=input("Ingrese 1 si la propiedad es un departamento,2 si es una casa, o 3 si es un local comercial: ")
            tipo=validacionesgrales("tipo",tipo,listav,listaa,clientess,empleadoss)
            anio_const=input("Ingrese el año de contruccion de la propiedad: ")
            anio_const=validacionesgrales("anioconstruccion",anio_const,listav,listaa,clientess,empleadoss)
            estado=input("Ingrese 1 si desea poner su popiedad en venta, o 2 si desea ponerla en alquiler: ")#Asumo q no va a estar vendida o alquilada cuando se ingresa
            estado=validacionesgrales("estado",estado,listav,listaa,clientess,empleadoss)
            precio=input("Ingrese el monto en dolares al cual desea ofrecer la propiedad: ")
            precio=validacionesgrales("precio",precio,listav,listaa,clientess,empleadoss)
            inquilino=" "
            fechainicio=" "
            fechafin=" "
            venta=open(r"ListaPropiedadesVenta.txt",'a')
            alquiler=open(r"ListaPropiedadesAlquiler",'a')
            arch_empleados=r"DatosEmpleados.unknown"
            empleados=extraerInfo(arch_empleados)
            pos_em=randint(0,len(empleados)-1)
            for i in range(len(empleados)):
                if i==pos_em:
                    empleado=empleados[i][0]
            atributos=[propietario,m2,direccion,barrio,id,num_ambientes,tipo,anio_const,estado,precio,inquilino,empleado,fechainicio,fechafin]
            for i in range(len(atributos)):
                if i!=len(atributos)-1:
                    if self.estado=="en venta":
                        venta.write(str(atributos[i]))
                        venta.write(',')
                    elif self.estado=="en alquiler":
                        alquiler.write(str(atributos[i]))
                        alquiler.write(',')
                else:
                    if self.estado=="en venta":
                        venta.write(str(atributos[i]))
                        venta.write('\n')
                    elif self.estado=="en alquiler":
                        alquiler.write(str(atributos[i]))
                        alquiler.write('\n')
            venta.close()
            alquiler.close()
            print("Se ha ingresado la propiedad al sistema. El id de su nueva propiedad es "+str(self.id))
        except:
            print("Ha habido un error y no se pudo ingresar la propiedad al sistema")

    def Dar_baja(self): 
        try:
            print("Ha seleccionado eliminar una propiedad del sistema.")
            id=input("Ingrese el id de la propiedad que desea eliminar: ")
            en_venta=open(r'ListaPropiedadesVenta.txt','r')
            en_alquiler=open(r"ListaPropiedadesAlquiler",'r')
            se_queda_v=""
            se_queda_a=""
            esta=""
            for linea in en_venta:
                if id not in linea:
                    se_queda_v+=(linea)
                else:
                    esta = 'venta'
            for fil in en_alquiler:
                if id not in fil:
                    se_queda_a+=(fil)
                else:
                    esta="alquiler"
            en_venta.close()
            en_alquiler.close()
            if esta=="venta":
                en_venta_w=open(r'ListaPropiedadesVenta.txt','w')  
                en_venta_w.write(se_queda_v)
                en_venta_w.close()
            elif esta=="alquiler":
                en_alquiler_w=open(r"ListaPropiedadesAlquiler",'w')  
                en_alquiler_w.write(se_queda_a)
                en_alquiler_w.close()

            print("Se ha dado de baja la propiedad con ID:"+str(id))    
        except:
             print("Ha habido un error y no se pudo dar de baja la propiedad")

             

    def Actualizar(self,listav,listaa,clientess,empleadoss):
        try:
            campo=input('ingrese campo a actualizar')   
            dato=input('ingrese el nuevo dato')
            dato=validacionesgrales(campo,dato,listav,listaa,clientess,empleadoss)
            propiedad=input('ingrese id de la propiedad que quiere actualizar')
            accion=input('ingrese 1 si la propiedad esta en venta o 2 si esta en alquiler')
            while accion!= '1' and accion!='2':
                accion=input('ingrese si la propiedad esta en venta o en alquiler')
            if accion=='1':
                propiedades=open("ListaPropiedadesVenta.txt",'r')
                arch="ListaPropiedadesVenta.txt"
            if accion=='2':
                propiedades=open("ListaPropiedadesAlquiler",'r')
                arch="ListaPropiedadesAlquiler"
            lista =propiedades.readlines()
            propiedades.close()
            cont=0
            with open(arch,'w')as archivo:
                for linea in lista:
                    if propiedad in linea:
                        rotulo=linea.split(',')
                        if campo=='cliente':
                            rotulo[0]=dato
                        elif campo=='m2':
                            rotulo[1]=dato
                        elif campo=='direccion':
                            rotulo[2]=dato  
                        elif campo=='barrio':
                            rotulo[3]=dato
                        elif campo=='id':
                            rotulo[4]=dato
                        elif campo=='numambientes':
                            rotulo[5]=dato
                        elif campo=='tipo':
                            rotulo[6]=dato
                        elif campo=='anioconstruccion':
                            rotulo[7]=int(anio)-int(dato)
                        elif campo=='estado':
                            rotulo[8]=dato
                        elif campo=='precio':
                            rotulo[9]=dato
                        elif campo == 'fechainicio':
                            rotulo[10] = dato
                        elif campo=='inquilino':
                            rotulo[11]=dato
                        elif campo=='fechafin':
                            rotulo[12]=dato
                        else:
                            print('el campo ingresado no esta registrado')
                        cont=1
                        lineaNueva = ','.join(rotulo)
                        archivo.write(lineaNueva)
                    else: #no es la propiedad
                        archivo.write(linea)
                if cont==0:
                    print('el id ingresado no esta registrado')
        except:
            print("ha habido un error y no se pudo actualizar la propiedad")

    def alquiler(self, estado, lista):
        alquilada = True
        inquilino = input('Ingrese su nombre completo:\n')
        self.estado = estado
        self.fecha_alquiler = date.today()
        
        while alquilada:

            idprop = input('ingrese el id de la propiedad que quiere alquilar:\n')

            for i in range(len(lista)):
                if lista[i][4]==idprop and lista[i][8] == 'en alquiler' :
                    lista[i][8] = estado
                    lista[i][10] = inquilino 
                    lista[i][12] = str(date.today()) #fecha de inicio de alquiler
                    lista[i][13] = str(agregar_años(date.today(), 1)) #fecha de fin de alquiler
                    
                    contenido = crearstring(lista)
                    escribirinfo(r'ListaPropiedadesAlquiler', contenido)
                    print ('la operación fue exitosa')
                    alquilada = False
            
            if alquilada:
                print ('esa propiedad no esta disponible para alquilar')
        print_tabla(lista)
        return lista

    #alquiler ('Nombre Apellido', 'alquilada', listaa)

    def venta(self, estado, lista):
        
        self.estado = estado
        propietario = input('Ingrese su nombre completo:\n')
        vendida = True

        while vendida:

            idprop = input('ingrese el id de la propiedad que quiere comprar:\n')
            
            for i in range(len(lista)):
                if lista[i][4]==idprop and lista[i][8] == 'en venta' :
                    lista[i][10] = lista[i][0]
                    lista[i][0] = propietario
                    lista[i][8] = estado
                    lista[i][12] = str(date.today()) #fecha de venta
                    contenido = crearstring(lista)
                    escribirinfo(r'ListaPropiedadesVenta.txt', contenido)
                    print ('la operación fue exitosa')
                    vendida = False

            if vendida:
                print ('esa propiedad no esta disponible para vender')
            
        return lista

    #venta('Nombre Apellido' , 'vendida' , listav)

    def buscarporbarrio(self, lista):
        final = []
        barrio = input('ingrese el barrio en el que busca una propiedad:\n')
        for i in range(len(lista)):
            if (lista[i][8] == 'en alquiler' or lista[i][8] == 'en venta') and (lista[i][3] == barrio):
                final += [lista[i]]

        if len(final) == 0:
            print ('no hay propiedades disponibles en ese barrio')

        else:
            print ('las propiedades disponibles en ese barrio son:')
            print_tabla(final)
                   

    def buscarporprecio(self, lista):
        final = []
        min = int(input('ingrese un precio minimo:'))
        max = int(input('ingrese un precio maximo:'))

        for i in range(len(lista)):
            if (lista[i][8] == 'en alquiler' or lista[i][8] == 'en venta') and (int(lista[i][9]) <= max and int(lista[i][9]) >= min):
                final += [lista[i]]

        if len(final) == 0:
            print ('no hay propiedades que esten dentro del rango ingresado')

        else:
            print ('las propiedades dentro del rango de precios ingresado son:')
            print_tabla(final)

    #buscarporprecio(lista)

    def mostrarprop(self, lista):
        nueva = []
        print(len(lista))
        for i in range(len(lista)):
            if lista[i][8] == 'en alquiler' or lista[i][8] == 'en venta':
                nueva.append(lista[i])
        print_tabla(nueva)
       
    def calcular_comision(self, empleado, lista1):
        self.empleado = empleado
        if self.estado == 'vendido':
            comision =self.precio  * 0.05
        elif self.estado=='alquilado':
            comision=self.precio*0.04
        else:
            comision=0
        es=False
        print_tabla(lista1)
        for i in range(len(lista1)):
          if lista1[i][0]==empleado:
              es=True
              fila=i
            
        if es:
            salario=lista1[fila][4]
        print(salario)
        salarioFinal=int(salario)+int(comision)
        return empleado,int(comision),salarioFinal
    
    def Calcular_precio_m2(self):
        return ('El precio del m2 es',int(self.precio)/int(self.m2))
    