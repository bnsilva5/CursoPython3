from tkinter import filedialog as FileDialog
from tkinter import messagebox as MessageBox
import csv


class ReadFileService:

    file_service = ""

    def getFileService(self):
        return self.file_service

    def setFileService(self, file):
        self.file_service = file

    def readFile(self):
        file = FileDialog.askopenfilename(title="Abrir un fichero", filetypes=(
            ("Fichero de texto plano csv ", "*.csv"),
            ("Fichero de texto plano sql ", "*.sql")))
        if file:
            cont = 0
            try:
                with open(file, newline="\n") as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=";")
                    for indicador in reader:
                        print(indicador['Usuario asignado'])
                        cont += 1
                self.setFileService(file)
                MessageBox.showinfo(
                    "OK", "Archivo {} cargado con {} registros".format(
                        file, cont
                    ))
                print(cont)
                return file
            except KeyError:
                print("Archivo no delimitado por comas")
            except Exception as e:
                print(type(e).__name__)


test = ReadFileService()
test.readFile()
