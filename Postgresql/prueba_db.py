import psycopg2

conexion = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='admin',
    database='test_db',  
    port= '5432',  
    )
#print(conexion)
cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()