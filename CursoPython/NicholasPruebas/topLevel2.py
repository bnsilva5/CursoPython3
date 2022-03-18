from tkinter import Button, Frame
from tkinter import messagebox as MessageBox
import tkinter


def boton():
    MessageBox.showinfo()


class Application:

    def __init__(self, main_window):
        self.frame1 = main_window
        self.drawFrame()
        self.drawMenu()

    def drawFrame(self):
        self.main_frame = Frame(
            self.frame1, height=300, width=900, bg='dark red'
            ).pack(fill='both', expand=1)

    def drawMenu(self):
        self.menu_persona = Button(
            self.frame1, text="Persona", command=boton
            ).place(relx=.43, rely=.20, relwidth=.15, relheight=.15
                    )


root = tkinter.Tk()
root.title("Niveles")
root.geometry("1000x400")
app = Application(root)
root.mainloop()
