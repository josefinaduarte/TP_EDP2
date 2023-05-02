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