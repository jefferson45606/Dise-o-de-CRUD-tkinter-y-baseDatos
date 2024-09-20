class ControladorProducto:
    def __init__(self):
        self.db_manager = DBManager()

    def registrar_producto(self, nombre, descripcion, precio, cantidad):
        consulta = "INSERT INTO productos (nombre, descripcion, precio, cantidad) VALUES (%s, %s, %s, %s)"
        return self.db_manager.ejecutar_consulta(consulta, (nombre, descripcion, precio, cantidad))

    def obtener_todos_los_productos(self):
        """Obtener todos los productos de la base de datos"""
        consulta = "SELECT * FROM productos"
        return self.db_manager.fetch_all(consulta)

    def buscar_producto_por_nombre(self, nombre):
        """Buscar productos en la base de datos por nombre"""
        consulta = "SELECT * FROM productos WHERE nombre LIKE %s"
        return self.db_manager.fetch_all(consulta, (f"%{nombre}%",))
