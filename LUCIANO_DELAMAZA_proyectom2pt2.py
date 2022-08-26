#Esta es la segunda parte del proyecto del modulo 2
#Objetivo: Crear un programa que en base a 2 números de entrada, coordenadas,
#identifique en cuál de los 4 cuadrantes se encuentra el punto. 
#El programa debe verificar que ninguna coordenada sea 0.

#Por lo cual, lo primero es definir cuales seran las coordenadas.

x = 0.0
y = 0.0
print("Vamos a ubicar un punto en el plano cartesiano, puedes usar numeros negativos")
x = float(input("Por favor, ingresa el valor de X: "))
y = float(input("Ahora ingresa el valor de Y: "))


if x > 0 and y > 0:
    print("El punto se encuentra en el primer cuadrante del plano")
if x < 0 and y > 0:
    print("El punto se encuentra en el segundo cuadrante del plano")
if x < 0 and y < 0:
    print("El punto se encuentra en el tercer cuadrante del plano")
if x > 0 and y < 0:
    print("El punto se encuentra en el cuarto cuadrante del plano")
if x == 0 and y == 0:
    print("El punto se encuentra en el origen del plano, intenta otra vez")

if x == 0 or y == 0:
    if x != 0: 
        print("El punto se encuentra en el eje X")
    if y != 0:
        print("El punto se encuentra en el eje Y")