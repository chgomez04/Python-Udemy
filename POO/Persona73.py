class Persona:
    #pass
    #agregar los atributos de instancia o de objeto
    def __init__(self, nombre, apellido, edad, *args, **kwargs): #tipo dunder(double underscore)
        #pass
        #atributo de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    
    #agregar atributos de clase



    #agreagar metodos de instancia de una clase
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.args} {self.kwargs}')
    def __str__(self):
        pass


print(type(Persona))
persona1 = Persona('Juan', 'Perez', 28, '12345', 2, 3, 5, m='manzana', p='pera')
persona1.mostrar_detalle()

persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrar_detalle()