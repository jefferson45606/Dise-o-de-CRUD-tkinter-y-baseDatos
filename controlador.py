class Controlador:
    def __init__(self):
        # Diccionario temporal con usuarios y contraseñas
        # Esto se puede mover luego a una base de datos
        self.usuarios = {
            "vendedor": "12345",
            "admin": "67891"
        }

    def validar_credenciales(self, usuario, password):
        # Comprueba si el usuario y la contraseña son correctos
        return self.usuarios.get(usuario) == password