import tkinter as tk
from tkinter import messagebox

class VistaRegistroProducto:
    def __init__(self, root, controlador):
        self.controlador = controlador
        self.root = root
        self.root.title("Registro de Producto")

        # Campos de entrada para los datos del producto
        self.label_nombre = tk.Label(root, text="Nombre del Producto")
        self.label_nombre.pack(pady=10)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack(pady=10)

        self.label_descripcion = tk.Label(root, text="Descripción")
        self.label_descripcion.pack(pady=10)
        self.entry_descripcion = tk.Entry(root)
        self.entry_descripcion.pack(pady=10)

        self.label_precio = tk.Label(root, text="Precio")
        self.label_precio.pack(pady=10)
        self.entry_precio = tk.Entry(root)
        self.entry_precio.pack(pady=10)

        self.label_stock = tk.Label(root, text="Stock")
        self.label_stock.pack(pady=10)
        self.entry_stock = tk.Entry(root)
        self.entry_stock.pack(pady=10)

        # Botón para registrar el producto
        self.boton_registrar = tk.Button(root, text="Registrar Producto", command=self.registrar_producto)
        self.boton_registrar.pack(pady=20)

    def registrar_producto(self):
        # Obtener los valores ingresados
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        precio = float(self.entry_precio.get())
        stock = int(self.entry_stock.get())

        # Llamar al controlador para registrar el producto
        self.controlador.agregar_producto(nombre, descripcion, precio, stock)
        messagebox.showinfo("Éxito", "Producto registrado exitosamente")
        self.limpiar_campos()

    def limpiar_campos(self):
        # Limpiar los campos de texto después de registrar un producto
        self.entry_nombre.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)
