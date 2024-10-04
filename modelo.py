import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.conn = None

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='anderson',
                password='12345',
                database='catalogo_avenas'
            )
            if self.conn.is_connected():
                print("Conexión exitosa a la base de datos.")
                return self.conn
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def crear_tablas(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
                            ID_usuario BIGINT PRIMARY KEY,
                            Usuario VARCHAR(255) NOT NULL,
                            Contraseña VARCHAR(255) NOT NULL,
                            Rol VARCHAR(255) NOT NULL);''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS producto (
                            ID_producto BIGINT AUTO_INCREMENT PRIMARY KEY,
                            Nombre VARCHAR(255) NOT NULL,
                            Descripcion VARCHAR(255) NOT NULL,
                            Precio DECIMAL(10, 2) NOT NULL,
                            Cantidad_Stock INT NOT NULL);''')
        self.conn.commit()

    def agregar_usuario(self, id_usuario, usuario, contrasena, rol):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO usuario (ID_usuario, Usuario, Contraseña, Rol) VALUES (%s, %s, %s, %s)', 
                    (id_usuario, usuario, contrasena, rol))
        self.conn.commit()

    def agregar_producto(self, nombre, descripcion, precio, cantidad_stock):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO producto (Nombre, Descripcion, Precio, Cantidad_Stock) VALUES (%s, %s, %s, %s)', 
                    (nombre, descripcion, precio, cantidad_stock))
        self.conn.commit()

    def consultar_productos(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM producto')
        return cursor.fetchall()

    def verificar_usuario(self, usuario, contrasena):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM usuario WHERE Usuario = %s AND Contraseña = %s', (usuario, contrasena))
        return cursor.fetchone()

    def cerrar_conexion(self):
        if self.conn.is_connected():
            self.conn.close()
            print("Conexión cerrada.")
