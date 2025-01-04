from Persona import Persona


print('Creacion Objetos'.center(30,'-'))
persona1 = Persona('Juan', 'Perez', 28)
persona1.mostrar_detalle()
print(__name__)

print('Eliminar objetos'.center(30, '-'))
del persona1