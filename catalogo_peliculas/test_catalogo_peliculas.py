from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp


opcion = None 
while opcion != 4:
    try:
        print('Opciones:')
        print('1- Agregar Pelicula')
        print('2- Listar Peliculas')
        print('3- Eliminar Catalogo Peliculas')
        print('4- Salir')

        opcion = int(input('Escribe tu opcion: '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicual:')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_peliculas(pelicula)

        elif opcion == 2:
            cp.listar_peliculas()

        elif opcion == 3:
            cp.eliminar_peliculas()



    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None 


else:
    print('Salimos del programa...')
