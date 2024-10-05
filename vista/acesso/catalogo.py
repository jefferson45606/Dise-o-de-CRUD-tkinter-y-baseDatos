import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import random

# Ventana 1: Catálogo de Productos
class ProductsFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Título de la sección
        catalog_title = tk.Label(self, text="Catálogo de Productos", font=("Arial", 18))
        catalog_title.pack(pady=10)

        # Botones de categorías
        category_buttons_frame = tk.Frame(self)
        category_buttons_frame.pack(pady=10)

        tk.Button(category_buttons_frame, text="Más Caro", command=self.sort_by_price_desc).pack(side="left", padx=5)
        tk.Button(category_buttons_frame, text="Más Barato", command=self.sort_by_price_asc).pack(side="left", padx=5)
        tk.Button(category_buttons_frame, text="A-Z", command=self.sort_by_name_asc).pack(side="left", padx=5)
        tk.Button(category_buttons_frame, text="Z-A", command=self.sort_by_name_desc).pack(side="left", padx=5)
        tk.Button(category_buttons_frame, text="Buscar", command=self.open_search_window).pack(side="left", padx=5)

        # Marco del catálogo de productos
        self.products_frame = tk.Frame(self)
        self.products_frame.pack(pady=10, fill="both")

        # Botón para registrar un nuevo producto
        register_button = tk.Button(self, text="Registrar Producto", command=self.open_register_window)
        register_button.pack(pady=10)

    # Función para abrir la ventana de registro de productos
    def open_register_window(self):
        register_window = tk.Toplevel(self)
        register_window.title("Registrar Producto")
        register_window.geometry("400x400")

        # Variables para almacenar los datos del producto
        product_name = tk.StringVar()
        product_description = tk.StringVar()
        product_image_path = tk.StringVar()
        product_price = tk.DoubleVar(value=0.0)
        codigo = tk.DoubleVar(value=0.0)
        ventas = tk.DoubleVar(value=0.0)

        # Función para cargar imagen
        def upload_image():
            filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
            if filepath:
                product_image_path.set(filepath)
                image_label.config(text=f"Imagen: {filepath.split('/')[-1]}")

        # Campos de entrada
        tk.Label(register_window, text="Nombre del Producto:").pack(pady=5)
        tk.Entry(register_window, textvariable=product_name).pack(pady=5)

        tk.Label(register_window, text="Descripción del Producto:").pack(pady=5)
        tk.Entry(register_window, textvariable=product_description).pack(pady=5)

        tk.Label(register_window, text="Precio del Producto:").pack(pady=5)
        tk.Entry(register_window, textvariable=product_price).pack(pady=5)
        
        tk.Label(register_window, text="codigo:").pack(pady=5)
        tk.Entry(register_window, textvariable=codigo).pack(pady=5)
        
        tk.Label(register_window, text="cantidad de ventas:").pack(pady=5)
        tk.Entry(register_window, textvariable=ventas).pack(pady=5)

        tk.Button(register_window, text="Cargar Imagen", command=upload_image).pack(pady=5)
        image_label = tk.Label(register_window, text="No se ha seleccionado ninguna imagen")
        image_label.pack(pady=5)

        # Función para registrar el producto
        def register_product():
            inicio.name = product_name.get()
            inicio.description = product_description.get()
            inicio.price = product_price.get()
            inicio.image_path = product_image_path.get()
            inicio.codigo = codigo.get()
            inicio.ventas = ventas.get()

            if inicio.codigo and inicio.name and inicio.description and inicio.image_path and inicio.price >= 0:
                inicio.confirmar = "si"
                messagebox.showinfo("Éxito", "Producto registrado con éxito.")
                register_window.destroy()
                inicio.root.destroy()
            else:
                messagebox.showwarning("Datos Incompletos", "Por favor complete todos los campos y asegúrese de que el precio no sea negativo.")
                inicio.confirmar = "no"
                register_window.destroy()
                inicio.root.destroy()

        tk.Button(register_window, text="Registrar Producto", command=register_product).pack(pady=10)

    # Función para actualizar el catálogo con los productos registrados
    def update_catalog(self):
        # Limpiar la grilla de productos actual
        for widget in self.products_frame.winfo_children():
            widget.destroy()

        # Mostrar cada producto en la grilla
        for index, product in enumerate(inicio.registered_products):

            product_frame = tk.Frame(self.products_frame, bd=1, relief="solid")
            product_frame.grid(row=index // 4, column=index % 4, padx=10, pady=10)

            tk.Label(product_frame, text=product["Nombre"], font=("Arial", 10, "bold")).pack(pady=2)
            tk.Label(product_frame, text=product["Descripcion"], font=("Arial", 8)).pack(pady=2)
            tk.Label(product_frame, text=(f"Precio: ${product['Precio']:.2f}"), font=("Arial", 8)).pack(pady=2)

    # Funciones para ordenar el catálogo
    def sort_by_price_desc(self):
        global registered_products
        inicio.registered_products.sort(key=lambda x: x["Precio"], reverse=True)
        ProductsFrame.update_catalog()

    def sort_by_price_asc(self):
        global registered_products
        inicio.registered_products.sort(key=lambda x: x["Precio"])
        ProductsFrame.update_catalog()

    def sort_by_name_asc(self):
        global registered_products
        inicio.registered_products.sort(key=lambda x: x["Nombre"].lower())
        ProductsFrame.update_catalog()

    def sort_by_name_desc(self):
        global registered_products
        inicio.registered_products.sort(key=lambda x: x["Nombre"].lower(), reverse=True)
        ProductsFrame.update_catalog()

    # Función para abrir la ventana de búsqueda
    def open_search_window(self):
        search_window = tk.Toplevel(self)
        search_window.title("Buscar Producto")
        search_window.geometry("300x150")

        search_value = tk.StringVar()

        tk.Label(search_window, text="Buscar por Nombre o Precio:").pack(pady=10)
        tk.Entry(search_window, textvariable=search_value).pack(pady=5)

        # Función para buscar productos
        def search_product():
            search_term = search_value.get()
            if not search_term:
                return

            try:
                price = float(search_term)
                results = [p for p in inicio.registered_products if p["Precio"] == price]
            except ValueError:
                results = [p for p in inicio.registered_products if search_term.lower() in p["Nombre"].lower()]

            if results:
                result_msg = "\n".join([f"{product['Nombre']} - ${product['Precio']:.2f}" for product in results])
                messagebox.showinfo("Resultados", f"Se encontraron {len(results)} productos:\n{result_msg}")
            else:
                messagebox.showinfo("Sin Resultados", "No se encontraron productos.")

        tk.Button(search_window, text="Buscar Producto", command=search_product).pack(pady=10)

# Ventana 2: Informe de Productos
class AboutFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Título de la sección
        report_title = tk.Label(self, text="Informe de Productos", font=("Arial", 18))
        report_title.pack(pady=10)

        # Marcos para listas de más y menos vendidos
        reports_frame = tk.Frame(self)
        reports_frame.pack(pady=10)

        # Marco de más vendidos
        most_sold_frame = tk.Frame(reports_frame, bd=1, relief="solid")
        most_sold_frame.grid(row=0, column=0, padx=10, pady=10)
        tk.Label(most_sold_frame, text="Más Vendidos").pack(pady=5)
        self.most_sold_listbox = tk.Listbox(most_sold_frame)
        self.most_sold_listbox.pack(pady=5)

        # Marco de menos vendidos
        least_sold_frame = tk.Frame(reports_frame, bd=1, relief="solid")
        least_sold_frame.grid(row=0, column=1, padx=10, pady=10)
        tk.Label(least_sold_frame, text="Menos Vendidos").pack(pady=5)
        self.least_sold_listbox = tk.Listbox(least_sold_frame)
        self.least_sold_listbox.pack(pady=5)

        # Botón para generar el informe
        generate_report_button = tk.Button(self, text="Generar Informe", command=self.generate_report)
        generate_report_button.pack(pady=10)

    # Función para generar el informe de productos
    def generate_report(self):
        self.most_sold_listbox.delete(0, "end")
        self.least_sold_listbox.delete(0, "end")

        # Ordenar los productos por ventas (aquí las ventas son aleatorias)
        sorted_products = sorted(inicio.registered_products, key=lambda x: x["Precio"], reverse=True)

        for product in sorted_products[:5]:  # Más vendidos
            self.most_sold_listbox.insert("end", f"{product['Nombre']} - ${product['Precio']:.2f}")

        for product in sorted_products[-5:]:  # Menos vendidos
            self.least_sold_listbox.insert("end", f"{product['Nombre']} - ${product['Precio']:.2f}")
            
            
class inicio():
# Función para cambiar de ventana
    def show_frame(frame_name):
        frame = inicio.frames[frame_name]
        frame.tkraise()

    def iniciar():
        # Lista de productos registrados

        # Crear la aplicación principal
        inicio.root = tk.Tk()
        inicio.root.title("Catálogo de Productos")
        inicio.root.geometry("1200x800")

        # Frame contenedor para las diferentes pantallas
        container = tk.Frame(inicio.root)
        container.pack(expand=True, fill="both")

        

        # Frame base para el menú superior
        top_menu_frame = tk.Frame(inicio.root, bd=1, relief="solid", height=50)
        top_menu_frame.pack(side="top", fill="x")

        # Botones del menú superior
        for menu in [("Home", "ProductsFrame"), ("About", "AboutFrame")]:
            tk.Button(top_menu_frame, text=menu[0], command=lambda name=menu[1]: inicio.show_frame(name)).pack(side="left", padx=5, pady=5)

        # Crear las ventanas y agregarlas al diccionario de frames
        for F in (ProductsFrame, AboutFrame):
            inicio.frame = F(container, inicio.root)
            inicio.frames[F.__name__] = inicio.frame
            inicio.frame.grid(row=0, column=0, sticky="nsew")

        # Mostrar la ventana inicial
        inicio.show_frame("ProductsFrame")
        try:
            ProductsFrame.update_catalog()
            print("este codigo se ejecuta")
        except:
            print("este codigo no se ejecuta")
        inicio.root.mainloop()