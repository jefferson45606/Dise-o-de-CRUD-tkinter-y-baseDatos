# Pruebas de registro de usuario
from controlador_usuario import ControladorUsuario

# Crear instancia del controlador de usuario
controlador_usuario = ControladorUsuario()

# Datos de prueba para un nuevo usuario
usuario = "vendedor1"
password = "password123"
rol = "vendedor"

# Intentar registrar el usuario
if controlador_usuario.registrar_usuario(usuario, password, rol):
    print("Usuario registrado correctamente.")
else:
    print("El usuario ya existe.")