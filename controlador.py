import json
from modelo import Database

class Controlador:
    def __init__(self):
        self.db = Database()
        self.db.conectar()
        self.db.crear_tablas()

    def registrar_usuario(self, id_usuario, usuario, contrasena, rol):
        self.db.agregar_usuario(id_usuario, usuario, contrasena, rol)

    def registrar_producto(self, nombre, descripcion, precio, cantidad_stock):
        self.db.agregar_producto(nombre, descripcion, precio, cantidad_stock)

    def iniciar_sesion(self, usuario, contrasena):
        return self.db.verificar_usuario(usuario, contrasena)

    def obtener_productos(self):
        return self.db.consultar_productos()

    def cerrar(self):
        self.db.cerrar_conexion()
        
def generar_informe(self):
    productos = self.obtener_productos()
    with open('informe_productos.txt', 'w') as f:
        for p in productos:
            f.write(f"ID: {p[0]}, Nombre: {p[1]}, Descripción: {p[2]}, Precio: {p[3]}, Cantidad: {p[4]}\n")
            
def generar_informe_json(self):
    productos = self.obtener_productos()
    with open('informe_productos.json', 'w') as f:
        json.dump(productos, f)
            


