import psycopg2

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host= '127.0.0.1',
    port= '5432',
    database= 'test_db' 
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            #####----Para seleccionar todo lo de una tabla
            #sentencia = 'SELECT * FROM persona'
            #####----si solo queremeos recuperar el id y el nombre
            #sentencia = 'SELECT id_persona, nombre FROM persona'
            #####----si solo queremos recuperar un registro de una tabla
            #sentencia =  'SELECT * FROM persona WHERE id_persona = 1'
            
            ######    %s   'PLACEHOLDER o parametro posicional
            #sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            #id_persona = input('Proporcione el valor  id_persona: ')
            #se le pasa el parametro como una tupla por eso se pone una coma cuando solo se encia un parametro y asi convertir en una tupla
            #cursor.execute(sentencia, (id_persona, ))
            #######-----busca solo un registro el fetchone
            #registros = cursor.fetchone()
            #######-----busca todos los registgros el fetchall
            #--------------------------------------
            
            
            #####------ cuando se utiliza IN se especifica varios valores o filas de la tabla o registro
            #sentencia = 'SELECT * FROM persona WHERE id_persona IN (1,2)'
            ####--Para realizar de manera dinamica
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            #llaves_primarias = ((1,2),) #como habiamos dicho, tiene que ser una tupla lo que se pasa
            entrada = input('Proporciona los id\'s a buscar (separado por coma):')
            llaves_primarias = (tuple(entrada.split(',')),) #con split especificamos que vamos a quitar o suprimir la coma

            
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
