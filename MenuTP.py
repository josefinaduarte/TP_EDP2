def extraerInfo (archivo):
        listaGen = []
        palabra = ''
        try:
            fd= open(archivo, 'r')
            for linea in fd:
                propiedad = []
                for caracter in linea:
                    if ((caracter != ",") and (caracter != "\n")):
                        palabra += caracter
                    else:
                        propiedad += [palabra]
                        palabra = ''
                listaGen += [propiedad]
            fd.close()
            return listaGen
        except IOError:
            print ('el archivo no fue encontrado')

if __name__ =='__main__':

    print('Menu: \n 1.Log In \n 2.Registrarse \n 3.Ver propiedades en alquiler \n 4.Ver propiedades en la venta \n 5.Buscar propiedad por barrio \n 6.Buscar propiedad por precio \n 7.Ver mis propiedades \n 8.Agregar una propiedad al sistema \n 9.Quitar una propiedad del sistema \n 10.Salir')
    continuar=True
    while continuar:
        eleccion=int(input('Ingrese la opcion del menu a la que desea ingresar: '))
        while eleccion<1 or eleccion>7:
            print('El numero ingresado debe estar entre el 1 y el 7.')
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
        
            

            
            