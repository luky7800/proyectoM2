#Aqui esta mi segundo proyecto.

## PARTE 1 : LONGITUD DE UNA FRASE ##
#Crear un programa para identificar la longitud de una palabra ingresada. 
#La palabra correcta debe tener entre cuatro y ocho letras

print ("Necesito que me digas una palabra. Esta debe tener entre 4 y 8 letras")
palabra = input("Escribe aqui tu palabra: ") 
print (len(palabra))
if len(palabra) <= 4 :
    print("Tu palabra es correcta, bien hecho")
elif len(palabra) > 8 :
    print ("Sobran letras, tiene " + str(len(palabra)) + " letras") 
elif len(palabra) < 4 :
    print("Hacen falta letras. Solo tiene " + str(len(palabra)) + " letras")
    exit()
