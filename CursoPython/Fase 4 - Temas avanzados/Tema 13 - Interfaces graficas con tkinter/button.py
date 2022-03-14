from tkinter import *

def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()

def resta():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()

def producto():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()

def borrar():
    n1.set("")
    n2.set("")

root = Tk()
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Numero 1").pack()
Entry(root, justify="center", textvariable=n1).pack() # primer numero

Label(root, text="Numero 2").pack()
Entry(root, justify="center", textvariable=n2).pack()
Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disable").pack()
Label(root, text=" ").pack()

Button(root, text="Sumar", command=sumar).pack(side="left")
Button(root, text="Resta", command=resta).pack(side="left")
Button(root, text="Producto", command=producto).pack(side="left")

# Abajo de todo
root.mainloop()