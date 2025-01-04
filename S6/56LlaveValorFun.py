#cuando se quiere enviar un diccionario
def listarTerminos(**kwargs): #kwargs=keyword arguments
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')


listarTerminos(IDE='Integrated Developement Environment', PK='Primary key')
listarTerminos(DBMS='Databae Management System')