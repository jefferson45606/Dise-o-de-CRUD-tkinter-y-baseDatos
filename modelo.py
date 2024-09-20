import json

class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock
        }

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

class Usuario:
    def __init__(self, usuario_id, nombre, rol):
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.rol = rol

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def generar_informe(self, filename):
        with open(filename, 'w') as file:
            for producto in self.productos:
                file.write(f"{producto.nombre} - {producto.precio} - {producto.stock}\n")

    def guardar_en_json(self, filename):
        with open(filename, 'w') as file:
            json.dump([producto.to_dict() for producto in self.productos], file, indent=4)