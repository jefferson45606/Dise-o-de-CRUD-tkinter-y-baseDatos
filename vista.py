import tkinter as tk
from tkinter import messagebox
from controlador import Controlador

class Aplicacion:
    def __init__(self):
        self.controlador = Controlador()
        self.ventana = tk.Tk()
        self.ventana.title("Catálogo de Avenas")
        
        self.crear_interface_inicio_sesion()
        
    def crear_interface_inicio_sesion(self):
        tk.Label(self.ventana, text="Usuario:").grid(row=0, column=0)
        self.entry_usuario = tk.Entry(self.ventana)
        self.entry_usuario.grid(row=0, column=1)

        tk.Label(self.ventana, text="Contraseña:").grid(row=1, column=0)
        self.entry_contrasena = tk.Entry(self.ventana, show='*')
        self.entry_contrasena.grid(row=1, column=1)

        tk.Button(self.ventana, text="Iniciar Sesión", command=self.iniciar_sesion).grid(row=2, columnspan=2)

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        if self.controlador.iniciar_sesion(usuario, contrasena):
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
            self.ventana.destroy()
            self.crear_interface_principal()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def crear_interface_principal(self):
        self.ventana = tk.Tk()
        self.ventana.title("Catálogo de Avenas")

        tk.Label(self.ventana, text="Registrar Producto").grid(row=0, columnspan=2)

        tk.Label(self.ventana, text="Nombre:").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(self.ventana)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(self.ventana, text="Descripción:").grid(row=2, column=0)
        self.entry_descripcion = tk.Entry(self.ventana)
        self.entry_descripcion.grid(row=2, column=1)

        tk.Label(self.ventana, text="Precio:").grid(row=3, column=0)
        self.entry_precio = tk.Entry(self.ventana)
        self.entry_precio.grid(row=3, column=1)

        tk.Label(self.ventana, text="Cantidad en Stock:").grid(row=4, column=0)
        self.entry_cantidad = tk.Entry(self.ventana)
        self.entry_cantidad.grid(row=4, column=1)

        tk.Button(self.ventana, text="Registrar Producto", command=self.registrar_producto).grid(row=5, columnspan=2)

        tk.Button(self.ventana, text="Consultar Productos", command=self.consultar_productos).grid(row=6, columnspan=2)
        
        tk.Button(self.ventana, text="Generar Informe JSON", command=self.generar_informe_json).grid(row=7, columnspan=2)


        self.ventana.mainloop()

    def registrar_producto(self):
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        precio = self.entry_precio.get()
        cantidad = self.entry_cantidad.get()
        self.controlador.registrar_producto(nombre, descripcion, float(precio), int(cantidad))
        messagebox.showinfo("Éxito", "Producto registrado.")

    def consultar_productos(self):
        productos = self.controlador.obtener_productos()
        if productos:
            info_productos = "\n".join([f"ID: {p[0]}, Nombre: {p[1]}, Precio: {p[3]}, Cantidad: {p[4]}" for p in productos])
            messagebox.showinfo("Productos", info_productos)
        else:
            messagebox.showinfo("Productos", "No hay productos registrados.")
        
    def generar_informe_json(self):
        self.controlador.generar_informe_json()
        messagebox.showinfo("Éxito", "Informe generado en formato JSON.")

            
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
    

