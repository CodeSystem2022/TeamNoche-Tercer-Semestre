# Alumna Yamila Belen Contreras

# 9.1 Clase PersonaDAO: método seleccionar

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

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Alumna Yamila Belen Contreras

# 9.2 Prueba método seleccionar

