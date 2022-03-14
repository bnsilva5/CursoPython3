from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()

def test():
    # MessageBox.showinfo("Hola!", "Hello_World")
    # MessageBox.showwarning("Alerta!", "seccion solo para administradores.")
    # MessageBox.showerror("Error!", "Ha ocurrido un error inesperado.")
    # resultado = MessageBox.askquestion("Salir!", "¿Esta seguro que desea salir sin guardar?")
    # if resultado == "yes":  # "no"
      #  root.destroy()
    # resultado = MessageBox.askokcancel("Salir!", "¿Sobreescribir el fichero actual?")
    # resultado = MessageBox.askyesno("Salir", "Esta seguro que desea salir sin guardar")
    # if resultado:
        #root.destroy()
    resultado = MessageBox.askretrycancel("Reintentar", "No se puede conectar")
    if resultado:
        root.destroy()

Button(root, text="Clickme", command=test).pack()

# Abajo de todo
root.mainloop()