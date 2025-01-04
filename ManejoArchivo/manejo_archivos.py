try:
    archivo = open('prueba.txt', 'w', encoding='utf8')# 'w' = sirve para escribir y utf8 = soporta caracteres como acento
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)

finally:
    archivo.close()
    print('fin del archivo')
    #archivo.write('nueva info')