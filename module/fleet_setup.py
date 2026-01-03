from abc import ABC, abstractmethod
import csv
from .electric_car import ElectricCar
from .electric_scooter import ElectricScooter
import json


class Vehicle(ABC):
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

    def __str__(self):
        return (
            f"ID: {self.vehicle_id}, "
            f"Model: {self.model}, "
            f"Battery: {self.__battery_percentage}%, "
            f"Status: {self.__maintenance_status}, "
            f"Fare: {self.__rental_price}"
        )

    def get_maintenance_status(self):
        return self.__maintenance_status

    def set_maintenance_status(self, status):
        self.__maintenance_status = status

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

    @abstractmethod
    def calculate_trip_cost(self, distance):
        pass


class FleetHub:
    def __init__(self):
        self.hubs = {}

    def add_hub(self, hub_name):
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []

    def add_vehicle(self, hub_name, vehicle):
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []

        if vehicle in self.hubs[hub_name]:
            print("Duplicate vehicle ID not allowed")
            return

        self.hubs[hub_name].append(vehicle)

    def display_hub(self):
        for hub, vehicles in self.hubs.items():
            print(f"\nHub: {hub}")
            for v in vehicles:
                print(v)

    def search_by_hub(self, hub_name):
        return self.hubs.get(hub_name, [])

    def search_battery_above_80(self):
        return [
            v
            for vehicles in self.hubs.values()
            for v in vehicles
            if v.get_battery_percentage() > 80
        ]

    def categorize_by_type(self):
        categories = {"Car": [], "Scooter": []}

        for vehicles in self.hubs.values():
            for v in vehicles:
                if isinstance(v, ElectricCar):
                    categories["Car"].append(v)
                elif isinstance(v, ElectricScooter):
                    categories["Scooter"].append(v)

        return categories

    def fleet_status_count(self):
        count = {
            "Available": 0,
            "On Trip": 0,
            "Under Maintenance": 0
        }

        for vehicles in self.hubs.values():
            for v in vehicles:
                status = v.get_maintenance_status()
                if status in count:
                    count[status] += 1

        return count

    def sort_by_model(self, hub_name):
        if hub_name not in self.hubs:
            return []

        self.hubs[hub_name] = sorted(
            self.hubs[hub_name],
            key=lambda v: v.model.lower()
        )
        return self.hubs[hub_name]

    def sort_by_battery_level(self):
        for hub, vehicles in self.hubs.items():
            self.hubs[hub] = sorted(
                vehicles,
                key=lambda v: v.get_battery_percentage(),
                reverse=True
            )

    def sort_by_fare_price(self):
        for hub, vehicles in self.hubs.items():
            self.hubs[hub] = sorted(
                vehicles,
                key=lambda v: v.get_rental_price(),
                reverse=True
            )

    def save_to_csv(self, filename="fleet_data.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "hub",
                "type",
                "vehicle_id",
                "model",
                "battery",
                "maintenance",
                "rental_price",
                "extra"
            ])

            for hub, vehicles in self.hubs.items():
                for v in vehicles:
                    if isinstance(v, ElectricCar):
                        writer.writerow([
                            hub,
                            "car",
                            v.vehicle_id,
                            v.model,
                            v.get_battery_percentage(),
                            v.get_maintenance_status(),
                            v.get_rental_price(),
                            v.seating_capacity
                        ])
                    elif isinstance(v, ElectricScooter):
                        writer.writerow([
                            hub,
                            "scooter",
                            v.vehicle_id,
                            v.model,
                            v.get_battery_percentage(),
                            v.get_maintenance_status(),
                            v.get_rental_price(),
                            v.max_speed_limit
                        ])

    def load_from_csv(self, filename="fleet_data.csv"):
        self.hubs = {}

        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                hub = row["hub"]

                if hub not in self.hubs:
                    self.hubs[hub] = []

                if row["type"] == "car":
                    vehicle = ElectricCar(
                        row["vehicle_id"],
                        row["model"],
                        int(row["battery"]),
                        row["maintenance"],
                        float(row["rental_price"]),
                        int(row["extra"])
                    )
                else:
                    vehicle = ElectricScooter(
                        row["vehicle_id"],
                        row["model"],
                        int(row["battery"]),
                        row["maintenance"],
                        float(row["rental_price"]),
                        int(row["extra"])
                    )

                self.hubs[hub].append(vehicle)
    def save_to_json(self, filename="fleet_data.json"):
        data = {}

        for hub, vehicles in self.hubs.items():
            data[hub] = []
            for v in vehicles:
                item = {
                    "type": v.__class__.__name__,
                    "vehicle_id": v.vehicle_id,
                    "model": v.model,
                    "battery": v.get_battery_percentage(),
                    "maintenance": v.get_maintenance_status(),
                    "rental_price": v.get_rental_price()
                }

                if isinstance(v, ElectricCar):
                    item["seating_capacity"] = v.seating_capacity
                else:
                    item["max_speed_limit"] = v.max_speed_limit

                data[hub].append(item)

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    def load_from_json(self, filename="fleet_data.json"):
        self.hubs = {}

        with open(filename, "r") as f:
            data = json.load(f)

        for hub, vehicles in data.items():
            self.hubs[hub] = []

            for v in vehicles:
                if v["type"] == "ElectricCar":
                    obj = ElectricCar(
                        v["vehicle_id"],
                        v["model"],
                        v["battery"],
                        v["maintenance"],
                        v["rental_price"],
                        v["seating_capacity"]
                    )
                else:
                    obj = ElectricScooter(
                        v["vehicle_id"],
                        v["model"],
                        v["battery"],
                        v["maintenance"],
                        v["rental_price"],
                        v["max_speed_limit"]
                    )

                self.hubs[hub].append(obj)
