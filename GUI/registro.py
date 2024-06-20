from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

class RegistroWindow():
    def __init__(self):
        self.v = uic.loadUi("Proyectos/P4_POO_DB/GUI/registro.ui")
        self.v.show()