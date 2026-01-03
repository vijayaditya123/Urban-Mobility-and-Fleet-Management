from module.fleet_setup import Vehicle

class ElectricScooter(Vehicle):
    def __init__(
        self,
        vehicle_id,
        model,
        battery_percentage,
        maintenance_status,
        rental_price,
        max_speed_limit
    ):
        super().__init__(
            vehicle_id,
            model,
            battery_percentage,
            maintenance_status,
            rental_price
        )
        self.max_speed_limit = max_speed_limit

    
    def calculate_trip_cost(self, minutes):
        return 1.0 + (0.15 * minutes)


