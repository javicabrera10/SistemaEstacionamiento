from auto import Auto
from camioneta import Camioneta
from estacionamiento import Estacionamiento



playa = Estacionamiento(3)

# Crear autos
auto1 = Auto("Chevrolet", "AAA111", "Rojo", 4)
auto2 = Auto("Ford", "BBB222", "Azul", 4)

# creo camioneta
camioneta1 = Camioneta("wolsvagen","afg123","verde",2)

# Ingresar autos
playa.ingresarVehiculo(auto1)
playa.ingresarVehiculo(auto2)
playa.ingresarVehiculo(camioneta1)

# Intentar uno más (sin cupo)
auto3 = Auto("Fiat", "CCC333", "Negro", 4)
playa.ingresarVehiculo(auto3)

# Mostrar estado
playa.mostrarEstado()

# Egreso
playa.egresarVehiculo("AAA111")

# Mostrar de nuevo
playa.mostrarEstado()