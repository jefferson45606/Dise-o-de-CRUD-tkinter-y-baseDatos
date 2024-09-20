import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class VistaCatalogo:
    def __init__(self, root, controlador):
        self.controlador = controlador
        self.root = root
        self.root.title("Catálogo de Productos")

        # Crear una tabla para mostrar los productos
        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "Descripción", "Precio", "Stock"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Stock", text="Stock")
        self.tree.pack(pady=20)

        # Botón para cargar los productos
        self.boton_cargar = tk.Button(root, text="Cargar Productos", command=self.cargar_productos)
        self.boton_cargar.pack(pady=10)
        self.boton_informe = tk.Button(root, text="Generar Informe", command=self.generar_informe)
        self.boton_informe.pack(pady=10)

    def cargar_productos(self):
        # Limpiar la tabla antes de cargar nuevos productos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Obtener los productos desde el controlador y agregarlos a la tabla
        productos = self.controlador.obtener_productos()
        for producto in productos:
            self.tree.insert("", tk.END, values=(producto.id_producto, producto.nombre, producto.descripcion, producto.precio, producto.stock))
            

    def generar_informe(self):
        # Llamar al método del controlador para generar el archivo TXT
        if self.controlador.generar_informe_productos():
            messagebox.showinfo("Informe Generado", "El informe de productos se ha generado exitosamente.")
        else:
            messagebox.showerror("Error", "No se pudo generar el informe.")

