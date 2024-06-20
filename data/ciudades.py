import conec as conexion

class CiudadData():

    def listaCiudades(self):
        self.db = conexion.Conexion().conectar()
        self.cursor = self.db.cursor()
        resul = self.cursor.execute("SELECT * FROM ciudades order by nombre")
        ciudad = resul.fetchall()
        return ciudad