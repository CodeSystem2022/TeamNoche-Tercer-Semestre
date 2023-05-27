#Florencia Pons
#Creamos un archivo txt e incorporamos información 


try:
    archivo = open('prueba.txt', 'w') # La w es de write que significa escribir
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally: #Siempre se ejecuta
    archivo.close() #Con esto se debe cerrar el archivo
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Soria Julio Ezequiel
# Anexamos informacion y copiamos a otro txt.
archivo2 = open('copia.txt', 'a', encoding= 'utf8') # con la letra A cada vez que se ejecute 
                                                    #el comando se agregara una nueva copia debajo de la anterior.

archivo2 = open('copia.txt', 'w', encoding= 'utf8') # con la letra W no importa cuantas veces se ejecute 
                                                    #el comando solo se copiara una vez

archivo2.write(archivo.read()) # copiamos el archivo 1 en el 2
archivo.close() # Cerramos priomero el archivo a copiar
archivo2.close() # Cerramos la copia

------------------------------------------------------------------------------------------------------------------------------------------------------
#Marino Alfredo
# with => abre el archivo y cierra de manera automática
# Manejo de contexto with: sintaxis simplicada, abre y cierra el archivo

with open('prueba.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())

# No hace falta el try catch ni el finally
# Utiliza diferentes métodos: __enter__ este es el que abre y __exit__ el que cierra

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Contreras, Yamila Belen

# Introducción al manejo de archivos
# Declaramos una variable
try:
    archivo = open('prueba.txt', 'w') # W = write
except Exception as e:
    print(e)
finally: # Siempre se ejecuta
    archivo.close() # Con esto se debe cerrar el archivo
