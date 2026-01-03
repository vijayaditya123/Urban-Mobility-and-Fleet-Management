class FleetHub:
    def __init__(self):
        self.hubs = {}  

    def add_hub(self, hub_name):
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []

    def add_vehicle(self, hub_name, vehicle):
        if hub_name not in self.hubs:
            raise ValueError("Hub does not exist")

        if vehicle in self.hubs[hub_name]:
            raise ValueError("Duplicate vehicle ID in this hub")

        self.hubs[hub_name].append(vehicle)

   

    def search_by_hub(self, hub_name):
        if hub_name not in self.hubs:
            return []
        return self.hubs[hub_name]

    def search_by_battery_above(self, percentage):
        return list(
            filter(
                lambda v: v.get_battery_percentage() > percentage,
                [v for vehicles in self.hubs.values() for v in vehicles]
            )
        )

    def group_by_vehicle_type(self):
        grouped = {}

        for vehicles in self.hubs.values():
         for vehicle in vehicles:
            vehicle_type = vehicle.__class__.__name__
            grouped.setdefault(vehicle_type, []).append(vehicle)

        return grouped
    def fleet_status_summary(self):
        summary = {
        "Available": 0,
        "On Trip": 0,
        "Under Maintenance": 0
        }

        for vehicles in self.hubs.values():
          for vehicle in vehicles:
            status = vehicle.get_maintenance_status()
            if status in summary:
                summary[status] += 1

        return summary
