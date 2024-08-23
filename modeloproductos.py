class Producto:
    def __init__(self, id, nombre, categoria, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def Dictar(self):
        return {  
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad
        }
