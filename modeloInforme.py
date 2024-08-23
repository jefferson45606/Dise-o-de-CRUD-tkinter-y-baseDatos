class Informe:
    def __init__(self, productos):
        self.productos = productos

    def generarInforme(self):
        mas_vendidos = sorted(self.productos, key=lambda x: x.cantidad, reverse=True)[:5]
        menos_vendidos = sorted(self.productos, key=lambda x: x.cantidad)[:5]
        return mas_vendidos, menos_vendidos
