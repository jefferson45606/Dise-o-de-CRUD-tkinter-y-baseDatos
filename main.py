from vista.arranque.vista_arranque import eleccion
from vista.arranque.vista_registro import registro
from vista.arranque.VistaInicioSesion import vistadeinicio
from controladores.controlador_de_informacion import b_d,guardado
from vista.acesso.catalogo import  inicio

class controlar:    
    def iniciar():
        inicio.registered_products = b_d.obtener_productos()
        registro.comprobar = ""
        eleccion.E = "eleccion"
        inicio.frames = {}
        while True:
            if eleccion.E == "iniciar":
                vistadeinicio.inicio()
                if vistadeinicio.comprobar == "si":
                    guardado.verificacion_inicio(vistadeinicio.usuario,vistadeinicio.contraseña)
                    if guardado.resultado=="exito":
                        eleccion.E = "catalogo"
                        guardado.resultado=""
                    elif guardado.resultado =="error":
                        eleccion.E = "iniciar"
                        guardado.resultado=""
                elif vistadeinicio.comprobar == "no":
                    eleccion.E = "eleccion"
                else:
                    eleccion.E = None
            elif eleccion.E == "registrarse":
                registro.inicio()
                if registro.comprobar == "si":
                    eleccion.E = "comprobar"
                elif registro.comprobar == "no":
                    eleccion.E = "eleccion"
                else:
                    eleccion.E = None
            elif eleccion.E == "eleccion":
                eleccion.E = None
                eleccion.arranque()
            elif eleccion.E == "comprobar":
                eleccion.E = None
                registro.comprobar = None
                usuario,contraseña,nombre,apellido,cedula=registro.obtencion()
                guardado.comprobacion_registro(usuario,contraseña,nombre,apellido,cedula)
                if guardado.resultado == "registro":
                    eleccion.E = "registrarse"
                    guardado.resultado = None
                else:
                    eleccion.E = "iniciar"
            elif eleccion.E == "catalogo":
                inicio.registered_products = b_d.obtener_productos()
                print(inicio.registered_products)
                inicio.iniciar()
                if inicio.confirmar == "si":
                    inicio.registered_products = b_d.obtener_productos()
                    print(inicio.registered_products)
                    inicio.confirmar = None
                    guardado.cargar_productos()
                elif inicio.confirmar == "no":
                    inicio.registered_products = b_d.obtener_productos()
                    print(inicio.registered_products)
                    eleccion.E = "catalogo"
                    inicio.confirmar = None
                elif inicio.confirmar == "actualizar":
                    guardado.actualizar_productos()
                    inicio.confirmar = None
                elif inicio.confirmar == "eliminar":
                    guardado.eliminar_registro()
            else:
                break
        
    def enviar():
        vistadeinicio.inicio()
        
controlar.iniciar()