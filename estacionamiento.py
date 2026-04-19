class Estacionamiento:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.vehiculos = []  # lista donde guardo los autos

    def ingresarVehiculo(self, vehiculo):
        if len(self.vehiculos) >= self.capacidad:
            print("No hay cupos disponibles")
        else:
            self.vehiculos.append(vehiculo)
            print("Vehículo ingresado correctamente")

    def egresarVehiculo(self, patente):
        for i in self.vehiculos:
            if i.patente == patente:
                self.vehiculos.remove(i)
                print("Vehículo retirado correctamente")
                return
        print("Vehículo no encontrado")

    def mostrarEstado(self):
        print("Capacidad total:", self.capacidad)
        print("Autos dentro:", len(self.vehiculos))

        print("Listado de vehículos:")
        for i in self.vehiculos:
            print(i.patente, "-", i.modelo)