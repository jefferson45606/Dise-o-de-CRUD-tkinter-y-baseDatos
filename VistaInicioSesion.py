import tkinter as tk

class vistadeinicio(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.titulo = tk.Label(self, text="Inicio de Sesión")
        self.titulo.pack()
        # Aquí se agregan widgets para el usuario y la contraseña.
