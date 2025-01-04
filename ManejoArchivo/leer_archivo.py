archivo = open('C:\\Users\\Administrador\\Desktop\\Programacion\\Python-Udemy\\prueba.txt','r', encoding= 'utf8')
#print(archivo.read())

#leer algunos caracteres que todavia no se ha leido
#print(archivo.read(5))
#print(archivo.read(3))

# leer lineas completas
#print(archivo.readline())
#print(archivo.readline())

#iterar el archivo
#for linea in archivo:
#    print (linea)

#leer totas las lineas(se guarda en una lista)
#print(archivo.readlines())

#acceder a una linea de la lista
#print(archivo.readlines()[0])

#abrimos un nuevo archivo
#a - anexa informacion sin borrar lo que ya contiene
#w - sobre escribe lo que ya tiene

archivo2 = open('copia.txt', 'a', encoding = 'utf8')
archivo2.write(archivo.read())

archivo.close
archivo2.close
