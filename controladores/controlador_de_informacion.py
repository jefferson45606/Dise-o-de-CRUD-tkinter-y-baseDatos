from vista.mensajes.mensajes_de_alerta import errores_en_registro,exito_en_registro,inicio_de_sesion_me
from vista.acesso.catalogo import inicio
from bd.data_base import b_d
class guardado:
    def comprobacion_registro(usuario,contraseña,nombre,rol,cedula):
        guardado.resultado=b_d.registrar_usuario_gui(cedula,nombre,contraseña,rol)
        if guardado.resultado == "usuario registrado":
            exito_en_registro.usuario_registrado()
        elif guardado.resultado == "ya registrado":
            errores_en_registro.usuario_ya_registrado()
            guardado.resultado == "registro"
        elif guardado.resultado == "llena campos":
            errores_en_registro.en_blanco()
            guardado.resultado = "registro"
        else:
            errores_en_registro.no_informacion()
            
    def verificacion_inicio(usuario,contraseña):
        if b_d.verificar_usuario(usuario, contraseña):
            inicio_de_sesion_me.inicio_exito()
            guardado.resultado="exito"
        else:
            inicio_de_sesion_me.inicio_error()
            guardado.resultado="error"
        
    def cargar_productos():
        b_d.agregar_avena(inicio.codigo, inicio.name, inicio.description, inicio.price, inicio.ventas, inicio.image_path)
        
    def actualizar_productos():
        b_d.actualizar(inicio.codigo, inicio.name, inicio.description, inicio.price, inicio.ventas, inicio.image_path)
        
    def eliminar_registro():
        b_d.eliminar(inicio.codigo)