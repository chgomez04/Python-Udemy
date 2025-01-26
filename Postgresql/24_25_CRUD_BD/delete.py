import psycopg2

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            
            #####Para eliminar un solo valor
            #sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            #entrada = input('Proporciona el id_persona a eliminar')
            #valores = (entrada,)# tiene que ser una tupla
            #cursor.execute(sentencia, valores)

            #####Para eliminar varios valores
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id_persona a eliminar(separados por coma): ')
            valores = (tuple(entrada.split(',')),)# tiene que ser una tupla
            cursor.execute(sentencia, valores)
            
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')

except Exception as e:
    print('Ocurrio un error: {e}')
finally:
    conexion.close()