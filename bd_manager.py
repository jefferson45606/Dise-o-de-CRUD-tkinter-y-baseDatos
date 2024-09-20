import mysql.connector

class DBManager:
    def __init__(self, host="localhost", user="root", password="", database="negocio_avena"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None
        self.conectar()

    def conectar(self):
        """Conectar a la base de datos MySQL"""
        self.conexion = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        cursor = self.conexion.cursor()

        # Crear tabla de usuarios en caso de que no exista, osea crear mañana
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                usuario VARCHAR(100) NOT NULL,
                password VARCHAR(100) NOT NULL,
                rol VARCHAR(20) NOT NULL
            )
        ''')

        # la misma vaina
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id_producto INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                descripcion TEXT NOT NULL,
                precio DECIMAL(10, 2) NOT NULL,
                stock INT NOT NULL
            )
        ''')

        self.conexion.commit()

    def cerrar(self):
        """Cerrar la conexión con la base de datos"""
        if self.conexion:
            self.conexion.close()

    def ejecutar_consulta(self, consulta, parametros=()):
        """Ejecutar una consulta con parámetros"""
        cursor = self.conexion.cursor()
        cursor.execute(consulta, parametros)
        self.conexion.commit()
        return cursor

    def fetch_all(self, consulta, parametros=()):
        """Obtener todas las filas de una consulta"""
        cursor = self.conexion.cursor()
        cursor.execute(consulta, parametros)
        return cursor.fetchall()
