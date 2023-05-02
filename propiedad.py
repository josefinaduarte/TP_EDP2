
from datetime import *
from random import *
from MenuTP import extraerInfo
hoy = date.today()
anio = hoy.year

def agregar_años(fecha, años):
    try:
        return fecha.replace(year=fecha.year + años)
    except ValueError:
        # si no existe el 29 de febrero, poner el 28:
        return fecha.replace(year=fecha.year + años, dia=28)
    
class Propiedad():
    estados_validos = ['en venta', 'en alquiler', 'alquilado', 'vendido']
    def __init__(self,cliente, m2,direccion,barrio,id,numambientes,tipo,anioconstruccion,estado,precio,fecha,inquilino):
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
        self.fecha = fecha
        self.inquilino = inquilino
    def __str__(self):
        return 'La propiedad tiene{} m2, la direccion es{}, la cantidad de ambientes que tiene es {}, es de tipo {}, se construyo en {} y se encuentra {}'.format(self.m2,self.direccion,self.numambientes,self.tipo,self.antiguedad,self.estado)

    def Dar_alta(self):
        venta=open(r"ListaPropiedadesVenta.txt",'a')
        alquiler=open(r"ListaPropiedadesAlquiler",'a')
        arch_empleados=r"DatosEmpleados.unknown"
        empleados=extraerInfo(arch_empleados)
        pos_em=randint(0,len(empleados)-1)
        print(pos_em)
        for i in range(len(empleados)):
            if i==pos_em:
                empleado=empleados[i][0]
                print(empleado)
        atributos=[self.cliente,self.m2,self.direccion,self.numambientes,self.tipo,self.antiguedad,self.estado,self.precio,self.inquilino,empleado,self.fecha]
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

    def Actualizar(self):
        try:
            campo=input('ingrese campo a actualizar')   
            dato=input('ingrese el nuevo dato')
            propiedad=input('ingrese id')
            accion=input('ingrese 1 si la propiedad esta en venta o 2 si esta en alquiler')
            while accion!= '1' and accion!='2':
                accion=input('ingrese si la propiedad esta en venta o en alquiler')
            if accion=='1':
                propiedades=open("ListaPropiedadesVenta.txt",'r')
                arch="ListaPropiedadesVenta.txt"
            if accion=='2':
                propiedades=open("ListaPropiedadesAlquiler.txt",'r')
                arch="ListaPropiedadesAlquiler.txt"
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
                            rotulo[7]=anio-dato
                        elif campo=='estado':
                            rotulo[8]=dato
                        elif campo=='precio':
                            rotulo[9]=dato
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
            print("ha habido un error y no se pudo dar de baja la propiedad")

    def alquiler(self, inquilino, estado, lista):
        self.inquilino = inquilino
        self.estado = estado
        self.fecha_alquiler = date.today()
        alquilada = True
        while alquilada:
            idprop = input('ingrese el id de la propiedad que quiere alquilar:\n')

            for i in range(len(lista)):
                if lista[i][4]==idprop and lista[i][8] == 'en alquiler' :
                    lista[i][8] = estado
                    lista[i][10] = inquilino 
                    lista[i][11] = str(date.today()) #fecha de inicio de alquiler
                    lista[i][12] = str(agregar_años(date.today(), 1)) #fecha de fin de alquiler
                    #print(lista)
                    alquilada = False

            print ('esa propiedad no esta disponible para alquilar')

        return lista

    #alquiler ('Nombre Apellido', 'alquilada', listaa)

    def venta(self, propietario, estado, lista):
        self.propietario = propietario
        self.estado = estado

        vendida = True
        while vendida:
            idprop = input('ingrese el id de la propiedad que quiere comprar:\n')
            
            for i in range(len(lista)):
                if lista[i][4]==idprop and lista[i][8] == 'en venta' :
                    lista[i][10] = lista[i][0]
                    lista[i][0] = propietario
                    lista[i][8] = estado
                    lista[i][12] = str(date.today()) #fecha de venta
                    #print (lista)
                    vendida = False

            print ('esa propiedad no esta disponible para vender')
            
        return lista

    #venta('Nombre Apellido' , 'vendida' , listav)

    def buscarporbarrio(lista):
        final = []
        barrio = input('ingrese el barrio en el que busca una propiedad:\n')
        for i in range(len(lista)):
            if (lista[i][8] == 'en alquiler' or lista[i][8] == 'en venta') and (lista[i][3] == barrio):
                final += [lista[i]]

        print ('las propiedades disponibles en ese barrio son:\n' , final)

        if len(final) == 0:
            print ('no hay propiedades disponibles en ese barrio')

    def buscarporprecio(lista):
        final = []
        min = int(input('ingrese un precio minimo:'))
        max = int(input('ingrese un precio maximo:'))

        for i in range(len(lista)):
            if (lista[i][8] == 'en alquiler' or lista[i][8] == 'en venta') and (int(lista[i][9]) <= max and int(lista[i][9]) >= min):
                final += [lista[i]]

        print ('las propiedades dentro del rango de precios ingresado son:\n' , final)

        if len(final) == 0:
            print ('no hay propiedades que esten dentro del rango ingresado')

    #buscarporprecio(lista)

    def mostrarprop(lista):
        nueva = []
        for i in range(len(lista)):
            if lista[i][8] == 'en alquiler' or lista[i][8] == 'en venta':
                nueva += [lista[i]]
        print (nueva)
       
    def calcular_comision(self, empleado, precio,salario):
        self.empleado = empleado
        self.precio = precio
        self.salario=salario

        if self.estado == 'vendido':
            comision = precio  * 0.05
        elif self.estado=='alquilado':
              comision=precio*0.04
        salarioFinal=salario+comision

        return ('El empleado es',empleado,'su comision es', comision,' y su salario final es',salarioFinal)
    
    def Calcular_precio_m2(self):
        return ('El precio del m2 es',int(self.precio)/int(self.m2))
    
    def Dar_baja(self,id):
        try:
            en_venta=open(r'ListaPropiedadesVenta.txt','r')
            en_alquiler=open(r"ListaPropiedadesAlquiler",'r')
            se_queda_v=""
            se_queda_a=""
            esta=""
            for linea in en_venta:
                if id not in linea:
                    se_queda_v+=(linea)
                else:
                    esta="venta"
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
             print("ha habido un error y no se pudo dar de baja la propiedad")