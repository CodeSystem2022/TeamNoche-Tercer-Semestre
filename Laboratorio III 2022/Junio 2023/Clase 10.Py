<<<<<<< HEAD
# Franco J. Videla
# 10.1 POOL DE CONEXIONES CON PYTHON Y POSTGRESQL: Parte 1 y 2

import psycopg2 as bd #otra forma de importar el psycopg2
from logger_base import log
import sys

class Conexion:
    _DATABASE = 'test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    
    @classmethod
    def obtenerConexion(cls):
        pass

    @classmethod
    def obtenerCursor(cls):
        pass

if __name == '__main__':
    pass
       

#---------------------------------------------------------------------------------------------------

# Franco J. Videla
# 10.2 Obtener una conexión a partir del Pool: Parte 1 y 2

#---------------------------------------------------------------------------------------------------

#Marino Alfredo
#Pruebas creando objetos del Pool de conexiones

class Conexion:
    _DATABASE = 'test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    
    
    @classmethod
    def obtenerCursor(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool:{conexion}')
        return conexion 
    
    
    @classmethod
    def obtenerCursor (cls):
        pass
    
    @calssmethd
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool( cls._MIN_CON,
                                                        cls._MAX_CON,
                                                        host = cls._HOST
                                                        user = cls._USERNAME,
                                                        password = cls._PASSWORD,
                                                        port = cls._DB_PORT,
                                                        database = cls._DATABASE)
                log.debug(f'creacion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error (f'Ocurrio un error al obtener el pool:{e}')
                sys.exit()
        else:
            return cls._pool
    
if __name__ =='__main__':
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
>>>>>>> 8db724bf61a1d24e854cbca9ca1aea4e1fe6d6ba
