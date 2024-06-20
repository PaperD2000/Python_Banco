import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from data.usuario import UsuarioData
from GUI.main import MainWindow
from model.user import Usuario

class Login:
    def __init__(self):
        # Obtener la ruta absoluta del archivo .ui
        ui_path = os.path.join(os.path.dirname(__file__), 'login.ui')
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"El archivo UI no se encuentra en la ruta especificada: {ui_path}")
        self.login = uic.loadUi(ui_path)
        self.iniGUI()
        self.login.login_mensaje.setText("")
        self.login.show()

    def ingresar(self):
        if len(self.login.txt_Usuario.text()) < 2:
            self.login.login_mensaje.setText("Ingrese un usuario valido")
            self.login.txt_Usuario.setFocus()
        elif len(self.login.txt_Contra.text()) < 3:
            self.login.login_mensaje.setText("Ingrese una contraseña valida")
            self.login.txt_Contra.setFocus()
        else:
            self.login.login_mensaje.setText("")
            usu = Usuario(Usuario=self.login.txt_Usuario.text(), Contra=self.login.txt_Contra.text())
            usuData = UsuarioData()
            res = usuData.login(usu)
            if res:
                self.main = MainWindow()
                self.login.hide()
            else:
                self.login.login_mensaje.setText("Datos de acceso incorrectos")

    def iniGUI(self):
        self.login.btn_Acceder.clicked.connect(self.ingresar)
