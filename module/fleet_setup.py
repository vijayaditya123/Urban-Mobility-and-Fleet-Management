class Vehicle:
    def __init__(self, vehicle_id, model, battery_percentage, maintenance_status, rental_price):
        self.vehicle_id = vehicle_id
        self.model = model
        self.set_battery_percentage(battery_percentage)
        self.__maintenance_status = maintenance_status
        self.set_rental_price(rental_price)

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.vehicle_id == other.vehicle_id
        return False

    def get_maintenance_status(self):
        return self.__maintenance_status

    def set_maintenance_status(self, maintenance_status):
        self.__maintenance_status = maintenance_status

    def get_battery_percentage(self):
        return self.__battery_percentage

    def set_battery_percentage(self, battery_percentage):
        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            raise ValueError("Battery percentage must be between 0 and 100")

    def get_rental_price(self):
        return self.__rental_price

    def set_rental_price(self, rental_price):
        if rental_price > 0:
            self.__rental_price = rental_price
        else:
            raise ValueError("Rental price must be positive")

