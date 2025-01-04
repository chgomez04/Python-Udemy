#####Sigue siendo Encapsulamiento###
#Get = obtener/recuperar
#Set = colocar/modificar
#@property = es un decorador y racticamente significa que modifica el comportamiento de nuestro metodo

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre #Para encapsular se pone un guion frente a la variable ej: self._nombre = nombre pero esto de igual forma deja modificar el valor
        self._apellido = apellido #si se pone doble gion no deja mosdificar pero no es recomendable hacer esto
        self._edad = edad
    #####GET###
    @property
    def nombre(self):
        return self._nombre
    
    ###SET###
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    ###para los demas atributos encapsulados
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad (self):
        return self._edad
    
    @edad.setter
    def edad (self, edad):
        self._edad = edad

    
    #agreagar metodos de instancia de una clase
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
    


print(type(Persona))
persona1 = Persona('Juan', 'Perez', 28)
persona1.mostrar_detalle()
print(persona1.nombre)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)
persona1.mostrar_detalle()