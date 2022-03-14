import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

        # Consulta
#cursor.execute("SELECT * FROM usuarios_autoincremental WHERE edad=23")
#usuarios = cursor.fetchall()
#print(usuarios)

        # Actualizar / Modificar
# cursor.execute("UPDATE usuarios_autoincremental SET nombre='Brandon', edad=20 WHERE dni='11111111A'")

        # Eliminar un registro
# cursor.execute("DELETE FROM usuarios_autoincremental WHERE dni='11111111A'")

conexion.commit()
conexion.close()