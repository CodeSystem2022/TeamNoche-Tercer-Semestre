# Alumna Yamila Belen Contreras

# 9.1 Clase PersonaDAO: método seleccionar

from capa_datos_persona.Persona import Persona
from capa_datos_persona.conexion import Conexion
from logger_base import log

class PersonaDAO:
    """

    DAO significa: Data Access Object
    Crud significa: Create: Insertar
                    Read: Seleccionar
                    Update: Actualizar
                    Delete: Eliminar
    """
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    # Definimos los métodos de clase
    
  @classmethod
    def seleccionar (cls):
        with Conexion.obtenerConexion():
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Alumna Yamila Belen Contreras

# 9.2 Prueba Método Seleccionar

if __name__== '__main__':
# Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas
        log.debug(persona)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Alumna Yamila Belen Contreras

# 9.3 Método Seleccionar

@classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona Insertada: {persona}')
                return cursor.rowcount

if __name__== '__main__':
    # Insertar un registro
    persona1 = Persona(nombre='Pedro', apellido='Romero', email='promero@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Alumno Suarez, Carlos Hernan

# 9.4 Metodo actualizar


@classmethod
def actualizar(cls, persona):
    with Conexion.obtenerCursor():
        with Conexion.obtenerCursor() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'persona actualizada: {persona}')
            return cursor.rowcount

if __name__ == '__main__':

    # Actualizar un registro
    persona1 = Persona(1, 'Juan Jose', 'Pena', 'jjpena@mail.com')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f'Personas actualizadas: {personas_actualizadas}')

    # Insertar un registro
   # persona1 = Persona(nombre='Omero', apellido='Ramos', email='omeror@mail.com')
   # personas_insertadas = personaDAO.insertar(persona1)
   # log.debug(f'Personas insertadas: {personas_insertadas}')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Alumno Suarez, Carlos Hernan
# 9.5 Método Eliminar

@classmethod
def actualizar(cls, persona):
    with Conexion.obtenerConexion():
        with Conexion.obtenerCursor() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Los objetos eliminados son: {persona}')
            return cursor.rowcount

if __name__ == '__main__':

    #Eliminar un registro
    persona1 = Persona(id_persona=13)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminada: {personas_eliminadas}')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Alumno Suarez, Carlos Hernan
# 9.6 Haciendo pruebas y eliminando errores

                    
if __name__ == '__main__':
    #Eliminar un registro
    #persona1 = Persona(id_persona=13)
    #personas_eliminadas = PersonaDAO.eliminar(persona1)
    #log.debug(f'Personas eliminada: {personas_eliminadas}')

    # Actualizar un registro
    #persona1= Persona(1, 'Juan Jose', 'Pena', 'jjpena@mail.com')
    #personas_actualizadas = PersonaDAO.actualizar(persona1)
    #log.debug(f'Personas actualizadas: {personas_actualizadas}')

    # Insertar un registro
    # persona1 = Persona(nombre='Omero', apellido='Ramos', email='omeror@mail.com')
    # personas_insertadas = personaDAO.insertar(persona1)
    # log.debug(f'Personas insertadas: {personas_insertadas}')

    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
