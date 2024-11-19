import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# Clase para la gestión de productos
class Product:
    def __init__(self, name, description, price, stock, image_path):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.image_path = image_path

# Clase para la gestión de usuarios
class User:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin

# Clase principal de la aplicación
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tienda")
        self.root.geometry("600x400")
        
        self.users = [
            User("admin", "admin", is_admin=True),
            User("sebastian", "1234")  # Usuario añadido
        ]
        self.current_user = None
        self.products = []

        self.show_login_frame()

    def show_login_frame(self):
        self.clear_frame()

        tk.Label(self.root, text="Iniciar Sesión", font=("Arial", 20)).pack(pady=10)

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        self.username_entry.insert(0, "Nombre de Usuario")

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)
        self.password_entry.insert(0, "Contraseña")

        tk.Button(self.root, text="Iniciar Sesión", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                self.show_catalog_frame()
                return
        
        messagebox.showerror("Error", "Credenciales incorrectas")

    def show_catalog_frame(self):
        self.clear_frame()
        tk.Label(self.root, text="Catálogo de Productos", font=("Arial", 20)).pack(pady=10)

        self.product_frame = tk.Frame(self.root)
        self.product_frame.pack(pady=10)

        self.load_products()

        if self.current_user.is_admin:
            tk.Button(self.root, text="Añadir Producto", command=self.add_product).pack(pady=5)
            tk.Button(self.root, text="Generar Informe", command=self.generate_report).pack(pady=5)

        tk.Button(self.root, text="Cerrar Sesión", command=self.show_login_frame).pack(pady=10)

    def load_products(self):
        for widget in self.product_frame.winfo_children():
            widget.destroy()

        for product in self.products:
            product_frame = tk.Frame(self.product_frame)
            product_frame.pack(pady=5)

            img = Image.open(product.image_path)
            img.thumbnail((50, 50))
            img = ImageTk.PhotoImage(img)

            img_label = tk.Label(product_frame, image=img)
            img_label.image = img  # mantener una referencia
            img_label.pack(side="left")

            tk.Label(product_frame, text=product.name).pack(side="left")
            tk.Label(product_frame, text=f"${product.price:.2f}").pack(side="left")
            tk.Button(product_frame, text="Comprar", command=lambda p=product: self.purchase_product(p)).pack(side="left")
            
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


    def purchase_product(self, product):
        quantity = simpledialog.askinteger("Comprar Producto", f"¿Cuántos quieres comprar de {product.name}?")
        if quantity is not None and quantity > 0:
            if quantity > product.stock:
                messagebox.showwarning("Advertencia", "No hay suficiente stock.")
            else:
                total_price = product.price * quantity
                product.stock -= quantity  # Reducir el stock
                messagebox.showinfo("Factura", f"Producto: {product.name}\nCantidad: {quantity}\nTotal: ${total_price:.2f}")

    def generate_report(self):
        report = "Informe de Productos:\n"
        for product in self.products:
            report += f"{product.name} - ${product.price:.2f} - Stock: {product.stock}\n"
        messagebox.showinfo("Informe de Productos", report)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
