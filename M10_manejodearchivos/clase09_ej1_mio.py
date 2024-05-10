
#1) Crear un script con el nombre "clase09_ej1.py" que reciba 3 parametros a elección, verificando que sean exactamente esa cantidad, 
#y muestre como salida los parámetros recibidos

import sys

for i in range(0,3): 
    sys.argv.append(input('Ingrese un parámetro cualequiera:'))


print('En total se cargaron '+ str(len(sys.argv)-1))
if len(sys.argv)-1 > 3:
    print('La lista tiene más de 3 elementos. ')
else:
    n=0
    for i in sys.argv:
        if n!=0:
            print(f"El elemento {n} es: {sys.argv[n]}")
            n += 1
