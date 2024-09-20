import tkinter as tk
from tkinter import messagebox

class VistaInicioSesion:
    def __init__(self, root, controlador, abrir_registro_producto):
        self.controlador = controlador
        self.root = root
        self.abrir_registro_producto = abrir_registro_producto  # Método para abrir la interfaz de registro de productos

        self.root.title("Inicio de Sesión")

        # entrada para el nombre de usuario
        self.label_usuario = tk.Label(root, text="Usuario")
        self.label_usuario.pack(pady=10)
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack(pady=10)

        # entrada para la contraseña
        self.label_password = tk.Label(root, text="Contraseña")
        self.label_password.pack(pady=10)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=10)

        # Botón de inicio de sesión
        self.boton_login = tk.Button(root, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_login.pack(pady=20)

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        # Validar el inicio de sesión usando el controlador
        if self.controlador.validar_usuario(usuario, password):
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            self.root.destroy()  # Cerrar la ventana actual de inicio de sesión
            self.abrir_registro_producto()  # Abrir la interfaz de registro de productos
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

