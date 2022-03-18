from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox
import csv


class Busqueda:

    file_controller = ""
    persons = ['Nicholas.silva', 'masr.silva', 'bnsr.silva']
    years = ['2020', '2021']
    list_name_date = []

    def cargarArchivo(self):
        file = FileDialog.askopenfilename(title="Abrir un fichero", filetypes=(
            ("Fichero de texto plano csv ", "*.csv"),
            ("Fichero de texto", "*.txt"),
            ("Fichero de texto plano sql ", "*.sql"),
            ("Todos los ficheros", "*.*")))
        if file:
            self.file_controller = file
            MessageBox.showinfo("OK", file)
        return file

    def findPerson(self):
        file = self.file_controller
        search_persons = self.persons
        name_date = self.list_name_date
        with open(file, newline="\n") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for indicador in reader:
                if (indicador['Usuario asignado'] in search_persons):
                    name_date.append(
                        indicador['Usuario asignado'])
        print("Se cargaron usuarios" + "\n")
        print("======================")

    def findDate(self):
        # Busca el mes
        file = self.file_controller
        search_people = self.persons
        year = self.years
        # name_and_date = []
        cont = 0
        with open(file, newline="\n") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for datos in reader:
                if(datos['Usuario asignado'] in search_people
                   and datos['Creado'][6:10] in year):
                    print(datos['Usuario asignado']
                          + " | " + datos['Creado'][6:10])
                    # if date_create['Creado'][0:2] not in name_and_date:
                    # print(date_create['Creado'][0:2])
                    cont += 1
        print("Se cargan {} meses".format(cont))


test = Busqueda()
test.cargarArchivo()
test.findPerson()
test.findDate()
