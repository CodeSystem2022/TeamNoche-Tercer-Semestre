# Franco J. Videla
# 10.1 POOL DE CONEXIONES CON PYTHON Y POSTGRESQL: Parte 1 y 2

from psycopg2 import pool #otra forma de importar el psycopg2
#from logger_base import log
#import sys

class Conexion:
    _DATABASE = 'test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    
    @classmethod
    def obtenerConexion(cls):
        pass

    @classmethod
    def obtenerCursor(cls):
        pass

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool()
                
if __name == '__main__':
    pass
       

#---------------------------------------------------------------------------------------------------

# Alumna Yamila Belen Contreras
# 10.2 Obtener una conexión a partir del Pool: Parte 1

 @classmethod
        def obtenerPool(cls):
            if cls._pool is None:
                try:
                    cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,
                                                          cls._MAX_CON,
                                                          host=cls._HOST,
                                                          user=cls._USERNAME,
                                                          password=cls._PASSWORD,
                                                          port=cls._DB_PORT,
                                                          database=cls._DATABASE)
                    log.debug(f'creación del pool exitosa: {cls._pool}')
                except Exception as e:
                    log.error(f'Ocurrió un error al obtener el pool: {e}')
                    sys.exit()
            else:
                return cls._pool

#---------------------------------------------------------------------------------------------------

# Alumna Yamila Belen Contreras
# 10.2 Obtener una conexión a partir del Pool: Parte 2

@classmethod
        def obtenerConexion(cls):
            conexion = cls.obtenerPool().getconn()
            log.debug(f'Conexión obtenida del pool: {conexion}')
            return conexion

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
