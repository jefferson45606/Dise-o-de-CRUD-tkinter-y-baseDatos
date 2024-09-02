from modelo.comprobacion.modeloUsuario import *

class guardado:
    def comprobacion(datos):
        Usuario.usuario
        Usuario.contraseña
        Usuario.Nombre
        Usuario.Apellido
        Usuario.Cedula
        try:
            resultado = comparacion(Usuario.usuario,Usuario.contraseña)
        except:
            pass
    
#------------------linea privada---------------------------------------------
def comparacion(usuario,contraseña):
    with open("guardados/usuarios.txt","r") as comprobar:
        pass