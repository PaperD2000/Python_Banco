import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt6.QtCore import QDate
from data.historial import HistorialData
from data.ciudades import CiudadData
from data.transfer import TransferData
from data.deposito import DepositoData
from model.movimientos import DepositoInter, Transferencia


class MainWindow():
    def __init__(self):
        # Obtener la ruta absoluta del archivo .ui
        ui_path = os.path.join(os.path.dirname(__file__), 'main.ui')
        self.main = uic.loadUi(ui_path)
        self.iniGUI()
        self.main.showMaximized()

    def iniGUI(self):
        self.main.actionRegisTrans.triggered.connect(self.abrirRegistro)
        self.main.actionReporTrans.triggered.connect(self.abrirDeposito)
        self.main.actionHistorialTrans.triggered.connect(self.abrirHistorial)
        ui_path2 = os.path.join(os.path.dirname(__file__), 'registro.ui')
        ui_path3 = os.path.join(os.path.dirname(__file__), 'depositos.ui')
        ui_path4 = os.path.join(os.path.dirname(__file__), 'historial.ui')
        self.registro = uic.loadUi(ui_path2)
        self.depositos = uic.loadUi(ui_path3)
        self.historial = uic.loadUi(ui_path4)

    def abrirRegistro(self):
        self.registro.btnRegis.clicked.connect(self.regisTrans)
        self.registro.show()

    def abrirDeposito(self):
        self.depositos.btnRegis.clicked.connect(self.regisDeposito)
        self.depositos.show()
        self.comboCiudades()
    
    def abrirHistorial(self):
        self.historial.btnBuscar.clicked.connect(self.buscar)
        self.historial.tablaHistorial.setColumnWidth(0,20)
        self.historial.tablaHistorial.setColumnWidth(1,250)
        self.historial.tablaHistorial.setColumnWidth(3,225)
        self.historial.tablaHistorial.setColumnWidth(4,190)
        self.historial.show()
        self.llenarTablaHist()
    
##########TRANSFERENCIAS##########

    def regisTrans(self):
        if self.registro.cbDocumento.currentText() == "---------Seleccione una Opción---------":
            mbox = QMessageBox()
            mbox.setText("Debe seleccionar un tipo de documento")
            mbox.exec()
            self.registro.cbDocumento.setFocus()
        elif len(self.registro.txtDoc.text()) < 3:
            mbox = QMessageBox()
            mbox.setText("Debe ingresar un documento valido")
            mbox.exec()
            self.registro.txtDoc.setFocus()
        elif self.registro.cbGiro.currentText() == "---------Seleccione una Opción---------":
            mbox = QMessageBox()
            mbox.setText("Debe seleccionar el motivo")
            mbox.exec()
            self.registro.cbGiro.setFocus()
        elif not self.registro.txtMonto.text().isnumeric():
            mbox = QMessageBox()
            mbox.setText("Debe ingresar un monto valido")
            mbox.exec()
            self.registro.txtMonto.setFocus("0")
            self.registro.txtMonto.setFocus()
        else:
            transferencia = Transferencia(
                tipo=self.registro.cbDocumento.currentText(),
                documento=self.registro.txtDoc.text(),
                giro=self.registro.cbGiro.currentText(),
                monto=float(self.registro.txtMonto.text()),
                internacional=self.registro.checkTInter.isChecked(),
                dolares=self.registro.checkDolar.isChecked()
            )
        objData = TransferData()
        mbox = QMessageBox()
        if objData.registrar(info=transferencia):
            mbox.setText("Transferencia Registrada")
            self.limpiarCamposTrans()
        else:
            mbox.setText("Transferencia NO Registrada")
        mbox.exec()

    def limpiarCamposTrans(self):
        self.registro.cbDocumento.setCurrentIndex(0)
        self.registro.cbGiro.setCurrentIndex(0)
        self.registro.txtDoc.setText("")
        self.registro.txtMonto.setText("0")
        self.registro.checkTInter.setChecked(False)
        self.registro.checkDolar.setChecked(False)
        self.registro.txtDoc.setFocus()

##########DEPOSITOS##########

    def comboCiudades(self):
        obj_ciudad = CiudadData()
        datos = obj_ciudad.listaCiudades()

        for item in datos:
            self.depositos.cbLugar.addItem(item[1])

    def validacionCampos(self)->bool:
        if not self.depositos.txtDoc.text() or not self.depositos.txtPrimerNombre.text() or not self.depositos.txtPrimerApellido.text() or not self.depositos.txtMonto.text() or self.depositos.cbDocumento.currentText() == "---------Seleccione una Opción---------" or self.depositos.cbGiro.currentText() == "---------Seleccione una Opción---------" or self.depositos.cbLugar.currentText() == "---------Seleccione una Opción---------" or self.depositos.cbGenero.currentText() == "---------Seleccione una Opción---------":
            return False
        else:
            return True        
        
    def regisDeposito(self):
        mbox = QMessageBox()
        if not self.validacionCampos():
            mbox.setText("Debe llenar los campos obligatorios (*)")
            mbox.exec()
        elif self.depositos.checkTerminos.isChecked() == False:
            mbox.setText("Debe aceptar los terminos y condiciones")
            mbox.exec()
            self.depositos.checkTerminos.setFocus()
        elif not self.depositos.txtMonto.text().isnumeric() or float(self.depositos.txtMonto.text())<1:
            mbox.setText("El monto debe ser numerico y mayor a $0")
            mbox.exec()
            self.depositos.txtMonto.setFocus()
            self.depositos.txtMonto.setText("0")            
        else:
            fechaNa=self.depositos.txtFecha.date().toPyDate()
            deposito = DepositoInter(
                tipo=self.depositos.cbDocumento.currentText(),
                documento=self.depositos.txtDoc.text(),
                giro=self.depositos.cbGiro.currentText(),
                genero=self.depositos.cbGenero.currentText(),
                lugarN=self.depositos.cbLugar.currentText(),
                monto=float(self.depositos.txtMonto.text()),
                nombre1=self.depositos.txtPrimerNombre.text(),
                nombre2=self.depositos.txtSegundoNombre.text(),
                apellido1=self.depositos.txtPrimerApellido.text(),
                apellido2=self.depositos.txtSegundoApellido.text(),
                terminos=self.depositos.checkTerminos.isChecked(),
                fechaN=fechaNa
            )
            objData = DepositoData()
            if objData.registrar(info=deposito):
                mbox.setText("Deposito Internacional Registrado")
                mbox.exec()
                self.limpiarCamposDep()
            else:
                mbox.setText("Deposito Internacional NO Registrado")
                mbox.exec()

    def limpiarCamposDep(self):
        self.depositos.cbDocumento.setCurrentIndex(0)
        self.depositos.cbGiro.setCurrentIndex(0)
        self.depositos.txtDoc.setText("")
        self.depositos.txtMonto.setText("0")
        self.depositos.checkTerminos.setChecked(False)
        self.depositos.cbGenero.setCurrentIndex(0)
        self.depositos.cbLugar.setCurrentIndex(0)
        self.depositos.txtPrimerNombre.setText("")
        self.depositos.txtSegundoNombre.setText("")
        self.depositos.txtPrimerApellido.setText("")
        self.depositos.txtSegundoApellido.setText("")
        reinicioFecha = QDate(2000,1,1)
        self.depositos.txtFecha.setDate(reinicioFecha)
        self.depositos.txtDoc.setFocus()

 ##########HISTORIAL##########

    def buscar(self):
        hist = HistorialData()
        datos = hist.buscarFecha(self.historial.txtDesde.date().toPyDate(), self.historial.txtHasta.date().toPyDate(), self.historial.cbDocumento.currentText(),self.historial.txtDoc.text())
        nombre = None
        fila = 0
        self.historial.tablaHistorial.setRowCount(len(datos))
        for i in datos:
            self.historial.tablaHistorial.setItem(fila, 0, QTableWidgetItem(str(i[0])))
            if nombre:
                self.historial.tablaHistorial.setItem(fila, 1, QTableWidgetItem(nombre))
            else:
                self.historial.tablaHistorial.setItem(fila, 1, QTableWidgetItem("{} {} {} {}".format(str(i[10]),str(i[11]),str(i[12]),str(i[13]))))
                nombre = "{} {} {} {}".format(str(i[10]),str(i[11]),str(i[12]),str(i[13]))
            if bool(i[7]) == True:
                self.historial.tablaHistorial.setItem(fila, 2, QTableWidgetItem("USD " + str(i[5])))
            else:
                self.historial.tablaHistorial.setItem(fila, 2, QTableWidgetItem(str(i[5])))
            if bool(i[6]) == True:
                self.historial.tablaHistorial.setItem(fila, 3, QTableWidgetItem("Internacional-"+str(i[4])))
            else:
                self.historial.tablaHistorial.setItem(fila, 3, QTableWidgetItem("Nacional-"+str(i[4])))
            self.historial.tablaHistorial.setItem(fila, 4, QTableWidgetItem(str(i[8])))
            if str(i[17]) == 'True':
                self.historial.tablaHistorial.setItem(fila, 5, QTableWidgetItem("SI"))
            else:
                self.historial.tablaHistorial.setItem(fila, 5, QTableWidgetItem("NO"))

            fila=fila+1
    def llenarTablaHist(self):
        pass
