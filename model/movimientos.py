class Transferencia():
    def __init__(self, tipo:str, documento:str, giro:float, monto:int, internacional: bool, dolares: bool):
        self.tipo = tipo
        self.documento = documento
        self.giro = giro
        self.monto = monto
        self.internacional = internacional
        self.dolares = dolares

class DepositoInter():
    def __init__(self, tipo:str, documento:str, giro:float, monto:int, nombre1: str, nombre2: str, apellido1:str, apellido2:str, genero:str,fechaN:str, lugarN:str, terminos:bool):
        self.tipo = tipo
        self.documento = documento
        self.giro = giro
        self.monto = monto
        self.internacional = True
        self.dolares = True
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.genero = genero
        self.fechaNacimiento = fechaN
        self.lugarNacimiento = lugarN
        self.terminos = terminos