from vehiculo import Vehiculo

class Camioneta(Vehiculo):
    def __init__(self, modelo, patente, color, puertas):
        super().__init__(modelo, patente, color)
        self.puertas = puertas

    def mostrarDatos(self):
        super().mostrarDatos()
        print("Puertas:", self.puertas)