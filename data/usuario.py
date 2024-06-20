import conec as conexion
from model.user import Usuario

class UsuarioData():
    def __init__(self):
        try:   
            self.db = conexion.Conexion().conectar()
            self.cursor = self.db.cursor() 
            insert = """INSERT INTO usuarios values(
            null,'{}','{}','{}')""".format("Administrador","Admin","Admin123")
            self.cursor.execute(insert)
            self.db.commit()
        except Exception as ex:
            print("Ya se ha creado el usuario Admin",ex)

    def login(self, usuario:Usuario):
        self.db = conexion.Conexion().conectar()
        self.cursor = self.db.cursor()
        resul = self.cursor.execute("SELECT * FROM usuarios WHERE Usuario='{}' AND Contra='{}'".format(usuario.usuario,usuario.contra))
        fila = resul.fetchone()
        if fila:
            usuario = Usuario(Nombre=fila[1], Usuario=[2])
            self.cursor.close()
            self.db.close()
            return usuario
        else:
            self.cursor.close()
            self.db.close()
            return None