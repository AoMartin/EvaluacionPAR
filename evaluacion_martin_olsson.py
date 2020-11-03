'''
Usted ha sido contratado para desarrollar una solución que le permita al dpto.
De RRHH obtener de manera ágil el estado de las vacaciones de sus empleados. 

Por cuestiones organizativas la empresa tiene los datos de legajo separados de los datos de vacaciones. 
El sistema deberá :
a - Tener un menú de acciones 
b - Permitir la carga de datos y guardarlos en un archivo csv cuyo nombre será dado por el usuario. 
    Si el archivo ya existe deberá preguntar si se desea modificar o sobreescribirlo. 
    * sólo validar que legajo y total de vacaciones sean números enteros.
c - Dado el número de legajo de un empleado calcular e informar en pantalla los días que le quedan disponibles 
de vacaciones junto con el resto de sus datos. Por ejemplo "Legajo 1 : Laura Estebanez, le restan 11 días de vacaciones" 

Tenga en cuenta que las acciones del menú no tienen un orden en particular.
'''

import csv


def imprimir_menu():
    print("\n-GESTOR DE VACACIONES-")
    print("1 - Cargar Datos de Legajo")
    print("2 - Calcular Vacaciones Disponibles")
    print("3 - Salir")


#guarda los nombres de los archivos generados por el usuario
archivos_generados = []

'''
FUNCIONES PARA EL PUNTO B
'''

#OPCION 1 - Cargar Datos de Legajo
def cargar_datos():
    campos = ['Legajo', 'Apellido', 'Nombre', 'Total Vacaciones']
    empleados_ingresados = []

    #ingresar datos: envia los campos a ingresar, y los indices de cuales deben ser numeros enteros
    empleados_ingresados = ingresar_datos_entrada(campos, [0,3])

    #ingresar nombre archivo: se le pasa la lista de archivos generados, devuelve el nombre y si quiere modificar/sobreescirbir
    nombre_archivo, modo_archivo = ingresar_nombre_archivo(archivos_generados)
    archivos_generados.append(nombre_archivo)

    #guardar
    if modo_archivo=='modificar':
        modo_archivo='a'
    else:    
        modo_archivo='w'

    try:
        with open(nombre_archivo, modo_archivo, newline="") as archivo:
            cargador_archivo = csv.writer(archivo)
            cargador_archivo.writerow(campos)
            cargador_archivo.writerows(empleados_ingresados)
            print(f'-El archivo {nombre_archivo} fue guardado con exito.-')
    except IOError:
        print("Hubo un problema con el archivo")


#funcion usada para que el usuario ingrese los datos de los empleados
def ingresar_datos_entrada(campos, campos_a_validar_enteros):
    continuar = "si"
    datos_entrada = []

    while continuar == "si" or continuar == "" or continuar == "\n":
        empleado = []

        for contador in range(len(campos)):
            #Si el indice del campo esta en la lista de los que hay que validar que sean enteros
            if campos_a_validar_enteros.__contains__(contador):
                #llama a la funcion especial para ingresar y validar numeros enteros
                empleado.append( validar_entrada_enteros(campos[contador]) )
            else:    
                empleado.append(input(f"Ingresar {campos[contador]} del empleado: "))

        datos_entrada.append(empleado)
        continuar = input("Continuar agregando datos? (escriba 'si' o pulse enter para continuar)")
    return datos_entrada


#funcion usada para validar los campos que deben ser numeros enteros
def validar_entrada_enteros(campo):
    valor_correcto = False
    while not valor_correcto:
        try:
            valor_ingresado = int(input(f"Ingresar {campo} del empleado: "))
            valor_correcto = True
        except:
            print("-Por favor ingrese un número entero-")
        
    return valor_ingresado

#funcion para ingresar nombre de archivo y elegir el modo con el que se manipulara
def ingresar_nombre_archivo(archivos_generados):
    nombre_archivo = ""
    opcion = ""

    nombre_archivo = input("Ingrese el nombre del archivo donde desea guardar los datos: ")
    for nombre in archivos_generados:
        if nombre == nombre_archivo:
            print("-Ya existe un archivo con ese nombre-")
            while not opcion == "modificar" or not opcion == "sobreescribir":
                opcion = input("Desea 'modificar' o 'sobreescribir' el archivo? (Ingresar una de las dos palabras que estan marcadas con comillas)")
            
    return nombre_archivo, opcion


'''
FUNCIONES PARA EL PUNTO C:

c - Dado el número de legajo de un empleado calcular e informar en pantalla los días que le quedan disponibles 
de vacaciones junto con el resto de sus datos. Por ejemplo "Legajo 1 : Laura Estebanez, le restan 11 días de vacaciones" 

Tenga en cuenta que las acciones del menú no tienen un orden en particular.
'''

#OPCION 2 - Calcular Vacaciones Disponibles
def calcular_vacaciones():
    #ingresar num legajo: se usa la funcion de validar enteros
    numero_legajo = validar_entrada_enteros("Número de legajo")

    #elegir archivo a usar
    if len(archivos_generados) == 0:
        print("No hay datos de empleados cargados, por favor primero ingrese los datos al sistema.")
        return

    print("Elija el archivo de datos que desea utilizar: ")
    for contador in range(len(archivos_generados)):
        print(f"{contador} - {archivos_generados[contador]}")

    ingreso_valido = False
    while not ingreso_valido:
        archivo_elegido = int(input("Ingrese el numero del archivo a utilizar: "))
        if archivo_elegido > len(archivos_generados) or  archivo_elegido < 0:
            print("-Ingrese un numero valido de los de la lista-")
        else:
            ingreso_valido=True
    
    #mostar vacaciones
