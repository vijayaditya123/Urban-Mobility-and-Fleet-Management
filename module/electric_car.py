from module.fleet_setup import Vehicle

class ElectricCar(Vehicle):
    def __init__(
        self,
        vehicle_id,
        model,
        battery_percentage,
        maintenance_status,
        rental_price,
        seating_capacity
    ):
        super().__init__(
            vehicle_id,
            model,
            battery_percentage,
            maintenance_status,
            rental_price
        )
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):
        return 5 + (0.5 * distance)


