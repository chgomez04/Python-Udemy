class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo
    
ancho = int(input('Proporciona el ancho: '))
alto = int(input('Proporciona el alto: '))
profundo = int(input('Proporciona el profundo: '))

cubo1 = Cubo(ancho, alto, profundo)
print(f'Volumen cubo:{cubo1.calcular_volumen()}')