#with = con. Esto se conoce como RESOURCE MANAGER O ADMINISTRADOR DE RECURSOS

from ManejoArchivos import ManejoArchivos
#with open('prueba.txt', 'r', encoding = 'utf8') as archivo:
#    print(archivo.read())

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
