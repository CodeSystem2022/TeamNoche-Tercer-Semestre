# Marlene Soriano
# Uso de with y funcion fetchone en psycopg2

import psycopg2 #Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' #Placeholder
            id_persona = input('Digite un numero para el id_persona: ')
            cursor.execute(sentencia, (id_persona,)) # Asi ejecutamos la sentencia
            registros = cursor.fetchone() # Recuperamos todos los registros que formaran una lista
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

#-------------------------------------------------------------------------------------------------------------------------------------------

# Franco J. Videla 
# Actualizar o editar un registro en la Base de datos 

import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
                sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
                valores = ('Franco', 'Videla', 'francojvidela@gmail.com', 1) # Es una tupla de tuplas
                cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia
                registros_insertados = cursor.rowcount
                print(f'Los registros insertados son: {registros_insertados}')

except Exception as e:
     print(f'Ocurrio un error: {e}')
finally:
     conexion.close()

#-------------------------------------------------------------------------------------------------------------------------------------------

# Marlene Soriano
# Actualizar o modificar varios registros en BD

import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
                sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
                valores = (('Marlene', 'Soriano', 'marlenesoriano1209@gmail.com', 4), # Es una tupla de tuplas
                          ('Franco', 'Videla', 'francojvidela@gmail.com', 5)) #Es una tupla de tuplas
                cursor.executemany(sentencia, valores) # De esta manera ejecutamos la sentencia
                registros_actualizados = cursor.rowcount
                print(f'Los registros actualizados son: {registros_actualizados}')

except Exception as e:
     print(f'Ocurrio un error: {e}')
finally:
     conexion.close()

#------------------------------------------------------------------------------------------------------------------------------------------

# Marlene Soriano
# Eliminar un registro

import psycopg2

conexion =psycopg2.connect(user='postgres', password="root", host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM persona WHERE id_persona=%s"
            entrada = input("Digite el número de registro a eliminar: ")
            valores = (entrada,) #Es una tupla de valores
            cursor.execute(sentencia,valores) #De esta manera ejecutamos la sentencia
            registros_eliminados = cursor.rowcount
            print(f"Los registros eliminados son: {registros_eliminados}")

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

#------------------------------------------------------------------------------------------------------------------------------------------

# Franco J. Videla
# Eliminar varios registros en Base de Datos

import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Digite los números de registros a eliminar: ')
            valores = (tuple(entrada.split(',')),)  # Es una tupla de valores
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Los registros eliminados son: {registros_eliminados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

#----------------------------------------------------------------------------------------------------------------------------------------  

# Franco J. Videla
# Insertar varios registros en Base de Datos

import psycopg2 # Conexion a postgres
conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database = 'test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)'
            valores = (
                ('Franco', 'Videla', 'francojvidela@gmail.com'),
                ('Marlene', 'Soriano', 'marlenesoriano1209@gmail.com'),
                ('Yamila', 'Contreras', '@gmail.com')
            ) # Es una tupla de tuplas
            cursor.executemany(sentencia, valores) # Así ejecutamos la sentencia
            # conexion.commit() esto se utiliza para guardar los cambios en la base de datos
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

#----------------------------------------------------------------------------------------------------------------------------------------  

# Franco J. Videla
# Funcion fetchall en psycopg2

import psycopg2 #Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' #Placeholder
            entrada = input(f'Digite los id_persona a buscar (separados por coma): ')
            llaves_primarias = (tuple(entrada.split(', ')),)
            cursor.execute(sentencia, llaves_primarias) # De esta manera ejecutamos la sentencia
            registros = cursor.fetchall() # Recuperamos todos los registros que serán una lista
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
    
# -------------------------------------------------------------------------------------------------------------------------------------------------
# Marino Alfredo
# Insertar un registro con psycopg2

import psycopg2 #esto es para conectar con postgresql

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido,email) VALUES (%s,%s,%s)'
            valores = ('Carlos','Lara','clara@gmail.com') #es una tupla
            cursor.execute(sentencia,valores) #De esta manera ejecutamos la sentencia
            #conexion.commit() esto se utiliza para guardar los cambios en la bbdd. Con with no es necesario ponerlo ya lo hace automaticamente
            registros_insertados = cursor.rowcount #ingresar cada columna los valores
            print(f'Los registros insertados son: {registros_insertados}')


except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
    --------------------------------------------------------------------------------------------------------------------------------------------------
    #Bruno Marchetti
    #5.1 Uso de with y psycopg2
    import psycopg2 

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' #Placeholder
            id_persona = input('Digite un número para el id_persona: ')
            cursor.execute(sentencia, (id_persona,)) # De esta manera ejecutamos la sentencia
            registros = cursor.fetchone() #Recuperamos todos los registros que serán una lista
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close(
