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

#Bruno Marchetti
#Procesar clases de exception más específicas


def dividir_numeros(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: División entre cero.")
    except TypeError:
        print("Error: Tipos de datos incompatibles.")
    except Exception as e:
        print("Error:", str(e))
# Ejemplos de entradas que nos ejecutarian las excepciones
print(dividir_numeros(10, 2))  # Resultado: 5.0
print(dividir_numeros(10, 0))  # Resultado: Error: División entre cero.
print(dividir_numeros(10, '2'))  # Resultado: Error: Tipos de datos incompatibles.        
