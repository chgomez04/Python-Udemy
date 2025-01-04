class Monitor:

    contadorMonitores = 0
    def __init__(self, marca, tamano) -> None:
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamano = tamano

    @property
    def marca (self):
        return self._marca
    
    @marca.setter
    def marca (self, marca):
        self._marca = marca

    
    @property
    def tamano (self):
        return self._tamano
    
    @tamano.setter
    def tamano (self, tamano):
        self._tamano = tamano

    def __str__(self):
        return f'Monitor: Id: {self._idMonitor} - Marca: {self._marca}, Tamano: {self._tamano} pulgadas'
    


if __name__ == "__main__":
    monitor1 = Monitor('HP', 16)
    monitor2 = Monitor('samnsung', 50)
    print(monitor1)
    print(monitor2)