#Si un metodo es abstracto entonces toda la clase se vuelve abstracta
# y con esto se consigue que en la clase hija se realice necesariamente la implementacion de ese metodo
#
#

#ABC = Abastract Base Class
from abc import ABC, abstractclassmethod
class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property 
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        self._alto = alto

    #esta es la manera de realizar una clase abstracta
    #por mas que no tenga una implementacion directa esto obliga 
    #a implementar en la clase hija
    @abstractclassmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]' 
        