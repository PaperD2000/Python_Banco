import conec as conexion

class HistorialData():

    def buscarFecha(self, fechaDesde, fechaHasta,tipo,doc):
        self.db = conexion.Conexion().conectar()
        self.cursor = self.db.cursor()
        sql="""
        SELECT T.Id as Transaccion, D.*, T.Verificado FROM transferencias T 
        INNER JOIN depositos D ON D.Tipo = T.Tipo AND D.Doc = T.Doc
        WHERE T.Fecha_registro >= '{}' and T.Fecha_registro <= '{}' and D.Tipo = '{}' and D.Doc = '{}'
        and T.Motivo = D.Giro and T.Monto = D.Monto
        """.format(fechaDesde,fechaHasta,tipo,doc)
        resul = self.cursor.execute(sql)
        data = resul.fetchall()
        return data