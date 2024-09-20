from bd_manager import DBManager

class ControladorUsuario:
    def __init__(self):
        # Crear instancia de DBManager para gestionar la conexión a la base de datos
        self.db_manager = DBManager()

    def registrar_usuario(self, usuario, password, rol):
        """Registrar un nuevo usuario si no existe"""
        
        consulta = "SELECT * FROM usuarios WHERE usuario = %s"
        resultado = self.db_manager.fetch_all(consulta, (usuario,))
        if resultado:
            
            return False
        else:
            
            consulta = "INSERT INTO usuarios (usuario, password, rol) VALUES (%s, %s, %s)"
            self.db_manager.ejecutar_consulta(consulta, (usuario, password, rol))
            return True

    def validar_usuario(self, usuario, password):
        """Validar las credenciales de un usuario"""
        consulta = "SELECT * FROM usuarios WHERE usuario = %s AND password = %s"
        resultado = self.db_manager.fetch_all(consulta, (usuario, password))
        if resultado:
            return True
        else:
            return False

    def obtener_rol_usuario(self, usuario):
        """Obtener el rol del usuario dado su nombre de usuario"""
        consulta = "SELECT rol FROM usuarios WHERE usuario = %s"
        resultado = self.db_manager.fetch_all(consulta, (usuario,))
        if resultado:
            return resultado[0][0]  
        else:
            return None