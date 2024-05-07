class Funciones_del_Archivo ():
    def __init__ (self, lista):
        self.lista = lista

    def es_primo (self):
        for numero in self.lista:
            self.__es_primo(numero)

    def  __es_primo (self,numero):
        if (numero != 0 and numero != 1):
            divisores = 0
            for j in range(1, numero + 1):
                if numero % j == 0:
                    divisores += 1
                    if divisores >2:
                        return print('El número: ' + str(numero) + ' no es primo')
                        break
            if divisores ==2:
                return print('El número: ' + str(numero) + ' sí es primo')
        else:
            return print('El número: ' + str(numero) + ' no es primo')

    
    def numero_repetido (self):
        mas_repetido = 0
        catidad_repeticiones=0
        for i in self.lista:
            if catidad_repeticiones < self.lista.count(i): 
                catidad_repeticiones = self.lista.count(i) 
                mas_repetido = i
        print ('El número que más se repite es: ' + str(mas_repetido) + ' un total de ' + str (catidad_repeticiones) + ' veces.')


    def convierte_grados(self, origen , destino):
        for i in self.lista:
            self.__convierte_grados(i, origen, destino)

    def __convierte_grados (self, temp, origen , destino):
        if origen == destino:
            print ('La unidad de origen y destino son iguales.')
        
        elif origen == 'Celsius' and origen == 'Farenheit' and origen == 'Kelvin':
            print ('La unidad de origen es incorrecta, ingrese un valor válido: Celsius / Fareheit / Kelvin')
        
        elif destino == 'Celsius' and destino == 'Farenheit' and destino == 'Kelvin':
            print ('La unidad de destino es incorrecta, ingrese un valor válido: Celsius / Fareheit / Kelvin')

        elif origen == 'Celsius': 
            if destino == 'Farenheit':
                resultado = (temp * 9/5) + 32
            elif destino == 'Kelvin':
                resultado = temp + 273.15
        
        elif origen == 'Farenheit':
            if destino == 'Celsius':
                resultado = (temp - 32) * 5/9
            elif destino == 'Kelvin':
                resultado = (temp - 32) * 5/9 + 273.15

        elif origen == 'Kelvin': 
            if destino == 'Farenheit':
                resultado = (temp - 273.15) * 9/5 +32
            elif  destino == 'Celsius':
                resultado = (temp - 273.15)

        print (str(temp) + ' grados ' + origen + ' son equivalentes a: ' + str(round(resultado,2)) + ' grados ' + destino)

    def factorial(self):
        for i in self.lista:    
            print ('El factorial de numero: ' + str(i) + ' es: ' + str(self.__factorial(i)))
    
    def __factorial (self,numero): 
        if type (numero) != int:
            return print ('Ingrese un número entero.')
        elif numero < 0:
            return print ('Ingrese un valor positivo.')
        elif numero <= 1:
            return 1
        else:
            numero = numero * self.__factorial (numero - 1)
            return numero