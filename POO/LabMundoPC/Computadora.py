from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado
from DispositivoEntrada import DispositivoEntrada

class Computadora:

    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras +=1
        self._idComputadoras = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre (self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'''
        {self._nombre} : {self._idComputadoras} 
        {self._monitor}
        {self._teclado}
        {self._raton}
        '''

if __name__ == '__main__':
    monitor1 = Monitor('HP', 16)
    monitor2 = Monitor('Acer', 50)
    teclado1 = Teclado('HP', 'USB')
    teclado2 = Teclado('Acer', 'Bluetooth')
    raton1 = Raton('HP', 'USB')
    raton2 = Raton('Acer', 'Bluetooth')

    compu1 = Computadora('Compu1', monitor1, teclado1, raton1)
    compu2 = Computadora('compu2', monitor2, teclado2, raton2)
    
    print(compu1)
    print(compu2)
