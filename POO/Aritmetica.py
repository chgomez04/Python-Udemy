class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc
    """

    def __init__(self, operadorA, operadorB):
        self.operadorA = operadorA
        self.operadorB = operadorB

    def sumar(self):
        return self.operadorA + self.operadorB
    
    def restar(self):
        return self.operadorA - self.operadorB
    
    def multiplicar(self):
        return self.operadorA * self.operadorB
    
    def dividir(self):
        return self.operadorA / self.operadorB
    

aritmetica1 = Aritmetica(5 , 3)
print(f'sumar: {aritmetica1.sumar()}')
print(f'restar: {aritmetica1.restar()}')
print(f'multiplicar: {aritmetica1.multiplicar()}')
print(f'dividir: {aritmetica1.dividir()}')
print(f'dividir: {aritmetica1.dividir():.2f}')