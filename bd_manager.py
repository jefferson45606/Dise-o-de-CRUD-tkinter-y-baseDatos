import mysql.connector

class DBManager:
    def __init__(self):
        # Conectar a la base de datos (usa tus credenciales de MySQL)
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="negocio_avena"
        )
        self.cursor = self.conn.cursor()

    def ejecutar_consulta(self, consulta, datos):
        """Ejecutar una consulta de modificación (INSERT, UPDATE, DELETE)"""
        try:
            self.cursor.execute(consulta, datos)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error ejecutando consulta: {e}")
            return False

    def fetch_all(self, consulta, datos=None):
        """Ejecutar una consulta SELECT y devolver los resultados"""
        try:
            if datos:
                self.cursor.execute(consulta, datos)
            else:
                self.cursor.execute(consulta)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error obteniendo datos: {e}")
            return None

