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
