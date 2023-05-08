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
