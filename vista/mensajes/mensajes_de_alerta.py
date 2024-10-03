from tkinter import messagebox

class errores_en_registro:
    def usuario_ya_registrado():
        messagebox.showerror("Error", "El usuario ya se encuentra registrado")
        
    def en_blanco():
        messagebox.showerror("Error", "debe de llenar todas las casillas")
        
    def no_informacion():
        messagebox.showerror("Error", "No se encontro informacion")
        
class exito_en_registro():
        def usuario_registrado():
            messagebox.showinfo("Éxito", "Usuario registrado.")