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
        
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Contreras, Yamila Belen
# Pruebas ingresando otras clases (Parte 1 y 2)

from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp
opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregrar Película')
        print('2. Lista de Películas')
        print('3. Eliminar Catálogo de Películas')
        print('4. Salir')
        opcion = int(input('Digite una opción de menú (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Digite el nombre de la película: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_peliculas(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()
    except Exception as e:
        print(f'Ocurrió un error de tipo: {e}')
        opcion = None
    else:
        print('Salida del programa')
 
C:\Users\USUARIO\TecnicaturaProgramacion3\Python3\Catalogo\Leccion03\catalogo_peliculas\venv\Scripts\python.exe C:/Users/USUARIO/TecnicaturaProgramacion3/Python3/Catalogo/Leccion03/catalogo_peliculas/test_catalogo_peliculas.py
Opciones: 
1. Agregrar Película
2. Lista de Películas
3. Eliminar Catálogo de Películas
4. Salir
Digite una opción de menú (1-4): 2
--------------Catálogo de películas---------------
Harry Potter y La Piedra Filosofal
Harry Potter y La Cámara de los Secretos
Harry Potter y El Prisionero de Azkaban
Harry Potter y El Cáliz de Fuego
Harry Potter y La Orden del Fénix
Harry Potter y El Príncipe Meztizo
Harry Potter y Las Reliquias de la Muerte Parte 1
Harry Potter y Las Reliquias de la Muerte Parte 2

Salida del programa
Opciones: 
1. Agregrar Película
2. Lista de Películas
3. Eliminar Catálogo de Películas
4. Salir
Digite una opción de menú (1-4): 4
Salida del programa

