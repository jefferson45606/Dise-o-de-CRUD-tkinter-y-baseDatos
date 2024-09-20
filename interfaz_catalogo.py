import tkinter as tk
from tkinter import messagebox
from controlador_producto import ControladorProducto

class InterfazCatalogo:
    def __init__(self, root):
        self.root = root
        self.root.title("Catálogo de Productos")
        self.root.geometry("500x400")

        # Crear instancia del controlador de productos
        self.controlador = ControladorProducto()

        # Campo para filtrar productos por nombre
        self.label_busqueda = tk.Label(root, text="Buscar Producto por Nombre")
        self.label_busqueda.pack(pady=5)
        self.entry_busqueda = tk.Entry(root)
        self.entry_busqueda.pack(pady=5)

        # Botón para buscar producto
        self.btn_buscar = tk.Button(root, text="Buscar", command=self.buscar_producto)
        self.btn_buscar.pack(pady=10)

        # Listbox para mostrar los productos
        self.listbox_productos = tk.Listbox(root, width=50, height=10)
        self.listbox_productos.pack(pady=10)

        # Botón para cargar todos los productos
        self.btn_cargar_todo = tk.Button(root, text="Cargar Todos los Productos", command=self.cargar_productos)
        self.btn_cargar_todo.pack(pady=10)

    def cargar_productos(self):
        """Cargar todos los productos en el Listbox"""
        self.listbox_productos.delete(0, tk.END)  # Limpiar el Listbox

        productos = self.controlador.obtener_todos_los_productos()

        if productos:
            for producto in productos:
                self.listbox_productos.insert(tk.END, f"{producto[0]} - {producto[1]} - {producto[2]} - {producto[3]} unidades")
        else:
            messagebox.showinfo("Información", "No hay productos registrados.")

    def buscar_producto(self):
        """Buscar producto por nombre"""
        nombre_producto = self.entry_busqueda.get()
        if nombre_producto:
            productos = self.controlador.buscar_producto_por_nombre(nombre_producto)
            self.listbox_productos.delete(0, tk.END)  # Limpiar el Listbox

            if productos:
                for producto in productos:
                    self.listbox_productos.insert(tk.END, f"{producto[0]} - {producto[1]} - {producto[2]} - {producto[3]} unidades")
            else:
                messagebox.showinfo("Información", "No se encontró ningún producto con ese nombre.")
        else:
            messagebox.showerror("Error", "Por favor, ingresa un nombre de producto.")
