import tkinter as tk
from tkinter import simpledialog, messagebox

class Product:
    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tienda")
        self.products = []

        tk.Button(self.root, text="Añadir Producto", command=self.add_product).pack(pady=20)
        self.root.mainloop()

    def add_product(self):
        name = simpledialog.askstring("Añadir Producto", "Nombre del Producto:")
        description = simpledialog.askstring("Añadir Producto", "Descripción:")
        price = simpledialog.askfloat("Añadir Producto", "Precio:")
        stock = simpledialog.askinteger("Añadir Producto", "Stock:")

        if name and description and price is not None and stock is not None:
            new_product = Product(name, description, price, stock)
            self.products.append(new_product)
            messagebox.showinfo("Éxito", "Producto añadido con éxito.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

if __name__ == "__main__":
    app = App()
