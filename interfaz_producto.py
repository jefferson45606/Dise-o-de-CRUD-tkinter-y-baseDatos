import tkinter as tk
from tkinter import messagebox
from controlador_producto import ControladorProducto

class InterfazProducto:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Productos")
        self.root.geometry("400x300")

        # Crear instancia del controlador de productos
        self.controlador = ControladorProducto()

        # Campos de entrada para los detalles del producto
        self.label_nombre = tk.Label(root, text="Nombre del Producto")
        self.label_nombre.pack(pady=5)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack(pady=5)

        self.label_descripcion = tk.Label(root, text="Descripción del Producto")
        self.label_descripcion.pack(pady=5)
        self.entry_descripcion = tk.Entry(root)
        self.entry_descripcion.pack(pady=5)

        self.label_precio = tk.Label(root, text="Precio del Producto")
        self.label_precio.pack(pady=5)
        self.entry_precio = tk.Entry(root)
        self.entry_precio.pack(pady=5)

        self.label_cantidad = tk.Label(root, text="Cantidad Disponible")
        self.label_cantidad.pack(pady=5)
        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.pack(pady=5)

        # Botón para registrar el producto
        self.btn_registrar = tk.Button(root, text="Registrar Producto", command=self.registrar_producto)
        self.btn_registrar.pack(pady=10)

    def registrar_producto(self):
        """Registrar un nuevo producto en la base de datos"""
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        precio = self.entry_precio.get()
        cantidad = self.entry_cantidad.get()

        if nombre and descripcion and precio and cantidad:
            try:
                precio = float(precio)
                cantidad = int(cantidad)
                if self.controlador.registrar_producto(nombre, descripcion, precio, cantidad):
                    messagebox.showinfo("Éxito", "Producto registrado correctamente.")
                    self.limpiar_campos()
                else:
                    messagebox.showerror("Error", "Error al registrar el producto.")
            except ValueError:
                messagebox.showerror("Error", "El precio debe ser un número y la cantidad un entero.")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    def limpiar_campos(self):
        """Limpiar los campos de entrada después de registrar un producto"""
        self.entry_nombre.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)

