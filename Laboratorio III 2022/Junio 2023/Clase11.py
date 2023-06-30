# Alumna Yamila Contreras
# 1.1 Método liberarConexion()

@classmethod
def liberarConexion(cls, conexion):
    cls.obtenerPool().putconn(conexion)
    logging.debug(f'Regresamos la conexion del pool: {conexion}')
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Alumna Yamila Contreras

# 1.2 Método cerrarConexiones()

@classmethod
def cerrarConexxiones(cls):
    cls.obtenerPool().closeall()

if __name__ =='__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion2)
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    conexion6 = Conexion.obtenerConexion()
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Alumna Yamila Contreras

#1.3 Creación de la Clase CursorDelPool - Parte 1

from logger_base import log
from  conexion import Conexion


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del método with y __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Alumna Yamila Contreras

#1.3 Creación de la Clase CursorDelPool - Parte 2
   
    def __exit__(self, tipo exception, valor_exception, detalle_exception):
    log.debug('Se ejecuta el método exit')
        if valor_exception:
            self._conexion.rollback()
            log.debug(f'Ocurrió una excepción: {valor_exception}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
