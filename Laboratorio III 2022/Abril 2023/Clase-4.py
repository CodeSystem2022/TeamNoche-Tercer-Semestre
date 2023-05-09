#Florencia Pons
#POSTGRE SQL
#Creamos una base de datos llamada test_bd y creamos la tabla "Persona" dentro de ella
SELECT * FROM public."Persona"
ORDER BY id_persona ASC 

#Realizamos consultas e incorporamos elementos en la tabla
--Consulta informacion seleccionada
--SELECT * FROM "Persona" WHERE id_persona in (1,2,3) 
--Ingresamos un nuevo elemento a la tabla
--INSERT INTO "Persona"(nombre,apellido,email)VALUES ('Susana', 'Lara', 'slara@mail.com') 
--Hacemos la consulta para ver toda la informacion de la tabla
--SELECT * FROM "Persona"

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Soria Ezequiel
# Conexion de db en python y postgresql
import psycopg2 # Importamos el paquete que permite la conexion a la BD

# Es muy importante tener bien los datos tando de la base de dato como usuario e ip.
conexion = psycopg2.connect(
    database = 'test_bd',
    user = 'postgres',
    password = 'Admin',
    host = '127.0.0.1',
    port = '5432'
)

#Creamos el "cursor" que es el encargado de ejecutar las sentencias y las query entre el programa y la db. 
cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()

print(registros)

------------------------------------------------------------------------------------------------------------------------------------------------------------------
