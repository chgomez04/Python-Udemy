##Para aplicar el concepto de Herencia 

class Persona:# Es la clase padre
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    ###SOBREESCRITURA  del metodo str
    def __str__(self):
        return f'Persona[Nombre: {self.nombre}, Edad: {self.edad}]'

class Empleado(Persona):# Empleado es la clase hija y Persona es la clase padre, lo cual Empleado va a heredar de la clase Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) #la forma correcta en la que se debe inicializar una clase padre
        self.sueldo = sueldo

    ###SOBREESCRITURA del metodo str heredado de la clase Persona
    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}'


empleado1 = Empleado('Juan', 28, 5000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)