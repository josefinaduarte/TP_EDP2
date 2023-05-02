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

def crearstring(lista1):
    cadena = ''
    for i in range(len(lista1)):
        j = ','.join(map(str, lista1[i]))
        cadena += j
        cadena += '\n'
    return(cadena)

def escribirinfo (archivo, lista):
    fd= open(archivo, 'w')
    print(lista)
    fd.write(lista)
    fd.close()


def agregar_años(fecha, años):
    try:
        return fecha.replace(year=fecha.year + años)
    except ValueError:
        # si no existe el 29 de febrero, poner el 28:
        return fecha.replace(year=fecha.year + años, dia=28)
    
#armado de listas para propiedades
listaa = extraerInfo('ListaPropiedadesVenta.txt')
listav = extraerInfo('ListaPropiedadesAlquiler.txt')
lista = listaa + listav

if __name__ =='__main__':

    print('Menu: \n 1.Log In \n 2.Registrarse \n 3.Salir')
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
            if correcto==True:
                print('Menu: 1.Ver propiedades en alquiler \n 2.Ver propiedades en la venta \n 3.Buscar propiedad por barrio \n 4.Buscar propiedad por precio \n 5.Ver mis propiedades \n 6.Agregar una propiedad al sistema \n 7.Quitar una propiedad del sistema \n 8.Salir')
        elif eleccion==2:
            pass
        elif eleccion==3:
            print('Adios!')
            continuar=False
        
            

            
            