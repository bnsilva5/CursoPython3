from tkinter import *

root = Tk()


def top():
    newTop = Toplevel()
    # Mantiene el foco de la ventana hasta que se cierre y devuelve la interacción con la ventana principal el root en este caso.
    newTop.grab_set()
    newTop.focus_set()  # Mantiene el foco cuando se abre la ventana.
    newTop.mainloop()


Button(root, text="toplevel", command=top).pack()


root.mainloop()
