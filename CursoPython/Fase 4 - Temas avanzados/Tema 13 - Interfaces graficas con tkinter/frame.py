from tkinter import *

root = Tk()

root.title("Hello World")
root.resizable(1,1)
root.iconbitmap('@hola.xbm')

frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")


root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

# Abajo de todo
root.mainloop()