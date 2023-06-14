# Franco J. Videla 
# 8.1 Creacion de la Clase Persona

class Persona:
    def __init__(self, id_persona, nombre, apellido, email):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'Id Persona: {self._id_persona},' \
               f'Nombre: {self._nombre},' \
               f'Apellido: {self._apellido},' \
               f'Email: {self._email}'

        # Metodos getters and setters
        @property
        def id_persona(self):
            return self._id_persona
        
        @id_persona.setter
        def id_persona(self,id_persona):
            self._id_persona = id_persona

        @property
        def nombre(self):
            return self._nombre

        @nombre.setter
        def id_persona(self,nombre):
            self._nombre = nombre

        @property
        def apellido(self):
            return self._apellido

        @apellido.setter
        def apellido(self,apellido):
            self._apellido = apellido

        @property
        def email(self):
            return self._email

        @email.setter
        def email(self,email):
            self._email = email

if __name__ == '__main__':
    persona1 = Persona(1, 'Franco', 'Videla', 'francojvidela@mail.com')
    log.debug(persona1)
    persona2 = Persona(nombre='Marlene', apellido='Soriano', email='marlenesoriano1209@mail.com')
    log.debug(persona2)
    persona1 = Persona(id_persona = 1)
    log.debug(persona1)

#por continuar

#---------------------------------------------------------------------------------------------------------------------------

# Franco J. Videla
# 8.4 Comienzo de la creacion de la Clase PersonaDAO

from capa_datos_persona.Persona import Persona
from capa_datos_persona.conexion import Conexion
from logger_base import log


class PersonaDAO:
    """
    DAO significa: Data Access Object
    CRUD significa:
                  Create -> Insertar
                  Read -> Seleccionar
                  Update -> Actualizar
                  Delete -> Eliminar
    
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'
    """

    # Definimos los metodos de la clase
    @classmethod
    def seleccionar(clase):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(clase._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []  # Creamos una lista
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(clase, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(clase._INSERTAR, valores)
                log.debug(f'Persona Insertada: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(clase, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerConexion() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(clase._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada: {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(clase, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona)
                cursor.execute(clase._ELIMINAR, valores)
                log.debug(f'Los objetos eliminados son: {persona}')
                return cursor.rowcount

#para continuar