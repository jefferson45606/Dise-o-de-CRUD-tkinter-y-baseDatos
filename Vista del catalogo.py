import tkinter as tk

class vistaCatalogo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.titulo = tk.Label(self, text="Catálogo de Productos")
        self.titulo.pack()
        # Aquí se agregan más widgets como botones, listas, etc.
