'''
El siguiente codigo en python usa la funcion cuadradolibre(x) (La funcion no se va a importar, sino
que se va a colocar en el codigo para dar evidencia de ella) para crear una funcion probcuadradolibre(N) 
que realiza una simulacion de obtener un numero cuadrado libre en un rango de numeros N.

Parametros de entrada: 
    N: Rango de numeros para hallar cuantos numeros cuadrado libre contiene.
    

Datos de salida: Aproximacion de la probabilidad de obtener un cuadrado libre en un rango
                 de numeros.

Autor: David Felipe Henao
Ultima actualizacion: 13/10/2021
'''
import math

# Esta funcion encuntra si un numero x es cuadrado libre
def cuadradolibre(x): 
 
 #Calculamos la raices de los numeros menores o iguales a x
 for i in range (2, round(math.sqrt(x))): 
    
    #Verificamos que x no sea divisible por un cuadrado
    if x % (i**2) == 0: 
        return 0 
 return 1

#print(cuadradolibre(10))
import random

#Creamos una funcion que calcule la probabilidad de obtener cuadrados libres
def probcuadradolibre(N):
    
    count = 0
    for i in range(1, N+1):
        n = random.randint(1, N)
        
        #Verificamos que el numero elegido al azar sea cuadrado libre
        if cuadradolibre(n) == 1:
            count += 1
    return count/N

print(probcuadradolibre(1000))