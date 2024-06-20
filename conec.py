import sqlite3

class Conexion():
    def __init__(self):
        try:
            self.con = sqlite3.connect("banco.db")
            self.cTablas()
        except Exception as ex:
            print(ex)

    def cTablas(self):
        tabla1 = """CREATE TABLE IF NOT EXISTS usuarios(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT,
        Usuario TEXT UNIQUE,
        Contra TEXT)"""
        cur = self.con.cursor()
        cur.execute(tabla1)
        cur.close()

    def conectar(self):
        return self.con