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
