from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contadorRatones = 0

#    @classmethod
#   def generar_sgt_val (cls):
#        cls.contadorRatones += 1
#       return cls.contadorRatones
    
    def __init__(self, marca, tipoEntrada):
        #DispositivoEntrada.__init__(self, tipoEntrada, marca)
        #self._idRaton = Raton.generar_sgt_val()
        Raton.contadorRatones += 1
        self._idRaton = Raton.contadorRatones
        super().__init__(marca, tipoEntrada)

    def __str__(self) -> str:
        return f'Raton: Id: {self._idRaton} - {DispositivoEntrada.__str__(self)} '
  

if __name__ == '__main__':
    raton1 = Raton('zate', 'usb')
    print(raton1)

    raton2 = Raton('Acer', 'Bluetooth')
    print(raton2)

