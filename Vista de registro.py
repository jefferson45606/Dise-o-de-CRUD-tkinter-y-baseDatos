import tkinter as tk

class vistaregistroproducto(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.titulo = tk.Label(self, text="Registrar Producto")
        self.titulo.pack()
        # Aquí se agregan widgets para ingresar datos del producto.
