import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

def conectar_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='jefferson',       
            password='2005', 
            database='catalogo_avenas'          
        )
        if conn.is_connected():
            print("Conexión exitosa a la base de datos 'catalogo_avenas'")
            return conn
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def crear_tablas(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario (
            ID_usuario BIGINT PRIMARY KEY,
            Usuario VARCHAR(255) NOT NULL,
            Contraseña INT(50) NOT NULL,
            Rol VARCHAR(255) NOT NULL
        );
    ''')
    print("Tabla 'usuario' creada o ya existe.")
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS producto (
            ID_producto BIGINT AUTO_INCREMENT PRIMARY KEY,
            Nombre VARCHAR(255) NOT NULL,
            Descripcion VARCHAR(255) NOT NULL,
            Precio BIGINT NOT NULL,
            Cantidad_Stock BIGINT NOT NULL
        );
    ''')
    print("Tabla 'producto' creada o ya existe.")

def agregar_usuario(cursor, username, password):
    cursor.execute('INSERT INTO usuarios (username, password) VALUES (%s, %s)', (username, password))

def verificar_usuario(username, password):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user is not None
    return False

# Funciones de la interfaz
def registrar_usuario_gui():
    username = entry_usuario_nombre.get()
    password = entry_usuario_password.get()
    if username and password:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            try:
                agregar_usuario(cursor, username, password)
                conn.commit()
                messagebox.showinfo("Éxito", "Usuario registrado.")
                entry_usuario_nombre.delete(0, tk.END)
                entry_usuario_password.delete(0, tk.END)
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Error al registrar usuario: {e}")
            finally:
                cursor.close()
                conn.close()
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

def iniciar_sesion_gui():
    username = entry_inicio_usuario.get()
    password = entry_inicio_password.get()
    if verificar_usuario(username, password):
        messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
        ventana_inicio.destroy()  # Cierra la ventana de inicio de sesión
        mostrar_ventana_principal(username)  # Muestra la ventana principal
    else:
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos.")

def mostrar_ventana_principal(username):
    ventana_principal = tk.Tk()
    ventana_principal.title("Inventario de catalogo de avenas")

    label_bienvenida = tk.Label(ventana_principal, text=f"Bienvenido(a), {username}!")
    label_bienvenida.pack(pady=10)

    # Conectar a la base de datos
    conn = conectar_db()
    if conn is not None:
        cursor = conn.cursor()
        crear_tablas(cursor)

        # Sección para Pizzas
        frame_avenas = tk.Frame(ventana_principal)
        frame_avenas.pack(pady=10)

        label_avena_nombre = tk.Label(frame_avenas, text="Nombre de de la avena:")
        label_avena_nombre.grid(row=0, column=0)

        entry_avena_nombre = tk.Entry(frame_avenas)
        entry_avena_nombre.grid(row=0, column=1)

        label_avena_tamaño = tk.Label(frame_avenas, text="Descripcion del producto:")
        label_avena_tamaño.grid(row=1, column=0)

        entry_avena_tamaño = tk.Entry(frame_avenas)
        entry_avena_tamaño.grid(row=1, column=1)
        
        label_avena_tamaño = tk.Label(frame_avenas, text="Precio del producto:")
        label_avena_tamaño.grid(row=2, column=0)
        
        entry_avena_tamaño = tk.Entry(frame_avenas)
        entry_avena_tamaño.grid(row=2, column=1)
        
        label_avena_tamaño = tk.Label(frame_avenas, text="Cantidad en stock:")
        label_avena_tamaño.grid(row=3, column=0)
        
        entry_avena_tamaño = tk.Entry(frame_avenas)
        entry_avena_tamaño.grid(row=3, column=1)

        button_agregar_avena = tk.Button(frame_avenas, text="Agregar avena", command=lambda: agregar_avena(cursor, entry_avena_nombre.get(), entry_avena_tamaño.get()))
        button_agregar_avena.grid(row=2, columnspan=2)


def agregar_avena(cursor, Nombre, Descripcion, Precio, Cantidad_Stock):
    if Nombre and Descripcion and Precio and Cantidad_Stock:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO pizza (Nombre, Descripcion, Precio, Cantidad_Stock) VALUES (%s, %s)', (Nombre, Descripcion, Precio, Cantidad_Stock))
            conn.commit()
            messagebox.showinfo("Éxito", f"avena '{Nombre}' agregada.")
            cursor.close()
            conn.close()
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

def consultar_avenas(cursor):
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM producto')
        resultados = cursor.fetchall()
        avenas_texto = "\n".join([f"ID_preducto: {fila[0]}, Nombre: {fila[1]}, Descripcion: {fila[2]}, Precio: {fila[3]}, Cantidad_Stock: {fila[4]}" for fila in resultados])
        messagebox.showinfo("Avenas en la Base de Datos", avenas_texto if avenas_texto else "No hay ninguna avena registrada.")
        cursor.close()
        conn.close()

# Configuración de la interfaz de registro e inicio de sesión
ventana_inicio = tk.Tk()
ventana_inicio.title("Registro e Inicio de Sesión")

# Crear las tablas si no existen
conn = conectar_db()
if conn:
    cursor = conn.cursor()
    crear_tablas(cursor)
    cursor.close()
    conn.close()

# Sección de Registro de Usuarios
frame_usuario = tk.Frame(ventana_inicio)
frame_usuario.pack(pady=10)

label_usuario_nombre = tk.Label(frame_usuario, text="Nombre de Usuario:")
label_usuario_nombre.grid(row=0, column=0)
entry_usuario_nombre = tk.Entry(frame_usuario)
entry_usuario_nombre.grid(row=0, column=1)

label_usuario_password = tk.Label(frame_usuario, text="Contraseña:")
label_usuario_password.grid(row=1, column=0)
entry_usuario_password = tk.Entry(frame_usuario, show='*')
entry_usuario_password.grid(row=1, column=1)

button_registrar_usuario = tk.Button(frame_usuario, text="Registrar Usuario", command=registrar_usuario_gui)
button_registrar_usuario.grid(row=2, columnspan=2)

# Sección de Inicio de Sesión
frame_inicio_sesion = tk.Frame(ventana_inicio)
frame_inicio_sesion.pack(pady=10)

label_inicio_usuario = tk.Label(frame_inicio_sesion, text="Nombre de Usuario:")
label_inicio_usuario.grid(row=0, column=0)
entry_inicio_usuario = tk.Entry(frame_inicio_sesion)
entry_inicio_usuario.grid(row=0, column=1)

label_inicio_password = tk.Label(frame_inicio_sesion, text="Contraseña:")
label_inicio_password.grid(row=1, column=0)
entry_inicio_password = tk.Entry(frame_inicio_sesion, show='*')
entry_inicio_password.grid(row=1, column=1)

button_iniciar_sesion = tk.Button(frame_inicio_sesion, text="Iniciar Sesión", command=iniciar_sesion_gui)
button_iniciar_sesion.grid(row=2, columnspan=2)

ventana_inicio.mainloop()