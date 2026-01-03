class FleetHub:
    def __init__(self):
        self.hubs = {}  # hub_name -> list of vehicles

    def add_hub(self, hub_name):
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []

    def add_vehicle(self, hub_name, vehicle):
        if hub_name not in self.hubs:
            raise ValueError("Hub does not exist")

        if vehicle in self.hubs[hub_name]:
            raise ValueError("Duplicate vehicle ID in this hub")

        self.hubs[hub_name].append(vehicle)
