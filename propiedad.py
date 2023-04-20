
from datetime import *
hoy = date.today()
anio = hoy.year
class Propiedad():
    estados_validos = ['venta', 'alquiler', 'libre']
    def __init__(self,cliente, m2,direccion,numambientes,tipo,anioconstruccion,estado,precio):
        if estado not in Propiedad.estados_validos:
            raise ValueError("el estado no es valido")
        self.cliente=cliente
        self.m2=m2
        self.direccion=direccion
        self.numambientes=numambientes
        self.tipo=tipo
        self.estado=estado
        self.precio=precio
        self.antiguedad=anio-anioconstruccion
    def __str__(self):
        return 'La propiedad tiene{} m2, la direccion es{}, la cantidad de ambientes que tiene es {}, es de tipo {}, se construyo en {} y se encuentra {}'.format(self.m2,self.direccion,self.numambientes,self.tipo,self.fecconstruccio,self.estado)
    def Dar_alta(self):
        propiedades=open("ListaPropiedades.txt",'a')
        atributos=[self.nombre,self.m2,self.direccion,self.numambientes,self.tipo,self.antiguedad,self.estado,self.precio]
        for i in range(len(atributos)):
            if i!=len(atributos)-1:
                propiedades.write(atributos[i])
                propiedades.write('\t')
            else:
                propiedades.write(atributos[i])
                propiedades.write('\n')
        propiedades.close()
    def Actualizar(self):
        campo=input('ingrese campo a actualizar')
        dato=input('ingrese el nuevo dato')
        propiedades=open("ListaPropiedades.txt",'a')
        if campo=='m2':
            self.m2=dato
        elif campo=='direccion':
            self.direccion=dato
        elif campo=='numambientes':
            self.numambientes=dato
        elif campo=='tipo':
            self.tipo=dato
        elif campo=='anioconstruccion':
            self.antiguedad=anio-dato
        elif campo=='estado':
            self.estado=dato
        else:
            print('el campo ingresado no esta registrado')

    def alquiler (self, propietario):
        self.estado = 'alquilado'
        self.propietario = propietario
        self.fecha_alquiler = date.today()
        
    def venta (self, propietario, empleado):
        self.estado = 'vendido'
        self.propietario = propietario
        self.fecha_venta = date.today()
       
    
    def calcular_comision(self, empleado, precio):
        self.empleado = empleado
        self.precio = precio

        if self.estado == 'vendido':
            comision = precio  * 0,05

        return empleado, comision
    
    def Calcular_precio_m2(self):
        return int(self.precio)/int(self.m2)