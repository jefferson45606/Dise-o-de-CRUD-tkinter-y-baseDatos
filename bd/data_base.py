import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

class Controlador:
    def __init__(self):
        self.conexion = self.conectar_db()

    def conectar_db(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='jefferson',
                password='12345',
                database='catalogo_avenas'
            )
            if conn.is_connected():
                print("Conexión exitosa a la base de datos.")
                return conn
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def crear_tablas(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario (
                ID_usuario BIGINT PRIMARY KEY AUTO_INCREMENT,
                Usuario VARCHAR(255) NOT NULL,
                Contraseña VARCHAR(255) NOT NULL,
                Rol VARCHAR(255) NOT NULL
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS producto (
                ID_producto BIGINT AUTO_INCREMENT PRIMARY KEY,
                Nombre VARCHAR(255) NOT NULL,
                Descripcion VARCHAR(255) NOT NULL,
                Precio BIGINT NOT NULL,
                Cantidad_Stock BIGINT NOT NULL
            );
        ''')
        self.conexion.commit()
        cursor.close()

    def agregar_usuario(self, cedula, username, password, rol):
        cursor = self.conexion.cursor()
        cursor.execute('INSERT INTO usuario (Cedual, Usuario, Contraseña, Rol) VALUES (%s, %s, %s, %s)', (cedula, username, password, rol))
        self.conexion.commit()
        cursor.close()

    def verificar_usuario(self, username, password):
        cursor = self.conexion.cursor()
        cursor.execute('SELECT * FROM usuario WHERE Usuario = %s AND Contraseña = %s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        return user is not None

    def agregar_producto(self, nombre, descripcion, precio, stock):
        cursor = self.conexion.cursor()
        cursor.execute('INSERT INTO producto (Nombre, Descripcion, Precio, Cantidad_Stock) VALUES (%s, %s, %s, %s)', (nombre, descripcion, precio, stock))
        self.conexion.commit()
        cursor.close()

    def consultar_productos(self):
        cursor = self.conexion.cursor()
        cursor.execute('SELECT * FROM producto')
        productos = cursor.fetchall()
        cursor.close()
        return productos
