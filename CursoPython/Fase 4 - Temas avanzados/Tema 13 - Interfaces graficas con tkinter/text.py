from tkinter import *

# Configuracion de la raiz
root = Tk()

texto = Text(root)
texto.pack()
texto.config(width=30, height=10, font=("Consolas",12),
            padx=15, pady=15, selectbackground="red")


# Abajo de todo
root.mainloop()