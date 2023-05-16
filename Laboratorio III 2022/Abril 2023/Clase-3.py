#Florencia Pons
#Creación de la clase pelicula

class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Pelicula: {self._nombre}'

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Soria Julio Ezequiel
#Creacion de la clase CatalogoPeliculas
import os

class CatalogoPeliculas:

    ruta_archivo = 'c:\\Users\ezequiel\Documents\GitHub\Tecnicatura3semestre\Laboratorio3\Python\Leccion03\catalogo_peliculas\peliculas.txt'
    @classmethod
    def agregar_pelicula(cls, nombre, anio, categoria):
        with open(cls.ruta_archivo, 'a', encoding= 'utf8') as archivo:
            archivo.write(f'Titulo: {nombre} / Año: {anio} / Categoria: {categoria} \n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding= 'utf8') as archivo:
            print(f'Catalogo de peliculas'.center(50, '-'))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')
-------------------------------------------------------------------------------------------------------------------------------------------------------------
# ALFREDO MARINO
# test_catalogo_peliculas
opcion = None
while opcion != 4:
    try:
        print('Opciones')
        print('1. Aregrar Pelicula')
        print('2. Lista de peliculas')
        print('3. Eliminar ctatálogo de peliculas')
        print('4. Salir')
        opcion=  int(input('Digite una opción de menú (1-4):'))
        
    except Exception as e:
        print(f'Ocurrió un error de tipo: {e}')
        opcion = None
    else:
        print('Salimos del programa')
