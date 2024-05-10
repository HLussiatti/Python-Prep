# 2) Crear un script con el nombre "clase09_ej2.py2" que reciba como un valor de temperatura en grados centígrados, un valor de humedad y por último si llovio 
#(Con True o False). Y que cada vez que sea invocado, cargue en el archivo provisto "clase09_ej2.csv" una marca de tiempo y esa información.
#Para trabajar con tipos de datos relacionados con la medición del tiempo, como ser fechas, horarios o marcas de tiempo se puede utilizar la clase *datetime*

import datetime
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
tiempo = datetime.datetime.now()
#tiempo = datetime.datetime.timestamp(tiempo)
#tiempo = datetime.datetime.fromtimestamp(tiempo)

sys.argv.append(int(input('Ingrese un valor de temperatura en °C: ')))
sys.argv.append( int(input('Ingrese un porcentaje de humedad: ')))
respuesta = '' 
while respuesta != 'SI' and respuesta != 'NO':    
    respuesta = input('Llovió o no llovio? SI/NO: ')
    if respuesta == 'SI':
        sys.argv.append(True)
    elif respuesta == 'NO':
        sys.argv.append(False)

justMyCode = True
file = open(dir_path + '\\clase09_ej2_mio.csv','a')
print (file)
file.write(str(tiempo)+',')
for n in range(1,4):
    print (str(sys.argv[n]))
    file.write(str(sys.argv[n]))
    if n != 3: file.write (',')
file.write('\n')
file.close()
