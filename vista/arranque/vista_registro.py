from vista.mensajes.mensajes_de_alerta import errores_en_registro
import tkinter as tk

class registro():
    def inicio():
        registro.root=tk.Tk()
        registro.root.title("Avanas.com")
        registro.root.geometry("600x400")
        registro.root.configure(bg="ghost white")
        
        registro.frame = tk.Frame(registro.root, padx=10, pady=10, bg="ghost white")
        registro.frame.pack()
        registro.usuario_label = tk.Label(registro.frame, text="usuario")
        registro.usuario_label.grid(column=1,row=2)
        registro.usuario_Entry = tk.Entry(registro.frame)
        registro.usuario_Entry.grid(column=1,row=3)

        registro.contraseña_label = tk.Label(registro.frame, text="contraseña")
        registro.contraseña_label.grid(column=1,row=4)
        registro.contraseña_Entry = tk.Entry(registro.frame) 
        registro.contraseña_Entry.grid(column=1,row=5)

        registro.nombre_label = tk.Label(registro.frame, text="Nombre")
        registro.nombre_label.grid(column=1,row=6)
        registro.nombre_Entry = tk.Entry(registro.frame)
        registro.nombre_Entry.grid(column=1,row=7)

        registro.cedula_label = tk.Label(registro.frame, text="Cedula")
        registro.cedula_label.grid(column=1,row=0)
        registro.cedula_Entry = tk.Entry(registro.frame)
        registro.cedula_Entry.grid(column=1,row=1)
        
        registro.registrar_botton = tk.Button(registro.frame, text="registrar" , bg="skyblue" , command=registro.comprobacion_de_registro)
        registro.registrar_botton.grid(row=10, column=1, padx=10, pady=10)
        
        registro.volver_botton = tk.Button(registro.frame, text="volver" , bg="skyblue" , command=registro.retroceder)
        registro.volver_botton.grid(row=11, column=1, padx=10, pady=10)
        
        registro.root.mainloop()
        
    def comprobacion_de_registro():
        registro.usuario = registro.usuario_Entry.get()
        registro.contraseña = registro.contraseña_Entry.get()
        registro.nombre = registro.nombre_Entry.get()
        registro.apellido = "admin"
        registro.cedula = registro.cedula_Entry.get()
        if registro.usuario == "" or registro.contraseña=="" or registro.nombre=="" or registro.apellido=="" or registro.cedula=="":
            errores_en_registro.en_blanco()
        else:
            registro.root.destroy()
            registro.comprobar = "si"
        
    def retroceder():
        registro.usuario =""
        registro.contraseña=""
        registro.nombre=""
        registro.apellido=""
        registro.cedula=""
        registro.root.destroy()
        registro.comprobar="no"
        
        
    def obtencion():
        return registro.usuario,registro.contraseña,registro.nombre,registro.apellido,registro.cedula