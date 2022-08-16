from random import randint
from random import choice
from random import seed
import sys
import sqlite3 as sql


listado = ['Martinez E', 'Romero', 'Otamendi', 'Acunia', 'Montiel', 'Lo Celso', 'Paredes', 'Messi', 'Di Maria', 'Martinez L', 'De Paul', 'Gomez', 'Dybala', 'Correa J', 'Correa A', 'Musso', 'Rulli', 'De Rossi', 'Molina', 'Pezzela', 'Perez ', 'Benedetto', 'Pique', 'De Bruyne', 'Ronaldo', 'Neymar', 'Mbappe', 'Kante', 'Mane', 'Van Dijk', 'Haaland', 'Rojo', 'Busquets', 'Diaz L', 'Suarez', 'Jesus G', 'Rossi A', 'Vinicius Jr', 'Benzema', 'Courtois', 'Modric', 'Veratti', 'Insigne', 'Kroos']

conn = sql.connect("C:\\Users\\Alumno 2022\\Desktop\\Programador\\hogwarts.db")
cursor = conn.cursor()

def copiar_lista():
    """Esta funcion devuelve la lista de alumnos copiada"""
    copia_alumnos = listado.copy()

    return copia_alumnos

def sorteo_casas(copia_alumnos):
    '''Esta devuelve los jugadores en las casas'''
    indice_aleatorio = randint(0, len(copia_alumnos)-1)

    return indice_aleatorio

def seleccionar_alumnos():
    """Esta funcion muestra a que casa ingresa cada alumno"""
    contador = 0
    copia_alumnos = copiar_lista()
    contador_alumnos_gryffindor =  0
    contador_alumnos_ravenclaw =  0
    contador_alumnos_slytherin =  0
    contador_alumnos_hufflepuff =  0

    for x in range(len(copia_alumnos)-1):
        contador += 1
        alumno = copia_alumnos.pop(sorteo_casas(copia_alumnos))

        if contador%4 == 1:
            contador_alumnos_gryffindor +=1
            cursor.execute("INSERT INTO alumnos VALUES(?, ?, ?, ?)",(None, alumno, 18, 1))
            cursor.execute("UPDATE casas SET cantidad_alumnos={}".format(contador_alumnos_gryffindor))
            conn.commit()

        elif contador%4 == 2:
            contador_alumnos_ravenclaw +=1
            cursor.execute("INSERT INTO alumnos VALUES(?, ?, ?, ?)",(None, alumno, 17, 2))
            cursor.execute("UPDATE casas SET cantidad_alumnos={}".format(contador_alumnos_ravenclaw))
            conn.commit()

        elif contador%4 == 3:
            contador_alumnos_slytherin +=1
            cursor.execute("INSERT INTO alumnos VALUES(?, ?, ?, ?)",(None, alumno, 19, 3))
            cursor.execute("UPDATE casas SET cantidad_alumnos={}".format(contador_alumnos_slytherin))
            conn.commit()


        else:
            contador_alumnos_hufflepuff +=1
            cursor.execute("INSERT INTO alumnos VALUES(?, ?, ?, ?)",(None, alumno, 16, 4))
            cursor.execute("UPDATE casas SET cantidad_alumnos={}".format(contador_alumnos_hufflepuff))
            conn.commit()


