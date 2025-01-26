##Una transaccion puede tener una o mas sentencias que modifique el estado de la base de datos
import psycopg2

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)

try:
    ######como habiamos dicho with ya trae integrado el rollback
    with conexion:
        with conexion.cursor() as cursor:

            #conexion.autocommit = False #Inicia la transaccion # si es False no se actualiza de forma automatica el commit y con True si se actualiza de manera automatica
                                        #si se usa false al final hay que usar conexion.commit() para actualizar
                                        #por defecto viene false
                                        #si se usa with ya trae integrado para actualizar
            cursor = conexion.cursor()
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = ('Alex', 'Rojas', 'arojas@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido= %s, email=%s WHERE id_persona = %s'
            valores = ('Juan', 'Perez', 'jperez@mail.com', 1)
            cursor.execute(sentencia, valores)


            #conexion.commit()#termina la transaccion #actualiza los datos 
            #print('Termina la transaccion, se hizo commit')

except Exception as e:
    #conexion.rollback()#proposito de no realizar ninguna actualizacion o cambio si se presenta un error
    print('Ocurrio un error, se hizo rollback: {e}')
finally:
    conexion.close()

print('Termina la transaccion, se hizo commit')