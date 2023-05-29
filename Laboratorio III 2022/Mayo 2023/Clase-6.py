# Franco J. Videla
# Manejo de transacciones con with (auto)

import psycopg2 as bd # Esto es para poder conectarnos a Postgre

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
  with conexion:
    with conexion.cursor() as cursor:
      sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
      valores = ('Franco', 'Videla', 'francojvidela@mail.com')
      cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Federico', 'Perez', 'fedeperez@gmail.com', 1)
    cursor.execute(sentencia, valores)
    
except Exception as e:
    print(f'Ocurrió un error, se hizo un rollback: {e}')
finally:
    conexion.close()
    
    print('Termina la transacción')

#--------------------------------------------------------------------------------------------------------------------------------------------

# Marlene Soriano
# Transacciones

import psycopg2 as bd # Esto es para poder conectarnos a Postgre

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Marlene', 'Soriano', 'marlenesoriano1209@gmail.com')
    cursor.execute(sentencia, valores)
    conexion.commit()  # Realizamos el commit manualmente
    print('Termina la transacción')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo un rollback: {e}')
finally:
    conexion.close()

#-------------------------------------------------------------------------------------------------------------------------------------------

#