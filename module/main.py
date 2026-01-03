from module.electric_car import ElectricCar
from module.electric_scooter import ElectricScooter

vehicles = [
    ElectricCar("C1", "Tesla", 90, "OK", 100, 5),
    ElectricScooter("S1", "Ola", 80, "OK", 30, 60)
]

for v in vehicles:
    print(v.calculate_trip_cost(10))
