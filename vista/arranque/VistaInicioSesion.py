import tkinter as tk

class vistadeinicio():
    def inicio():
        vistadeinicio.root=tk.Tk()
        vistadeinicio.root.title("Avanas.com XD")
        vistadeinicio.root.geometry("600x400")
        vistadeinicio.root.configure(bg="#b9f1d6")
        
        vistadeinicio.frame = tk.Frame(vistadeinicio.root, padx=10, pady=10, bg="#b9f1d6")
        vistadeinicio.frame.pack()
        vistadeinicio.usuario_label = tk.Label(vistadeinicio.frame, text="usuario")
        vistadeinicio.usuario_label.grid(column=0,row=0)
        vistadeinicio.usuario_Entry = tk.Entry(vistadeinicio.frame)
        vistadeinicio.usuario_Entry.grid(column=0,row=1)

        vistadeinicio.contraseña_label = tk.Label(vistadeinicio.frame, text="contraseña")
        vistadeinicio.contraseña_label.grid(column=0,row=2)
        vistadeinicio.contraseña_Entry = tk.Entry(vistadeinicio.frame)
        vistadeinicio.contraseña_Entry.grid(column=0,row=3)
        
        vistadeinicio.inicio_botton = tk.Button(vistadeinicio.frame, text="iniciar" , bg="skyblue")
        vistadeinicio.inicio_botton.grid(row=10, column=0, padx=10, pady=10)
        
        vistadeinicio.root.mainloop()