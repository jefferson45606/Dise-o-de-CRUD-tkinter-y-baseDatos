import tkinter as tk
from tkinter import messagebox
from controlador_usuario import ControladorUsuario
from interfaz_producto import InterfazProducto

class InterfazLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("300x200")

        # Crear instancia del controlador de usuario
        self.controlador = ControladorUsuario()

        # Campos de entrada para usuario y contraseña
        self.label_usuario = tk.Label(root, text="Usuario")
        self.label_usuario.pack(pady=5)
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack(pady=5)

        self.label_password = tk.Label(root, text="Contraseña")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)

        # Botón para iniciar sesión
        self.btn_iniciar_sesion = tk.Button(root, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.btn_iniciar_sesion.pack(pady=10)

        # Botón para ir al registro de usuario
        self.btn_registrar = tk.Button(root, text="Registrar Usuario", command=self.mostrar_registro)
        self.btn_registrar.pack(pady=10)

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        if self.controlador.validar_usuario(usuario, password):
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
            self.abrir_interfaz_producto()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def mostrar_registro(self):
        self.root.destroy()
        root_registro = tk.Tk()
        InterfazRegistro(root_registro)
        root_registro.mainloop()

    def abrir_interfaz_producto(self):
        # Abrir la interfaz de productos si el inicio de sesión es exitoso
        self.root.destroy()
        root_producto = tk.Tk()
        InterfazProducto(root_producto)
        root_producto.mainloop()

class InterfazRegistro:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuario")
        self.root.geometry("300x250")

        # Crear instancia del controlador de usuario
        self.controlador = ControladorUsuario()

        # Campos de entrada para usuario, contraseña y rol
        self.label_usuario = tk.Label(root, text="Usuario")
        self.label_usuario.pack(pady=5)
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack(pady=5)

        self.label_password = tk.Label(root, text="Contraseña")
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)

        self.label_rol = tk.Label(root, text="Rol (vendedor/administrativo)")
        self.label_rol.pack(pady=5)
        self.entry_rol = tk.Entry(root)
        self.entry_rol.pack(pady=5)

        # Botón para registrar el usuario
        self.btn_registrar = tk.Button(root, text="Registrar", command=self.registrar_usuario)
        self.btn_registrar.pack(pady=10)

    def registrar_usuario(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        rol = self.entry_rol.get()

        if usuario and password and rol in ["vendedor", "administrativo"]:
            if self.controlador.registrar_usuario(usuario, password, rol):
                messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
                self.root.destroy()
                root_login = tk.Tk()
                InterfazLogin(root_login)
                root_login.mainloop()
            else:
                messagebox.showerror("Error", "El usuario ya existe.")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios y el rol debe ser 'vendedor' o 'administrativo'.")