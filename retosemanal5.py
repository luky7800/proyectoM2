#Reto semanal
#Objetivo: Solicitar año actual y otro año (a eleccion) y desplegar cuanto ha pasado o falta para dichas fechas.

#Aqui pedimos el primer año
añouno = input('Introduce el año actual: ')

if añouno.isnumeric():
    añouno1 = int(añouno)
else:
    print("Ingresaste un dato erroneo, corrobora que haz introducido el año actual")
    exit()
if añouno1 < 2022 :
    print("Esta es una fecha pasada y no el año actual")
elif añouno1 > 2022:
    print("El futuro no esta entre mis capacidades de calculo, intentalo denuevo")

#Ahora pedimos el segundo año
añodos = input("Introduce un segundo año para calcular: ")

if añodos.isnumeric():
    añodos2 = int(añodos)
else:
    print('Ingresa un año')
    exit()
if añodos2 == 0 :
    print("Podrias haberlo calculado tu mismo," " igualmente te dire la respuesta")
if añodos2 > 2022 :
       print("Faltan " + (str(añodos2 - 2022)) + " años para llegar al año que has introducido")
if añodos2 < 2022:
    print("Han pasado " + (str(2022 - añodos2)) + " años desde el año que has introducido")
if añodos2 == 2022:
    print('Has introducido el mismo año que el actual')

#Un pequeño mensaje de despedida 
print("No olvides que el tiempo es relativo, disfruta mucho cada instante que puedas <3")