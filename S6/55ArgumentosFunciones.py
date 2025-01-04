#cuando no sabemos cuantos argumentos va a recibir la funcion se usa una tupla como argumento

def listaNombres(*args): #args=argumentos es una tupla
    for nombre in nombres:
        print(nombre)

listaNombres('Juan', 'Karla', 'Maria', 'Ernesto')
listaNombres('Laura', 'carlos')