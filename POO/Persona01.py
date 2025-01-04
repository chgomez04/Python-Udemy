class Persona:
    #pass
    #agregar los atributos de instancia o de objeto
    def __init__(self, nombre, apellido, edad): #tipo dunder(double underscore)
        #pass
        #atributo de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    #agregar atributos de clase



    #agreagar metodos de instancia de una clase
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')
    def __str__(self):
        pass


print(type(Persona))
persona1 = Persona('Juan', 'Perez', 28)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

#utilizando el metodo creado-> este metodo es lo recomendado
persona1.mostrar_detalle()
#OTRA FORMA DE UTILIZAR
Persona.mostrar_detalle(persona1)

##Se puede crear un atributo propio de un objeto
persona1.telefono = 12345
print(persona1.telefono)

persona2 = Persona('Karla', 'Gomez', 30)
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad }')

#Como modificar los valos que ya se le habia asignado
persona2.nombre = 'Carlos'
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad }')
