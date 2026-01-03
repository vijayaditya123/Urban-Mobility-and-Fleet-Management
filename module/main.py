from module.fleet_setup import FleetHub
from module.electric_car import ElectricCar
from module.electric_scooter import ElectricScooter

fleet = FleetHub()

while True:
    print("""
1. Add Hub
2. Add Vehicle
3. Display Hub Vehicles
4. Search by Hub Name
5. Search Battery > 80
6. Fleet Status Count
7. Sort by Model
8. Sort by Battery Level
9. Sort by Fare Price
10. Load from CSV
11. Save to CSV
12. Load from JSON
13. Save to JSON
0. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        hub = input("Enter hub name: ")
        fleet.add_hub(hub)

    elif choice == "2":
        hub = input("Enter hub name: ")
        vtype = input("Car or Scooter: ").lower()

        vid = input("Vehicle ID: ")
        model = input("Model: ")
        battery = int(input("Battery %: "))
        status = input("Status: ")
        price = float(input("Rental Price: "))

        if vtype == "car":
            seats = int(input("Seating Capacity: "))
            vehicle = ElectricCar(vid, model, battery, status, price, seats)
        else:
            speed = int(input("Max Speed: "))
            vehicle = ElectricScooter(vid, model, battery, status, price, speed)

        fleet.add_vehicle(hub, vehicle)

    elif choice == "3":
        hub = input("Enter hub name: ")
        for v in fleet.search_by_hub(hub):
            print(v)

    elif choice == "4":
        hub = input("Enter hub name: ")
        print(fleet.search_by_hub(hub))

    elif choice == "5":
        for v in fleet.search_battery_above_80():
            print(v)

    elif choice == "6":
        print(fleet.fleet_status_count())

    elif choice == "7":
        hub = input("Enter hub name: ")
        for v in fleet.sort_by_model(hub):
            print(v)

    elif choice == "8":
        fleet.sort_by_battery_level()
        print("Sorted by battery level")

    elif choice == "9":
        fleet.sort_by_fare_price()
        print("Sorted by fare price")

    elif choice == "10":
        fleet.load_from_csv()
        print("Loaded from CSV")

    elif choice == "11":
        fleet.save_to_csv()
        print("Saved to CSV")

    elif choice == "12":
        fleet.load_from_json()
        print("Loaded from JSON")

    elif choice == "13":
        fleet.save_to_json()
        print("Saved to JSON")

    elif choice == "0":
        break

    else:
        print("Invalid choice")
