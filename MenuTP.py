from ClasePersonaTP import *
from ClaseCliente import *
from ClaseEmpleado import *
from propiedad import *
from funciones import *
from random import *
    
#armado de listas para propiedades
listav = extraerInfo('ListaPropiedadesVenta.txt')
listaa = extraerInfo('ListaPropiedadesAlquiler.txt')

lista = listaa + listav
clientes=extraerInfo(r"DatosClientes.unknown")

lista1 =  [['Scarlett Greenless', '969', '374 Sloan Drive', 'Caballito', '001', '2', 'casa', '2009', 'en alquiler', '4000000', 'Norton McClaren', 'Cecilius Lukas', '10/07/22'], ['pedro', '332', '3 Hoard Terrace', 'Recoleta', '002', '7', 'departamento', '2004', 'en venta', '3000000', 'Scarlett Greenless', 'Cyb Burl', '2023-05-02']]
prop = Propiedad('Scarlett Greenless','332','3 Hoard Terrace', 'Recoleta','002','7','departamento','2004','en venta','3000000',' ','Cyb Burl',' ')


if __name__ =='__main__':

    print('Menu: \n 1.Log In \n 2.Registrarse \n 3.Salir')
    continuar=True
    while continuar:
        eleccion=int(input('Ingrese la opcion del menu a la que desea ingresar: '))
        while eleccion<1 or eleccion>3:
            print('El numero ingresado debe estar entre el 1 y el 3.')
            eleccion=int(input('Ingrese la opcion del menu a la que desea ingresar: '))
        if eleccion==1:
            correcto=False
            while correcto==False:
                usuario=input('Ingrese su usuario: ')
                contrasenia=input('Ingrese su contrasenia: ') 
                for i in range(len(clientes)):
                    if usuario==clientes[i][3]:
                        if contrasenia==clientes[i][4]:
                            correcto=True
                if correcto==False:
                    print('El usuario o la contrasenia ingresados no son correctos. Ingreselos devuelta.')
            if correcto==True:
                print('Menu: \n 1.Ver propiedades en alquiler \n 2.Ver propiedades en la venta \n 3.Buscar propiedad por barrio \n 4.Buscar propiedad por precio \n 5.Ver todas las propiedades disponibles \n 6.Alquilar una propiedad \n 7. Comprar una propiedad \n 8.Agregar una propiedad al sistema \n 9.Quitar una propiedad del sistema \n 10.Dar de baja Cliente \n 11.Salir')
                eleccion2=int(input('Ingrese un el numero de la opcion a la que desea acceder: '))
                while eleccion2<1 or eleccion2>11:
                    print('El numero ingresado debe estar entre el 1 y el 11.')
                    eleccion2=int(input('Ingrese un el numero de la opcion a la que desea acceder: '))
                if eleccion2==1:
                    print('las propiedades en alquiler son las siguientes:')
                    prop.mostrarprop(listaa)
                    continuar=True
                elif eleccion2==2:
                    print('las propiedades en venta son las siguientes:')
                    prop.mostrarprop(listav)
                    continuar=True
                elif eleccion2==3:
                    prop.buscarporbarrio(lista)
                    continuar=True
                elif eleccion2==4:
                    prop.buscarporprecio(lista)
                    continuar=True
                elif eleccion2==5:
                    print('las propiedades disponibles para alquilar y vender son las siguientes:')
                    prop.mostrarprop(lista)
                    continuar=True
                elif eleccion2==6:
                    prop.alquiler('alquilado', listaa)
                    continuar=True
                elif eleccion2==7:
                    prop.venta('en venta' , listav)
                    continuar=True
                elif eleccion2==8:
                    print("Ha seleccionado ingresar una propiedad.")
                    propietario=input("Ingrese el nombre del propietario: ")
                    m2=input("Ingrese el numero de metros cuadrados de la propiedad: ")
                    while not m2.isdigit():
                        m2=input("El ingreso no es valido. Ingrese el numero de metros cuadrados de la propiedad: ")
                    direccion=input("Ingrese la direccion de la propiedad: ")
                    barrio=input("Ingrese el barrio donde se encuantra la propiedad: ")
                    id=str(randint(000,999))
                    lista_ids=[]
                    for i in range(len(listav)):
                        lista_ids.append(listav[i][4])
                    for j in range(len(listaa)):
                        lista_ids.append(listaa[j][4])
                    while id in lista_ids:
                        id=str(randint(000,999))
                    num_ambientes=input("Ingres el numero de ambientes de la propiedad: ")
                    while not num_ambientes.isdigit():
                        num_ambientes=input("Hubo un error con el numero ingresado, intente nuevamente. Ingres el numero de ambientes de la propiedad: ")
                    tipo=input("Ingrese 1 si la propiedad es un departamento,2 si es una casa, o 3 si es un local comercial: ")
                    while tipo not in "123":
                        tipo=input("Hubo un error con el numero ingresado. Ingrese 1 si la propiedad es un departamento,2 si es una casa, o 3 si es un local comercial: ")
                    if tipo=="1":
                        tipo="departamento"
                    elif tipo=="2":
                        tipo="casa"
                    else:
                        tipo="local"
                    anio_const=input("Ingrese el año de contruccion de la propiedad: ") #Que pasa si no lo conoce?
                    while not anio_const.isdigit():
                        anio_const=input("Hubo un error con el valor ingresado. Ingrese el año de contruccion de la propiedad: ")
                    estado=input("Ingrese 1 si desea poner su popiedad en venta, o 2 si desea ponerla en alquiler: ")#Asumo q no va a estar vendida o alquilada cuando se ingresa
                    while estado not in "12":
                        estado=input("Hubo un error con el valor ingresado. Ingrese 1 si desea poner su popiedad en venta, o 2 si desea ponerla en alquiler: ")
                    if estado=="1":
                        estado="en venta"
                        actividad="vender"
                    else:
                        estado="en alquiler"
                        actividad="alquilar"
                    precio=input("Ingrese el monto en dolares al cual desea {} la propiedad: ".format(actividad))
                    while not precio.isdigit():
                        precio=input("Hubo un error con el monto ingresado. Ingrese el monto en dolares al cual desea {} la propiedad: ".format(actividad))
                    inquilino=" "
                    fechainicio=" "
                    fechafin=" "
                    propiedad_nueva=Propiedad(propietario,m2,direccion,barrio,id,num_ambientes,tipo,anio_const,estado,precio,inquilino,fechainicio,fechafin)
                    propiedad_nueva.Dar_alta()
                    continuar=True
                elif eleccion2==9:
                    print("Ha seleccionado eliminar una propiedad del sistema.")
                    id=input("Ingrese el id de la propiedad que desea eliminar: ")
                    for i in range(len(lista)):
                        if lista[i][4]==id:
                            cliente=lista[i][0]
                            m2=lista[i][1]
                            direccion=lista[i][2]
                            barrio=lista[i][3]
                            id=lista[i][4]
                            num_ambientes=lista[i][5]
                            tipo=lista[i][6]
                            anio_const=lista[i][7]
                            estado=lista[i][8]
                            precio=lista[i][9]
                            inquilino=lista[i][10]
                            fechainicio=lista[i][11]
                            fechafin=lista[i][12]
                            prop=Propiedad(cliente,m2,direccion,barrio,id,num_ambientes,tipo,anio_const,estado,precio,inquilino,fechainicio,fechafin)
                            prop.Dar_baja(id)
                    continuar=True
                elif eleccion2==10:
                    print("Ha seleccionado eliminar un cliente del sistema.")
                    dni=input("Ingrese el dni del cliente que desea eliminar: ")
                    for i in range(len(clientes)):
                        if clientes[i][1]==dni:
                            nombre=clientes[i][0]
                            dni=clientes[i][1]
                            genero=clientes[i][2]
                            usuario=clientes[i][3]
                            contrasenia=clientes[i][4]
                            telefono=clientes[i][5]
                            direccion=clientes[i][6]
                            anio_ingreso=clientes[i][7]
                            email=clientes[i][8]
                            cli=Cliente(nombre,dni,genero,usuario,contrasenia,telefono,direccion,anio_ingreso,email)
                            cli.Dar_baja(dni)
                    continuar=True
                else:
                    print('Adios')
                    continuar=False
        elif eleccion==2:
            print("Ha seleccionado registrarse")
            nuevo_usuario=input("Ingrese un nombre de usuario") 
            for i in range(len(clientes)):
                if clientes[i][3]==nuevo_usuario:
                    nuevo_usuario=input("El usuario ya existe, ingrese otro:")
            contrasenia=input("Ingrese una contraseña: ")
            nombre=input("Ingrese su nombre completo: ")
            dni=input("Ingrese su numero de DNI")
            while not dni.isdigit() or len(dni)!=8:
                dni=input("El dni no es valido, ingreselo nuevamente: ")
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
            direccion=input("Ingrese su direccion: ")
            anio_ingreso=anio
            email=input("Ingrese su email:")
            nuevo_cliente=Cliente(nombre,dni,genero,nuevo_usuario,contrasenia,telefono,direccion,anio_ingreso,email)
            nuevo_cliente.Dar_alta()
            continuar=True
        elif eleccion==3:
            print('Adios!')
            continuar=False
        
            

            
            