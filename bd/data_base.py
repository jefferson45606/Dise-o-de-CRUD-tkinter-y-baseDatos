import mysql.connector
from mysql.connector import Error
class b_d:
    def verificar_usuario(username, password):
        b_d.conn = b_d.conectar_db()
        if b_d.conn:
            b_d.cursor = b_d.conn.cursor()
            b_d.cursor.execute('SELECT * FROM usuario WHERE Usuario = %s AND Contraseña = %s', (username, password))
            user = b_d.cursor.fetchone()
            b_d.cursor.close()
            b_d.conn.close()
            return user is not None
        return False

    def agregar_usuario(cedula, username, password, rol):
        b_d.cursor.execute('INSERT INTO usuario (ID_usuario, Usuario, Contraseña, Rol) VALUES (%s, %s, %s, %s)', (cedula, username, password, rol))
        
    def registrar_usuario_gui(cedula,username,password,rol):
        if cedula and username and password and rol:
            b_d.conn = b_d.conectar_db()
            if b_d.conn:
                b_d.cursor = b_d.conn.b_d.cursor()
                try:
                    b_d.agregar_usuario(cedula, username, password, rol)
                    b_d.conn.commit()
                    return "usuario registrado"
                except mysql.connector.Error as e:
                    return "ya registrado"
                finally:
                    b_d.cursor.close()
                    b_d.conn.close()
        else:
            return "llena campos"

    #----------------------avenas-------------------------------------------
    def agregar_avena(codigo, nombre, descripcion, precio, stock):
        if codigo and nombre and descripcion and precio and stock:
            b_d.conn = b_d.conectar_db()
            if b_d.conn:
                b_d.cursor = b_d.conn.b_d.cursor()
                b_d.cursor.execute('INSERT INTO producto (ID_producto, Nombre, Descripcion, Precio, Cantidad_Stock) VALUES (%s, %s, %s, %s, %s)', (codigo, nombre, descripcion, precio, stock))
                b_d.conn.commit()
                b_d.cursor.close()
                b_d.conn.close()
    #------------------conectar al server------------------------------------------------
            
    def conectar_db():
        try:
            b_d.conn = mysql.connector.connect(
                host='localhost',
                user='anderson',       
                password='12345', 
                database='catalogo_avenas'          
            )
            if b_d.conn.is_b_d.connected():
                print("Conexión exitosa a la base de datos 'catalogo_avenas'")
                return b_d.conn
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None