from modelo_producto import Producto

class ControladorProducto:
    def __init__(self):
        self.catalogo = []  # Aquí guardaremos los productos de manera temporal

    def agregar_producto(self, nombre, descripcion, precio, stock):
        id_producto = len(self.catalogo) + 1  # Generar un ID de producto simple
        nuevo_producto = Producto(id_producto, nombre, descripcion, precio, stock)
        self.catalogo.append(nuevo_producto)

    def obtener_productos(self):
        return self.catalogo

    def generar_informe_productos(self):
        try:
            # Crear un archivo de texto llamado "informe_productos.txt"
            with open("informe_productos.txt", "w") as archivo:
                archivo.write("Informe de Productos\n")
                archivo.write("=" * 50 + "\n")
                archivo.write(f"{'ID':<5} {'Nombre':<15} {'Descripción':<25} {'Precio':<10} {'Stock':<5}\n")
                archivo.write("-" * 50 + "\n")

                # Escribir los detalles de cada producto
                for producto in self.catalogo:
                    archivo.write(f"{producto.id_producto:<5} {producto.nombre:<15} {producto.descripcion:<25} {producto.precio:<10} {producto.stock:<5}\n")

            return True  # Si se genera el archivo correctamente
        except Exception as e:
            print(f"Error al generar el informe: {e}")
            return False  # Si ocurre un error
