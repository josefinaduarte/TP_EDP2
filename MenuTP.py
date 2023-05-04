#Importamos las clases que necesitamos para comenzar nuestro programa principal

from ClasePersonaTP import *
from ClaseCliente import *
from ClaseEmpleado import *
from propiedad import *
from funciones import *
from ClaseLista import *
from random import *
    
#Armamos las listas que necesitamos para la implementación de los métodos
listav = extraerInfo('ListaPropiedadesVenta.txt')
listaa = extraerInfo('ListaPropiedadesAlquiler.txt')
lista = listaa + listav
empleados = extraerInfo('DatosEmpleados.txt')
clientes=extraerInfo('DatosClientes.txt')

lista1 =  [['Scarlett Greenless', '969', '374 Sloan Drive', 'Caballito', '001', '2', 'casa', '2009', 'en alquiler', '4000000', 'Norton McClaren', 'Cecilius Lukas', '10/07/22'], ['pedro', '332', '3 Hoard Terrace', 'Recoleta', '002', '7', 'departamento', '2004', 'en venta', '3000000', 'Scarlett Greenless', 'Cyb Burl', '2023-05-02']]
prop = Propiedad('Scarlett Greenless','332','3 Hoard Terrace', 'Recoleta','002','7','departamento','2004','en venta','3000000',' ','Cyb Burl',' ')
pro = Propiedad('Scarlett Greenless',332,'3 Hoard Terrace', 'Recoleta',2,7,'departamento',2004,'en venta',3000000,' ','Cyb Burl',' ')
empl=Empleado('Marlena Skiplorne','44816108','Male','Administrativo','20000','62750','1980','408-722-6688')
emp=Empleado('Marlena Skiplorne',44816108,'Male','Administrativo',20000,62750,1980,'408-722-6688')
cliente=Cliente('Evelyn Tithacott','44116184','Female','mroundg9','df45tg','412-766-0581','56 Doe Crossing Crossing','2000','bbon@youku.com')
client=Cliente('Evelyn Tithacott',44116184,'Female','mroundg9','df45tg','412-766-0581','56 Doe Crossing Crossing',2000,'bbon@youku.com')

#Programa principal:
if __name__ =='__main__':
    continuar=True
    while continuar:
        print('Menu: \n 1.Log In \n 2.Registrarse \n 3.Salir')
        eleccion=int(input('Ingrese la opcion del menu a la que desea ingresar: '))
        while eleccion<1 or eleccion>3:
            print('El numero ingresado debe estar entre el 1 y el 3.')
            eleccion=int(input('Ingrese la opcion del menu a la que desea ingresar: '))
        if eleccion==1:
            correcto=False
            while correcto==False:
                usuario=input('Ingrese su usuario: ')
                contrasenia=input('Ingrese su contraseña: ') 
                for i in range(len(clientes)):
                    if usuario==clientes[i][3]:
                        if contrasenia==clientes[i][4]:
                            correcto=True
                if correcto==False:
                    print('El usuario o la contraseña ingresados no son correctos. Ingreselos devuelta.')
            while correcto==True:
                print('Menu: \n 1.Ver propiedades en alquiler \n 2.Ver propiedades en la venta \n 3.Buscar propiedad por barrio \n 4.Buscar propiedad por precio \n 5.Ver todas las propiedades disponibles \n 6.Alquilar una propiedad \n 7. Comprar una propiedad \n 8.Agregar una propiedad al sistema \n 9.Quitar una propiedad del sistema \n 10.Dar de baja Cliente \n 11.Actualizar Cliente \n 12.Actualizar Empleado \n 13.Actualizar Propiedad \n 14.Conocer nuestros empleados \n 15.Mostrar barrios con propiedades disponibles \n 16.Salir')
                eleccion2=int(input('Ingrese un el numero de la opcion a la que desea acceder: '))
                while eleccion2<1 or eleccion2>14:
                    print('El numero ingresado debe estar entre el 1 y el 14.')
                    eleccion2=int(input('Ingrese un el numero de la opcion a la que desea acceder: '))
                if eleccion2==1:
                    print('Las propiedades en alquiler son las siguientes:')
                    prop.mostrarprop(listaa)
                    correcto, continuar = verificarmenu()
                elif eleccion2==2:
                    print('Las propiedades en venta son las siguientes: ')
                    prop.mostrarprop(listav)
                    correcto, continuar = verificarmenu()
                elif eleccion2==3:
                    prop.buscarporbarrio(lista)
                    correcto, continuar = verificarmenu()
                elif eleccion2==4:
                    prop.buscarporprecio(lista)
                    correcto, continuar = verificarmenu()
                elif eleccion2==5:
                    print('Las propiedades disponibles para alquilar y vender son las siguientes: ')
                    prop.mostrarprop(lista)
                    correcto, continuar = verificarmenu()
                elif eleccion2==6:
                    prop.alquiler('alquilado', listaa)
                    correcto, continuar = verificarmenu()
                elif eleccion2==7:
                    prop.venta('vendido' , listav)
                    correcto, continuar = verificarmenu()
                elif eleccion2==8:
                    prop.Dar_alta(listav,listaa,clientes,empleados)
                    correcto, continuar = verificarmenu()
                elif eleccion2==9:
                    prop.Dar_baja()
                    correcto, continuar = verificarmenu()
                elif eleccion2==10:
                    cliente.Dar_baja()
                    correcto, continuar = verificarmenu()
                elif eleccion2==11:
                    client.Actualizar(listav,listaa,clientes,empleados)
                    correcto, continuar = verificarmenu()
                elif eleccion2==12:
                    emp.Actualizar(listav,listaa,clientes,empleados)
                    correcto, continuar = verificarmenu()
                elif eleccion2==13:
                    pro.Actualizar(listav,listaa,clientes,empleados)
                    correcto, continuar = verificarmenu()
                    
                elif eleccion2 == 14:
                    #Creamos una lista enlazada para mostrar los empleados de la inmobiliaria:
                    list=Lista()
    
                    list.agregarinicio(Nodo(empleados[0][0])) 

                    for i in range(len(empleados)):
                        list.append(Nodo(empleados[i][0]))
                    
                    list.pop(1)
                    print(list)
                    correcto, continuar = verificarmenu()
                    
                elif eleccion2 == 15:
                    #Creamos una lista enlazada para mostrar los barrios que tengan propiedades disponibles:
                    list=Lista()
        
                    if lista[0][2] == 'en alquiler' or lista[0][2] == 'en venta':
                        list.agregarinicio(Nodo(lista[0][1]))
                        
                    for i in range(len(lista)):
                        if lista[i][2] == 'en alquiler' or lista[i][2] == 'en venta':
                            list.append(Nodo(lista[i][1]))
                            
                    list.pop(1)
                    print(list)
                    correcto, continuar = verificarmenu()
                    
                else:
                    print('Adios')
                    correcto=False
                    continuar=False
                    
        elif eleccion==2:
            cliente.Dar_alta(listav,listaa,clientes,empleados)
            correcto, continuar = verificarmenu()
            
        elif eleccion==3:
            print('Adios!')
            continuar=False
        