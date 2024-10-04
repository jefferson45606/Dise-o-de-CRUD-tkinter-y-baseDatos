from modelo.comprobacion.modeloUsuario import *
from vista.mensajes.mensajes_de_alerta import *
from bd.data_base import *

class guardado:
    def comprobacion_registro(usuario,contraseña,nombre,rol,cedula):
        conn = data_base_base.conectar_db()
        if conn:
            cursor = conn.cursor()
            data_base_base.crear_tablas(cursor)
            cursor.close()
            conn.close()
        data_base_base.conectar_db()
        resultado=data_base_base.agregar_usuario(cursor,cedula,usuario,contraseña,rol)
        if resultado == "usuario registrado":
            exito_en_registro.usuario_registrado()
        elif resultado == "ya registrado":
            errores_en_registro.usuario_ya_registrado()
            guardado.resultado == "registro"
        elif resultado == "llena campos":
            errores_en_registro.en_blanco()
            guardado.resultado = "registro"
        else:
            errores_en_registro.no_informacion()