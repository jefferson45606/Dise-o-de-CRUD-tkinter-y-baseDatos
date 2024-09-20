
import tkinter as tk
from controlador import Controlador
from vista_inicio import VistaInicioSesion

# Crear la ventana principal
root = tk.Tk()

# Crear el controlador
controlador = Controlador()

# Crear la vista del inicio de sesión y pasarle el controlador
vista_inicio = VistaInicioSesion(root, controlador)

# Ejecutar la aplicación
root.mainloop()
