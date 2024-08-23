class controladorinforme:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def generarInforme(self):
        # Obtiene los productos más y menos vendidos desde el modelo
        masVendidos, menosVendidos = self.model.generarInforme()
        
        # este muestra la lista de productos más vendidos en la vista
        self.view.actualizar_mas_vendidos(masVendidos)
        
        # aqui se mustrar la lista de productos menos vendidos en la vista
        self.view.actualizar_menos_vendidos(menosVendidos)
        
        # para guardar el informe en un archivo de texto
        self.guardarInformeDeTxt(masVendidos, menosVendidos)

    def guardarInformeDeTxt(self, masVendidos, menosVendidos):
        with open("informe_productos.txt", "w") as file:
            file.write("Informe de Productos\n")
            file.write("Más Vendidos:\n")
            for producto in masVendidos:
                file.write(f"{producto.nombre}: {producto.cantidad}\n")
            file.write("\nMenos Vendidos:\n")
            for producto in menosVendidos:
                file.write(f"{producto.nombre}: {producto.cantidad}\n")
