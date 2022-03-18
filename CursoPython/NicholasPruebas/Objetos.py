from tkinter import filedialog as FileDialog, messagebox
import csv


class PersonaController():

    archivo = ""

    def getArchivo(self):
        return self.archivo

    def setArchivo(self, archivo):
        self.archivo = archivo

    def cargarArchivo():
        file = FileDialog.askopenfilename(title="Abrir un fichero", filetypes=(
            ("Fichero de texto plano csv ", "*.csv"),
            ("Fichero de texto", "*.txt"),
            ("Fichero de texto plano sql ", "*.sql"),
            ("Todos los ficheros", "*.*")))
        if file:
            cont = 0
            with open(file, newline="\n") as csvfile:
                reader = csv.reader(csvfile, delimiter=";")
                for indicador in reader:
                    print(indicador)
                    cont = cont + 1
            messagebox.showinfo(
                "OK", "Archivo {} cargado con {} registros".format(file, cont))
            return file

    def findPerson(file):
        with open(file, newline="\n") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            for indicador in reader:
                print(indicador[3])


test = PersonaController
