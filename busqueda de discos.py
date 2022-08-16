import sqlite3 as sql

conn = sql.connect("C:\\Users\\Alumno 2022\\Desktop\\Programador\\Discos.db")
cursor = conn.cursor()

def main():
    """Funcion principal del programa."""
    print("Bienvenido a la base de datos de discos de musica!")
    print("¿Que desea hacer?")
    print("1- Agregar un disco o mas")
    print("2- Buscar un disco en la base")
    print("3- Ver todos los discos")
    print("4- Eliminar un disco.")

    seleccion_usuario()

def seleccion_usuario():
    """Recibe como parametro la opcion elegida por el usuario y devuelve la funcion que corresponda"""
    opcion_elegida = int(input("Ingrese un numero: "))

    if opcion_elegida == 1:
        agregar_disco()

    elif opcion_elegida == 2:
        buscar_disco()

    elif opcion_elegida == 3:
        mostrar_discos()

    elif opcion_elegida == 4:
        eliminar_disco()

    else:
        print("Ingreso un numero erroneo.")

def agregar_disco():
    """Agrega un disco o mas a la base de datos."""

    nombre = input("Ingrese el nombre del disco: ")
    fecha_lanzamiento = int(input("Ingrese la fecha de lanzamiento: "))
    artista = input("Ingrese el nombre del artista: ")
    duracion = int(input("Ingrese la duracion total del album(minutos): "))
    cantidad_canciones = int(input("Ingrese la cantidad de canciones: "))
    genero = input("Ingrese el/los generos del disco: ")

    cursor.execute("INSERT INTO Discos VALUES(?, ?, ?, ?, ?, ?, ?)",(None, nombre, fecha_lanzamiento, artista, duracion, cantidad_canciones, genero))
    conn.commit()


def buscar_disco():
    """Busca un disco en la base de datos y lo muestra."""
    print("¿Como desea buscar el disco?")
    print("1- Por Artista")
    print("2- Por disco")
    opcion_busqueda_elegida = int(input("Ingrese una opcion: "))

    if opcion_busqueda_elegida == 1:
        artista_elegido = input("Escriba el nombre del artista: ")
        proceso = "SELECT nombre FROM Discos WHERE artista={}".format(artista_elegido)
        cursor.execute(proceso)
        artista = cursor.fetchall()
        print(artista)

    elif opcion_busqueda_elegida == 2:
        disco_elegido = input("Escriba el nombre del disco: ")
        instruccion = "SELECT artista FROM Discos WHERE nombre={}".format (disco_elegido)
        cursor.execute(instruccion)
        disco = cursor.fetchone()
        print(disco)

    else:
        print("No se encontraron resultados.")

def mostrar_discos():
    """Muestra todos los discos de la base de datos."""
    cursor.execute("SELECT nombre FROM Discos")
    datos = cursor.fetchall()
    for disco in datos:
        print(disco[0])

def eliminar_disco():
    """Elimina un disco de la base de datos."""
    nombre_album = input("Nombre el album que desea borrar: ")
    instruccion = "DELETE FROM Discos WHERE nombre={}".format(nombre_album)
    cursor.execute(instruccion)
    conn.commit()









