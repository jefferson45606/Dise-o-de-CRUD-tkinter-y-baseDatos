import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

class data_base_base:
    def conectar_db():
        try:
            data_base_base.conn = mysql.connector.connect(
                host='localhost',
                user='anderson',
                password='12345',
                database='catalogo_avenas'
            )
            if data_base_base.conn.is_connected():
                print("Conexión exitosa a la base de datos.")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def crear_tablas():
        data_base_base.cursor = data_base_base.conexion.cursor()
        data_base_base.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuario (
                ID_usuario BIGINT PRIMARY KEY AUTO_INCREMENT,
                Usuario VARCHAR(255) NOT NULL,
                Contraseña VARCHAR(255) NOT NULL,
                Rol VARCHAR(255) NOT NULL
            );
        ''')
        data_base_base.cursor.execute('''
            CREATE TABLE IF NOT EXISTS producto (
                ID_producto BIGINT AUTO_INCREMENT PRIMARY KEY,
                Nombre VARCHAR(255) NOT NULL,
                Descripcion VARCHAR(255) NOT NULL,
                Precio BIGINT NOT NULL,
                Cantidad_Stock BIGINT NOT NULL
            );
        ''')
        data_base_base.conexion.commit()
        data_base_base.cursor.close()

    def agregar_usuario(cursor,cedula, username, password, rol):
        try:
            print("1")
            data_base_base.cursor = data_base_base.conexion.cursor()
            try:
                print("2")
                data_base_base.cursor.execute('INSERT INTO usuario (Cedual, Usuario, Contraseña, Rol) VALUES (%s, %s, %s, %s)', (cedula, username, password, rol))
                resultado = "registro"
            except:
                resultado = "ya registrado"
            print("3")
            data_base_base.conexion.commit()
            print("4")
            data_base_base.cursor.close()
            return resultado
        except:
            return ""

    def verificar_usuario(username, password):
        data_base_base.cursor = data_base_base.conexion.cursor()
        data_base_base.cursor.execute('SELECT * FROM usuario WHERE Usuario = %s AND Contraseña = %s', (username, password))
        data_base_base.user = data_base_base.cursor.fetchone()
        data_base_base.cursor.close()

    def agregar_producto(nombre, descripcion, precio, stock):
        cursor = data_base_base.conexion.cursor()
        cursor.execute('INSERT INTO producto (Nombre, Descripcion, Precio, Cantidad_Stock) VALUES (%s, %s, %s, %s)', (nombre, descripcion, precio, stock))
        data_base_base.conexion.commit()
        cursor.close()

    def consultar_productos():
        data_base_base.cursor = data_base_base.conexion.cursor()
        data_base_base.cursor.execute('SELECT * FROM producto')
        productos = data_base_base.cursor.fetchall()
        data_base_base.cursor.close()
        return productos
