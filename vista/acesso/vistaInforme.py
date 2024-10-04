import tkinter as tk

class vistainforme(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.titulo = tk.Label(self, text="Informe de Productos")
        self.titulo.pack()
