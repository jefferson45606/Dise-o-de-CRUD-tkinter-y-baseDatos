import tkinter as tk
from tkinter import messagebox

class vistadeinicio():
    def inicio():
        vistadeinicio.root=tk.Tk()
        vistadeinicio.root.title("Avanas.com")
        vistadeinicio.root.geometry("200x300")
        vistadeinicio.root.configure(bg="ghost white")
        
        vistadeinicio.frame = tk.Frame(vistadeinicio.root, padx=10, pady=10, bg="ghost white")
        vistadeinicio.frame.pack()
        vistadeinicio.usuario_label = tk.Label(vistadeinicio.frame, text="cedula")
        vistadeinicio.usuario_label.grid(column=0,row=0)
        vistadeinicio.usuario_Entry = tk.Entry(vistadeinicio.frame)
        vistadeinicio.usuario_Entry.grid(column=0,row=1)

        vistadeinicio.contraseña_label = tk.Label(vistadeinicio.frame, text="contraseña")
        vistadeinicio.contraseña_label.grid(column=0,row=2)
        vistadeinicio.contraseña_Entry = tk.Entry(vistadeinicio.frame, show="*") # falto agregar eso para que no se vea la contraseña
        vistadeinicio.contraseña_Entry.grid(column=0,row=3)
        
        vistadeinicio.inicio_botton = tk.Button(vistadeinicio.frame, text="iniciar" , bg="skyblue", command=vistadeinicio.iniciar)
        vistadeinicio.inicio_botton.grid(row=10, column=0, padx=10, pady=10)
        
        vistadeinicio.volver_botton = tk.Button(vistadeinicio.frame, text="volver" , bg="skyblue", command=vistadeinicio.retroceder)
        vistadeinicio.volver_botton.grid(row=11, column=0, padx=10, pady=10)
        
        vistadeinicio.root.mainloop()
        
    def retroceder():
        vistadeinicio.usuario = ""
        vistadeinicio.contraseña = ""
        vistadeinicio.root.destroy()
        vistadeinicio.comprobar="no"
        
    def iniciar():
        try:
            vistadeinicio.comprobar="si"
            try:
                vistadeinicio.usuario = int(vistadeinicio.usuario_Entry.get())
            except:
                if vistadeinicio.usuario == None:
                    messagebox.showerror("Error", "debe de llenar todas las casillas")
                else:
                    messagebox.showerror("Error", "solo puede poner numeros")
                vistadeinicio.comprobar="no"
            vistadeinicio.contraseña =vistadeinicio.contraseña_Entry.get()
            if vistadeinicio.contraseña == "":
                messagebox.showerror("Error", "debe de llenar todas las casillas")
                vistadeinicio.comprobar="no"
            vistadeinicio.root.destroy()
        except:
            messagebox.showerror("Error", "debe de llenar todas las casillas")
            vistadeinicio.comprobar="no"