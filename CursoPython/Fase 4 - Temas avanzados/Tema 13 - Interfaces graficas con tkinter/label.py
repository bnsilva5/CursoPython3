from tkinter import *

# Configuracion de la raiz
root = Tk()


# Variables dinamicas
texto = StringVar()
texto.set("Un nuevo texto")

Label(root, text="¡Hello World!").pack(anchor="nw")
label = Label(root, text="¡Otra etiqueta!")
label.pack(anchor="center")
Label(root, text="¡Ultima etiqueta!").pack(anchor="se")

label.config(bg="green", fg="blue", font=("verdana",20))
label.config(textvariable=texto)


imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")


# Finalmente bucle de la aplicacion
root.mainloop()