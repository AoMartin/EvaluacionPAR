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


def cargar_datos():
    campos = ['Legajo', 'Apellido', 'Nombre', 'Total Vacaciones']
    lista_empleados = []

    #ingresar datos: envia los campos a ingresar, y los indices de cuales deben ser numeros enteros
    lista_empleados = ingresar_datos_entrada(campos, [0,3])

    #ingresar nombre archivo: se le pasa la lista de archivos generados
    ingresar_nombre_archivo(archivos_generados)

    #guardar


def ingresar_datos_entrada(campos, campos_a_validar_enteros):
    continuar = "si"
    datos_entrada = []

    while continuar == "si" or continuar == "" or continuar == "\n":
        empleado = []

        for campo in campos:
            #Si el indice del campo esta en la lista de los que hay que validar que sean enteros
            if campos_a_validar_enteros.__contains__(campo.index):
                #llama a la funcion especial para ingresar y validar numeros enteros
                empleado.append( validar_entrada_enteros(campo) )
            else:    
                empleado.append(input(f"Ingresar {campo} del empleado: "))

        datos_entrada.append(empleado)
        continuar = input("Continuar agregando datos? (escriba 'si' o pulse enter para continuar)")
    return datos_entrada


def validar_entrada_enteros(campo):
    valor_correcto = False
    while not valor_correcto:
        try:
            valor_ingresado = int(input(f"Ingresar {campo} del empleado: "))
        except:
            print("-Por favor ingrese un número entero-")
        valor_correcto = True
    return valor_ingresado

def ingresar_nombre_archivo():