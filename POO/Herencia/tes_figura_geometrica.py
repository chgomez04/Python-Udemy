from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica


#No se puede instanciar una clase abstracta
#figura = FiguraGeometrica()

cuadrado1 = Cuadrado(5, 'rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(f'Calculo del area del cuadrado: {cuadrado1.calcular_area()}' )

#MRO - Method Resolution Order: da el orden en que se va ejecutando las clases
print(Cuadrado.mro())

print(cuadrado1)

rectangulo1 = Rectangulo(3, 8, 'verde')
print(f'Calculo area rectangulo: {rectangulo1.calcular_area()}')
print (rectangulo1)