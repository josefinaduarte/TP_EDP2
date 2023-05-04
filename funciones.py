from random import randint

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

def escribirinfo (archivo, contenido):
    fd= open(archivo, 'w')
    print(contenido)
    fd.write(contenido)
    fd.close()

def agregar_años(fecha, años):
    try:
        return fecha.replace(year=fecha.year + años)
    except ValueError:
        # si no existe el 29 de febrero, poner el 28:
        return fecha.replace(year=fecha.year + años, dia=28)
    
def leer_archivo(archivo):
    archivo=open(archivo,'r')
    texto=""
    for linea in archivo:
        texto+=linea
    archivo.close()
    return texto

def verificarmenu():
    opcion = input('Desea volver al menu?\n 1. Si \n 2. No\n')
    while opcion!='1' and opcion!='2':
        print('Porfavor ingrese una opcion valida')
        opcion = input('Desea volver al menu?\n 1. Si \n 2. No\n')
    if opcion == '1':
        correcto=True
        continuar = True
    else:
        correcto=False
        continuar = False
        print('Adios')

    return correcto, continuar

def print_tabla( lista ):
    for fila in lista:
        for dato in fila:
            print(dato, end='\t') 
        print()

def validacionesgrales(campo,dato,listav,listaa,clientes,empleados):
    if campo=='m2':
        while not dato.isdigit():
            dato=input("El ingreso no es valido. Ingrese el numero de metros cuadrados de la propiedad: ")
    if campo=='id':
        lista_ids=[]
        for i in range(len(listav)):
            lista_ids.append(listav[i][4])
        for j in range(len(listaa)):
            lista_ids.append(listaa[j][4])
        while dato in lista_ids:
            dato=str(randint(000,999))
    if campo=='numambientes':
        while not dato.isdigit():
                dato=input("Hubo un error con el numero ingresado, intente nuevamente. Ingres el numero de ambientes de la propiedad: ")
    if campo=='tipo':
        while tipo not in "123":
                tipo=input("Hubo un error con el numero ingresado. Ingrese 1 si la propiedad es un departamento,2 si es una casa, o 3 si es un local comercial: ")
        if tipo=="1":
            tipo="departamento"
        elif tipo=="2":
            tipo="casa"
        else:
            tipo="local"
    if campo=='anionconstruccion':
        while not dato.isdigit():
            dato=input("Hubo un error con el valor ingresado. Ingrese el año de contruccion de la propiedad: ")
    if campo=='estado':
        while dato not in "12":
                dato=input("Hubo un error con el valor ingresado. Ingrese 1 si desea poner su popiedad en venta, o 2 si desea ponerla en alquiler: ")
        if dato=="1":
            dato="en venta"
            actividad="vender"
        else:
            dato="en alquiler"
            actividad="alquilar"
    if campo=='precio':
        while not dato.isdigit():
            dato=input("Hubo un error con el monto ingresado. Ingrese el monto en dolares al cual desea {} la propiedad: ".format(actividad))
    if campo=='DNIempleado':
        lista_dni=[]
        for i in range(len(empleados)):
            lista_dni.append(empleados[i][1])
        while dato in lista_dnis:
            dato=input("Hubo un error con el valor ingresado. Ingrese el dni del empleado: ")
    if campo=='DNIcliente':
        lista_dnis=[]
        for i in range(len(clientes)):
            lista_dnis.append(clientes[i][1])
        while dato in lista_dnis:
            dato=input("Hubo un error con el valor ingresado. Ingrese el dni del cliente: ")
    if campo=='salario':
        while not dato.isdigit():
            dato=input("Hubo un error con el valor ingresado. Ingrese el salario del empleado: ")
    if campo=='legajo':
        while not dato.isdigit():
            dato=input("Hubo un error con el valor ingresado. Ingrese el legajo del empleado: ")
        lista_legajos=[]
        for i in range(len(empleados)):
            lista_dnis.append(empleados[i][1])
        while dato in lista_legajos:
            dato=input("Hubo un error con el valor ingresado. Ingrese el legajo del cliente: ")
    if campo=='anioIngreso':
         while not dato.isdigit():
            dato=input("Hubo un error con el valor ingresado. Ingrese el anio de ingreso: ")
    if campo=='usuario':
        lista_usuarios=[]
        for i in range(len(clientes)):
            lista_dnis.append(clientes[i][5])
        while dato in lista_dnis:
            dato=input("Hubo un error con el valor ingresado. Ingrese el dni del cliente: ")
    return dato