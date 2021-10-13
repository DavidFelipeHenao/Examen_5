'''
El siguiente codigo en python usa las funciones perfecto(x) -que calcula si un numero es perfecto-
y V(x) -que calcula la cantidad de numeros perfectos- (Las funciones no se van a importar, sino
que se va a colocar en el codigo para dar evidencia de ellas) para crear  una funcion 
probperfecto(N) que realiza la simulacion de obtener un numero perfecto en un rango de numeros N.

Parametros de entrada: 
    N: Rango de numeros para hallar cuantos numeros perfectos contiene.
    

Datos de salida: Aproximacion de la probabilidad de obtener un perfectp en un rango de numeros.

Autor: David Felipe Henao
Ultima actualizacion: 13/10/2021
'''

# Esta funcion calcula si un numero es perfecto.
def perfecto(x):
    count = 0
    for i in range(1, x):
        if x % i == 0:
            count += i
    if count == x:
        return 1
    else: 
        return 0

# Esta funcion calcula el numero de numeros perfectos menores o iguales a x
def V(x):
    count = 0
    for i in range(1, x+1):
        if perfecto(i) == 1:
            count += 1
    return count/x

print(V(100))

import random
def probperfecto(N):
    count = 0
    for i in range(1, N+1):
        n = random.randint(1, N)
        if perfecto(n) == 1:
            count += 1
    return count/N

print(probperfecto(100))
print(probperfecto(1000))
print(probperfecto(10000))


    






