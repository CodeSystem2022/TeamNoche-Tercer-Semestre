#Florencia Pons
#Excepciones

try:
    10/0
except Exception as e:
    print(f'Ocurrió un error: {e}')
    
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Julio Ezequiel Soria
#Manejo de try and exception

resultado = None

try:
    a = int(input('Digite el primer numero: '))
    b = int(input('Digite el segundo numero: ')) 
    resultado = a/b # modificamos
except TypeError as e:
    print(f'1) Ocurrio un error: {e}')

------------------------------------------------------------------------------------------------------------------------------------------------------------


#Suarez, Carlos Hernan
#1.5 Bloques else y finally al manejar excepciones

try:
    a = int(input('Digite el primer numero: '))
    b = int(input('Digite el segundo numero: '))
    resultado = a / b # modificamos
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {type(e)}')
else :
    print('No se arrojo ninguna excepcion')
finally: #Siempre se va a ejecutar
    print('Ejecucion de este bloque finally')
    
print(f'El resultado es: {resultado}')
print('Seguimos...')

------------------------------------------------------------------------------------------------------------------------------------------------------------

#Suarez, Carlos Hernan
#1.6 Creación de clases de Exception personalizadas

class NumerosIgualesException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        
        
from NumerosIgualesException import NumerosIgualesException

try:
    a = int(input('Digite el primer numero: '))
    b = int(input('Digite el segundo numero: '))

    if a == b:
        raise NumerosIgualesException('Son numeros iguales')

    resultado = a / b  # Modificamos

except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {type(e)}')
else:
    print('No se arrojó ninguna excepción')
finally:
    print('Ejecución de este bloque finally')
    
print(f'El resultado es: {resultado}')
print('Seguimos...')


------------------------------------------------------------------------------------------------------------------------------------------------------------

#Suarez, Carlos Hernan
#1.4 Más de procedimientos de excepciones

resultado = None

try:
    a = int(input('Digite el primer numero: '))
    b = int(input('Digite el segundo numero: '))
    resultado = a / b  # Modificamos
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {type(e)}')

print(f'El resultado es: {resultado}')
print('Seguimos...')


------------------------------------------------------------------------------------------------------------------------------------------------------------

#Suarez, Carlos Hernan
#1.3 Procesar clases de exception más específicas

resultado = None
a = 7
b = 0

try:
    resultado = a / b  # modificamos
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {type(e)}')

print(f'El resultado es: {resultado}')
print('Seguimos...')

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Contreras, Yamila Belen
#Creación de clases Exception personalizadas

from NumerosIgualesException import NumerosIgualesException

resultado = None

try:
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))
    if a == b:
        raise NumerosIgualesException('Son números iguales')
    resultado = a / b # modificamos
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {type(e)}')
else:
    print('No arrojó ninguna excepción')
finally: # Siempre se va a ejecutar
    print('Ejecución de este bloque finally')

print(f'El resultado es: {resultado}')
print('seguimos...')

class NumerosIgualesException(Exception): #Extiende de la clase
    def __instancecheck__(self, mensaje):
        self.message = mensaje
