from controladorInforme import *
from modeloBaseDatos import *
from modeloInforme import *
from modeloproductos import *
from modeloUsuario import *
#from VistaCatalogo import *
from vistaInforme import *
from VistaInicioSesion import *
from VistarRegistroproductos import *
from vista_arranque import *
from vista_registro import *

class controlar:
    def __init__(self):
        pass
    
    def iniciar():
        eleccion.E = ""
        eleccion.arranque()
        if eleccion.E == "iniciar":
            vistadeinicio.inicio()
        elif eleccion.E == "registrarse":
            registro.inicio()
        else:
            pass
        
controlar.iniciar()