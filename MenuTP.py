from propiedad import *
from funciones import *
    
#armado de listas para propiedades
listav = extraerInfo('ListaPropiedadesVenta.txt')
listaa = extraerInfo('ListaPropiedadesAlquiler.txt')

lista = listaa + listav

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
            listaArchivo=extraerInfo('/Users/constanzanicoli/Documents/GitHub/TP_EDP2/DatosClientes.unknown')
            correcto=False
            while correcto==False:
                usuario=input('Ingrese su usuario: ')
                contrasenia=input('Ingrese su contrasenia: ') 
                for i in range(len(listaArchivo)):
                    if usuario==listaArchivo[i][3]:
                        if contrasenia==listaArchivo[i][4]:
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
                    continuar=True
                elif eleccion2==9:
                    continuar=True
                elif eleccion2==10:
                    continuar=True
                else:
                    print('Adios')
                    continuar=False
        elif eleccion==2:
            continuar=True
        elif eleccion==3:
            print('Adios!')
            continuar=False
        
            

            
            