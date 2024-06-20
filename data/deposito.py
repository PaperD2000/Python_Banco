import conec as conexion
from model.movimientos import DepositoInter
from datetime import datetime

class DepositoData():
    def __init__(self):
        try:
            self.db = conexion.Conexion().conectar()
            self.cursor = self.db.cursor()
            tabla3 = """CREATE TABLE IF NOT EXISTS depositos(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Tipo TEXT,
            Doc TEXT,
            Giro TEXT,
            Monto NUMERIC,
            Internacional BOOLEAN,
            Dolares BOOLEAN,
            Fecha_registro DATETIME,
            Fecha_nacimiento DATETIME,
            PrimerNombre TEXT,
            SegundoNombre TEXT,
            PrimerApellido TEXT,
            SegundoApellido TEXT,
            Genero TEXT,
            CiudadNacimiento TEXT,
            Terminos BOOLEAN
            )"""
            self.cursor.execute(tabla3)
            self.db.commit()
            self.cursor.close()
            self.db.close()
            print('Tabla Deposito creada')

        except Exception as ex:
            print('Tabla Deposito OK ',ex)

    def registrar(self, info:DepositoInter):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db = conexion.Conexion().conectar()
        self.cursor = self.db.cursor()
        self.cursor.execute("""
        INSERT INTO depositos values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info.tipo, info.documento, info.giro, info.monto, info.internacional, info.dolares, fecha, info.fechaNacimiento, info.nombre1, info.nombre2, info.apellido1, info.apellido2, info.genero, info.lugarNacimiento, info.terminos))
        self.db.commit()
        if self.cursor.rowcount == 1:
            return True
        else:
            return False