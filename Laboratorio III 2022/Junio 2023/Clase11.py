# Alumna Yamila Contreras
# Método liberarConexion()

@classmethod
def liberarConexion(cls, conexion):
    cls.obtenerPool().putconn(conexion)
    logging.debug(f'Regresamos la conexion del pool: {conexion}')
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
