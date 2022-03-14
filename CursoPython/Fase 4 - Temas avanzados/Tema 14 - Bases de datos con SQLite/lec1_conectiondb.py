import sqlite3
from sqlite3.dbapi2 import Cursor

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
# cursor.execute("INSERT INTO usuarios VALUES ('Nicholas', 23, 'nicholas@silva.com')")

# cursor.execute("SELECT * FROM usuarios")
            # Un registro
# usuario = cursor.fetchone()

#usuarios = [
#    ('Manuel', 41, "manuel@ejemplo.com"),
#    ('Camil', 23, "camil@ejemplo.com"),
#    ('Tony', 41, "tony@ejemplo.com"),
#]
#cursor.executemany("INSERT INTO usuarios VALUES (?, ?, ?)", usuarios)

cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()

for usuario in usuarios:
    print("Nombre: ", usuario[0], "| Email: ", usuario[2], "| Edad: ", usuario[1])


 # Se confirman los cambios en la base de datos
conexion.commit()

conexion.close()