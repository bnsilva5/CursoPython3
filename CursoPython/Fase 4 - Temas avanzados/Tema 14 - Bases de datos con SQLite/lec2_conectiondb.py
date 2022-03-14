import sqlite3

# Claves primarias, campos autoincrementales y claves unicas

# conexion = sqlite3.connect("usuarios.db")
# conexion = sqlite3.connect("productos.db")
conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()


#cursor.execute('''
 #   CREATE TABLE usuarios(
 #       dni VARCHAR(9) PRIMARY KEY,
 #       nombre VARCHAR(100),
 #       edad INTEGER,
 #       email VARCHAR(100)
 #   )
 #   ''')

#usuarios = [
#    ('11111111A', 'Nicholas', 24, 'nicholas@silva.com'),
#    ('22222222B' ,'Manuel', 35, 'manuel@silva.com'),
#    ('33333333C' ,'Camil', 24, 'camil@ortiz.com'),
#    ('44444444D' ,'Tony', 35, 'tony@waste.com')
#]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

#cursor.execute('''
#    CREATE TABLE productos (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        nombre VARCHAR(100) NOT NULL,
#        marca VARCHAR(50) NOT NULL,
#        precio FLOAT NOT NULL
#    )
#''')

#productos = [
#    ('Teclado', 'Redragon', 19.95),
#    ('Mouse', 'Redragon', 17.95)
#]

# cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)

# cursor.execute("SELECT * FROM productos")

# productos = cursor.fetchall()
# for producto in productos:
#    print(producto)

#cursor.execute('''
#    CREATE TABLE usuarios_autoincremental (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        dni VARCHAR(9) UNIQUE,
#        nombre VARCHAR(100),
#        edad INTEGER,
#        email VARCHAR(100)
#    )
#''')

#usuarios = [
#    ('11111111A', 'Nicholas', 24, 'nicholas@silva.com'),
#    ('22222222B' ,'Manuel', 35, 'manuel@silva.com'),
#    ('33333333C' ,'Camil', 24, 'camil@ortiz.com'),
#    ('44444444D' ,'Tony', 35, 'tony@waste.com')
#]

#cursor.executemany("INSERT INTO usuarios_autoincremental VALUES (null, ?, ?, ?, ?)", usuarios)

cursor.execute("INSERT INTO usuarios_autoincremental VALUES (null, '44444444D', 'Mick', 31, 'mick@mars.com')")

conexion.commit()
conexion.close()