class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre #Para encapsular se pone un guion frente a la variable ej: self._nombre = nombre pero esto de igual forma deja modificar el valor
        self.__apellido = apellido #si se pone doble gion no deja mosdificar pero no es recomendable hacer esto
        self.edad = edad
    
    #agreagar metodos de instancia de una clase
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.__apellido} {self.edad}')
    


print(type(Persona))
persona1 = Persona('Juan', 'Perez', 28)
persona1.mostrar_detalle()
persona1._nombre = 'Juan Carlos'
persona1.__apellido = 'Gomez'
persona1.mostrar_detalle()

