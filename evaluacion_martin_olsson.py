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

