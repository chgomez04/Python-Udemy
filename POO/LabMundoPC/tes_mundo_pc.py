from Monitor import Monitor
from Computadora import Computadora
from orden import Orden
from Raton import Raton
from Teclado import Teclado


monitor1 = Monitor('HP', 16)
monitor2 = Monitor('Acer', 50)
teclado1 = Teclado('HP', 'USB')
teclado2 = Teclado('Acer', 'Bluetooth')
raton1 = Raton('HP', 'USB')
raton2 = Raton('Acer', 'Bluetooth')

teclado3 = Teclado('Gamer', 'Bluetooth')
raton3 = Raton('Gamer', 'Bluetooth')
monitor3 = Monitor('Gamer', 34)


compu1 = Computadora('Compu1', monitor1, teclado1, raton1)
compu2 = Computadora('compu2', monitor2, teclado2, raton2)
compu3 = Computadora('compu3', monitor3, teclado3, raton3)

computadora = [compu1, compu2]

orden1 = Orden(computadora)
print(orden1)
orden1.agregar_computadoras(compu3)
print(orden1)

computadora2 = [compu2, compu3]
orden2 = Orden(computadora2)
print(orden2)