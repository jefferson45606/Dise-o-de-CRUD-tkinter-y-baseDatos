from tkinter import *
import tkinter as tk

class eleccion():
    def arranque():
        eleccion.root=tk.Tk()
        eleccion.root.title("Avanas.com")
        eleccion.root.geometry("200x300")
        eleccion.root.configure(bg="ghost white")
        
        eleccion.frame = tk.Frame(eleccion.root, padx=10, pady=10, bg="ghost white")
        eleccion.frame.pack()
        eleccion.inicio_botton = tk.Button(eleccion.frame, text="iniciar secion" , bg="skyblue" ,command=eleccion.iniciar)
        eleccion.inicio_botton.grid(row=3, column=0, padx=10, pady=10)
        
        eleccion.registro_botton = tk.Button(eleccion.frame, text="registrarse" , bg="skyblue", command=eleccion.registrarse)
        eleccion.registro_botton.grid(row=5, column=0 , padx=10, pady=10)
        eleccion.root.mainloop()
        
    def iniciar():
        eleccion.E = "iniciar"
        eleccion.root.destroy()
        
    def registrarse():
        eleccion.E = "registrarse"
        eleccion.root.destroy()