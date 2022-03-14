from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

# Popups avanzados

root = Tk()

def test():
  # color = ColorChooser.askcolor(title="Elige un color")
  # print(color) # rgb / hexadecimal
  #ruta = FileDialog.askopenfilename(title="Abrir un fichero",
      # Validacion de archivos que se pueden subir a la aplicacion
  #  filetypes=(("Fichero de texto", "*.txt"),
  #  ("Archivo plano sql", "*.sql"),
  #  ("Todos los ficheros", "*.*")))
  #print(ruta)   # devuelve una ruta
            # Equivale a open('ruta', 'w')
  fichero = FileDialog.asksaveasfile(title="Guardar Fichero", mode="w", defaultextension=".txt")
  if fichero is not None:
    fichero.write("Hi! Hello_World")
    fichero.close()

Button(root, text="Clickme", command=test).pack()

# Abajo de todo
root.mainloop()