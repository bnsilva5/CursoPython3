from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox
import csv


class Grafica:
    file_controller = ""

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

    def camposFile(self):
        file = self.file_controller
        list_name = []
        cont = 0
        with open(file, newline="\n") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for indicador in reader:
                print(indicador['Usuario asignado'])
                if indicador['Usuario asignado'] not in list_name:
                    list_name.append(indicador['Usuario asignado'])
                    cont += 1
        MessageBox.showinfo("OK", "Se cargaron {} usuarios".format(cont))
