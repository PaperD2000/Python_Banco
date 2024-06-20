import conec as conexion
from model.movimientos import Transferencia
from datetime import datetime

class TransferData():
    def __init__(self):
        try:
            self.db = conexion.Conexion().conectar()
            self.cursor = self.db.cursor()
            tabla2 = """CREATE TABLE IF NOT EXISTS transferencias(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Tipo TEXT,
            Doc TEXT,
            Motivo TEXT,
            Monto NUMERIC,
            Internacional BOOLEAN,
            Dolares BOOLEAN,
            Verificado BOOLEAN,
            Fecha_registro DATETIME)"""
            self.cursor.execute(tabla2)
            self.db.commit()
            self.cursor.close()
            self.db.close()
            print('Tabla Transfer creada')

        except Exception as ex:
            print('Tabla Transfer OK ',ex)

    def registrar(self, info:Transferencia):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.db = conexion.Conexion().conectar()
        self.cursor = self.db.cursor()
        self.cursor.execute("""
        INSERT INTO transferencias values(null,'{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info.tipo, info.documento, info.giro, info.monto, info.internacional, info.dolares,False,fecha))
        self.db.commit()
        if self.cursor.rowcount == 1:
            return True
        else:
            return False