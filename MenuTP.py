
if __name__ =='__main__':

    print('Menu: \n 1.Log In \n 2.Registrarse \n 3.Ver propiedades en alquiler \n 4.Ver propiedades en la venta \n 5.Buscar propiedad por barrio \n 6.Buscar propiedad por precio \n 7.Ver mis propiedades \n 8.Agregar una propiedad al sistema \n 9.Quitar una propiedad del sistema \n 10.Salir')
    continuar=True
    while continuar:
        eleccion=int(input('Ingrese la opcion del menu a la que desea ingresar: '))
        while eleccion<1 or eleccion>7:
            print('El numero ingresado debe estar entre el 1 y el 7.')
            eleccion=int(input('Ingrese la opcion del menu a la que desea ingresar: '))
        if eleccion==1:
            usuario=input('Ingrese su usuario: ')
            contrasenia=input('Ingrese su contrasenia: ') 
            #habria que abrir el archivo de la info de cliente
            