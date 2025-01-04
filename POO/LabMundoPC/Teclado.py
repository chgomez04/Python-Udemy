from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contadorTeclados = 0

    @classmethod
    def generar_sgt_valor(cls):
        cls.contadorTeclados +=1
        return cls.contadorTeclados
    
    def __init__(self, marca, tipo_entrada):
        super().__init__(marca, tipo_entrada)
        self._idTeclado = Teclado.generar_sgt_valor()

    def __str__(self):
        return f'Teclado: Id: {self._idTeclado} - {DispositivoEntrada.__str__(self)}'
    


if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    print(teclado1)

    teclado2 = Teclado('Gamer', 'Bluetooth')
    print(teclado2)