# Examen 5

Este repositorio contiene dos codigos con las soluciones a los problemas 88 y 89 del taller 4. 

El archivo Probperfecto da la solucion del problema 89. Este contiene una funcion `probperfecto(N)` que realiza una simulacion de obtener un numero perfecto en un rango de numeros *N*.

El archivo CuadradoLibre da solucion al problema 88. Este contiene una funcion `probcuadradolibre(N)` que realiza una simulacion de obtener un numero cuadrado libre en un rango de numeros *N*.

## Problema 89
Se elige al azar un entero <img src="https://latex.codecogs.com/svg.image?n&space;\in&space;\Omega&space;:=&space;\left\{1,&space;2,&space;...,&space;N&space;\right\}" title="n \in \Omega := \left\{1, 2, ..., N \right\}" /> con *N* := 100 y deseamos estudiar el
evento <img src="https://latex.codecogs.com/svg.image?A&space;:=&space;\left\{n~es~un~numero~perfecto\right\}" title="A := \left\{n~es~un~numero~perfecto\right\}" />
1. Utilice la funcion `V(x)` del ejercicio (25) para hallar el valor teorico de *P(A)*.
2. Realice una simulacion para estimar el valor teorico de *P(A*) obtenido en (1).
3. ¿Que ocurre con *P(A)* cuando el espacio muestral Ω cambia y *N* = 1000, *N* = 10 000,
*N* = 1000 000, etc.? (*Sugerencia: utilice el teorema de Kanold*).

Primero al utilizar la funcion `V(x)` se obtuvo que el valor teorico <img src="https://latex.codecogs.com/svg.image?P(A)&space;=&space;0.002" title="P(A) = 0.002" /> cuando *N* = 100, este resultado era de esperarse pues entre los primeros 100 numeros naturales solo hay dos numeros perfectos, el 6 y el 28.

Al realizar la simulacion con la funcion `probperfecto(100)` se obtuvo como resultado 0.03, valor muy cercano al valor real.

Por ultimo al realizar la simulacion con *N* = 100, *N* = 1000 y *N* = 10000 se obtuvo los resultados 0.01, 0.005, 0.0004 respectivamente. Se concluye que cuando *N* se hace grande *P(A)* disminuye, tal y como
lo demostro *Kanold* <img src="https://latex.codecogs.com/svg.image?\displaystyle&space;\lim_{x&space;\to&space;\infty}\frac{V(x)}{x}=0" title="\displaystyle \lim_{x \to \infty}\frac{V(x)}{x}=0" />, esto se debe a que los numeros perfectos escalan de manera abismal y cada vez son mas escasos. 

## Problema 88
Un teorema afirma que la probabilidad de que un entero elegido al azar sea libre de cuadrados es: <img src="https://latex.codecogs.com/svg.image?\frac{6}{\pi^{2}}" title="\frac{6}{\pi^{2}}" />

Realice una simulacion para estimar el valor teorico de la probabilidad enunciado en el teorema de <img src="https://latex.codecogs.com/svg.image?\frac{6}{\pi^{2}}" title="\frac{6}{\pi^{2}}" />

(*Sugerencia: suponga que los enteros positivos son finitos: 
<img src="https://latex.codecogs.com/svg.image?\mathbb{Z}^{&plus;}=\left\{1,&space;...,&space;N&space;\right\}" title="\mathbb{Z}^{+}=\left\{1, ..., N \right\}" />. 

Al hacer una simulacion con *N* = 100000, se obtuvo como resultado 0.60864. Al compara este valor con <img src="https://latex.codecogs.com/svg.image?\frac{6}{\pi^{2}}" title="\frac{6}{\pi^{2}}" /> se puede observar una diferencia tan pequeña que es despeciabre. Por tanto se concluye que el teorema es cierto.

Al compara con el ejercicio (70), anexado en el repositorio Exmanen-4, se observa un hecho muy interesante, mientras que nuestra probabilidad se aproxima a <img src="https://latex.codecogs.com/svg.image?\frac{6}{\pi^{2}}" title="\frac{6}{\pi^{2}}" />
, la funcion zeta de Riemann se aproxima a <img src="https://latex.codecogs.com/svg.image?\frac{\pi^{2}}{6}" title="\frac{\pi^{2}}{6}" />.
## Autores
* David Felipe Henao Cuervo

