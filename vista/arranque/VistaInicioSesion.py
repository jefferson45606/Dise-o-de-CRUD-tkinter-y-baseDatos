import tkinter as tk

class vistadeinicio():
    def inicio():
        vistadeinicio.root=tk.Tk()
        vistadeinicio.root.title("Avanas.com XD")
        vistadeinicio.root.geometry("600x400")
        vistadeinicio.root.configure(bg="#b9f1d6")
        
        vistadeinicio.frame = tk.Frame(vistadeinicio.root, padx=10, pady=10, bg="#b9f1d6")
        vistadeinicio.frame.pack()
        vistadeinicio.usuario_label = tk.Label(vistadeinicio.frame, text="cedula")
        vistadeinicio.usuario_label.grid(column=0,row=0)
        vistadeinicio.usuario_Entry = tk.Entry(vistadeinicio.frame)
        vistadeinicio.usuario_Entry.grid(column=0,row=1)

        vistadeinicio.contraseña_label = tk.Label(vistadeinicio.frame, text="contraseña")
        vistadeinicio.contraseña_label.grid(column=0,row=2)
        vistadeinicio.contraseña_Entry = tk.Entry(vistadeinicio.frame)
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
        vistadeinicio.usuario =vistadeinicio.usuario_Entry.get()
        vistadeinicio.contraseña =vistadeinicio.contraseña_Entry.get()
        vistadeinicio.root.destroy()
        vistadeinicio.comprobar="si"