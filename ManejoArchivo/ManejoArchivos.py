class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50,'_'))
        self.nombre = open(self.nombre, 'r', encoding = 'utf8')
        return self.nombre
    
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):##la firma del metodo son los parametros que debemos agregar, de lo contrario marca error
        print('cerramos el recurso'.center(50,'-'))
        if self.nombre:
            self.nombre.close()
