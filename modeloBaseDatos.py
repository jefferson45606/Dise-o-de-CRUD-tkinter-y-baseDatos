import sqlite3

class baseDatos:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def ejecutar(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def seleccionar(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def cerrar(self):
        self.connection.close()
