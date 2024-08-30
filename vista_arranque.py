from tkinter import *
import tkinter as tk

class eleccion():
    def arranque():
        eleccion.root=tk.Tk()
        eleccion.root.title("Avanas.com XD")
        eleccion.root.geometry("600x400")
        eleccion.root.configure(bg="#b9f1d6")
        eleccion.frame = tk.Frame(eleccion.root, padx=10, pady=10, bg="#b9f1d6")
        eleccion.frame.pack()
        eleccion.inicio_botton = tk.Button(eleccion.frame, text="iniciar" , bg="skyblue")
        eleccion.inicio_botton.grid(row=0, column=0, padx=10, pady=10)
        eleccion.registro_botton = tk.Button(eleccion.frame, text="registrarse" , bg="skyblue")
        eleccion.registro_botton.grid(row=0, column=1, padx=10, pady=10)
        eleccion.root.mainloop()
        
    def iniciar():
        pass