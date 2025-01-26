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
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            #######para insertar un solo valor 
            #valores = ('Carlos', 'Lara', 'clara@mail.com')
            #cursor.execute(sentencia, valores)

            #######para insertar varios valores
            valores = (
                ('Marcos', 'Centu', 'mcentu@mail.com'),
                ('Angel', 'Quintana', 'aquintana@mail.com'),
                ('Maria', 'Gonzales', 'mgonzales@mail.com')
            )
            cursor.executemany(sentencia, valores)    

            ####conexion.commit()##commit guarda los cambios en la base de datos pero como al usar with, el commit se ejecuta en automatico, asi que no hay que colocarlo
            registros_insertados = cursor.rowcount## nos da cuatos registros se han insertado
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close()