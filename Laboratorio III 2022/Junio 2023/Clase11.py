# Alumna Yamila Contreras
# 1.1 Método liberarConexion()

@classmethod
def liberarConexion(cls, conexion):
    cls.obtenerPool().putconn(conexion)
    logging.debug(f'Regresamos la conexion del pool: {conexion}')
#  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
#    -------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Marlene Soriano
# 11.4 Pruebas del CursorDelPool -> Parte 1 y 2

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT* FROM persona')
        log.debug(cursor.fetchall())

# Definimos los métodos de clase en persona DAO

#@classmethod
#def seleccionar(cls):
#    with CursorDelPool() as cursor:
#        cursor.execute(cls._SELECCIONAR)
#        registros = cursor.fetchall()
#        personas = [] #creamos una lista
#        for registro in registros:
#            persona = Persona(registro[0], registro[1], registro[2], registro [3])
#            personas.append(persona)
#            return personas

#@classmethod
#def insertar(cls, persona):
#    with CursorDelPool() as cursor:
#        valores = (persona.nombre, persona.apellido, persona.email)
#        cursor.execute(cls._INSERTAR, valores)
#        log.debug(f'Persona Insertada: {persona}')
#        return cursor.rowcount

#@classmethod
#def actualizar(cls, persona):
#    with CursorDelPool() as cursor:
#        valores = (persona.nombre, persona.apellido, persona.email)
#        cursor.execute(cls._ACTUALIZAR, valores)
#        log.debug(f'Persona actualizada: {persona}')
#        return cursor.rowcount 

#@classmethod
#def eliminar(cls, persona):
#    with CursorDelPool() as cursor:
#        valores = (persona.id_persona,)
#        cursor.execute(cls._ELIMINAR, valores)
#        log.debug(f'Los objetos eliminados son: {persona}')
#        return cursor.rowcount

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Alumna: Yamila Belen Contreras

# Pruebas de personaDAO - Parte 1

if __name__ == '__main__':
    # Eliminar un registro
    # persona1 = Persona(id_persona=8)
    # personas_eliminadas = PersonaDAO.eliminar(persona1)
    # log.debug(f'Personas eliminadas: {personas_eliminadas}')

    # Actualizar un registro
    # persona1 = Persona(1, 'Juan José', 'Pena', 'jjpena@mail.com')
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas actualizadas: {personas_actualizadas}')

    #Insetar un registro
    persona1 = Persona(nombre='Marcos', apellido='Tejada', email=tejadam@mail.com)
    personas_insertadas = PersonaDAO.insetar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')

    # Seleccionar objetos
    personas = PersonaDao.seleccionar()
    for persona in personas
        log.debug(persona)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Alumna: Yamila Belen Contreras

# Pruebas de personaDAO - Parte 2

if __name__ == '__main__':
    # Eliminar un registro
    persona1 = Persona(id_persona=18)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')

    # Actualizar un registro
    persona1 = Persona(1, 'Juan', 'Pena', 'jpena@mail.com')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f'Personas actualizadas: {personas_actualizadas}')

    #Insetar un registro
    persona1 = Persona(nombre='Marcos', apellido='Torres', email=tmateo@mail.com)
    personas_insertadas = PersonaDAO.insetar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')

    # Seleccionar objetos
    personas = PersonaDao.seleccionar()
    for persona in personas
        log.debug(persona)
