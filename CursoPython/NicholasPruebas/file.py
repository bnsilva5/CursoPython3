from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox
import csv


class PersonaController:
    file_controller = ""

    def __init__(self):
        self.cargarArchivo()
        self.findPerson()

    def cargarArchivo(self):
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
                    cont += 1
            self.file_controller = file
            MessageBox.showinfo(
                "OK", "Archivo {} cargado con {} registros".format(file, cont))
            return file

    def findPerson(self):
        file = self.file_controller
        list_name = []
        cont = 0
        with open(file, newline="\n") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for indicador in reader:
                print(indicador['Usuario_asignado'])
                # if indicador['Usuario_asignado'] not in list_name:
                # list_name.append(indicador['Usuario_asignado'])
                # cont += 1
        MessageBox.showinfo("OK", "Se cargaron {} usuarios".format(cont))
        return list_name

    def findDate(self):
        date = self.file_controller
        list_date = []
        cont = 0
        with open(date, newline="\n") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for date_create in reader:
                if date_create['Creado'] not in list_date:
                    print(date_create['Creado'][0:2])
                    # list_date.append(date_create[2])
                    cont += 1
        MessageBox.showinfo("OK", "Cargan fechas {}".format(cont))
        return list_date


test = PersonaController()
test.findDate()
