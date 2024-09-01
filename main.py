from vista.arranque.vista_arranque import *
from vista.arranque.vista_registro import *
from vista.arranque.VistaInicioSesion import *
from modelo.comprobacion.modeloUsuario import *

class controlar:    
    def iniciar():
        registro.comprobar = ""
        eleccion.E = "eleccion"
        while True:
            if eleccion.E == "iniciar":
                eleccion.E = None
                vistadeinicio.inicio()
            elif eleccion.E == "registrarse":
                registro.inicio()
                if registro.comprobar == "si":
                    eleccion.E = "comprobar"
                else:
                    eleccion.E = None
            elif eleccion.E == "eleccion":
                eleccion.E = None
                eleccion.arranque()
            elif eleccion.E == "comprobar":
                eleccion.E = None
                registro.comprobar = None
                
            else:
                break
        
    def enviar():
        vistadeinicio.inicio()
        
controlar.iniciar()