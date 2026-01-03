# Urban-Mobility-and-Fleet-Management
<br/>
Project Overview
<br/>
The Urban Mobility and Fleet Management System is a Python-based application designed to manage electric vehicle fleets operating across multiple urban hubs. The system allows administrators to create hubs, register vehicles, monitor fleet status, perform searching and sorting operations, and persist data using CSV and JSON formats. The project is built using object-oriented programming principles and simulates real-world fleet management operations in a structured and modular manner.

Objectives
<br/>
The main objectives of this project are to efficiently manage multiple fleet hubs, support different types of electric vehicles, track battery levels, maintenance status, and rental prices, provide analytics on fleet status, enable sorting and searching of vehicles, store and retrieve fleet data using files, and offer a command-line interface for user interaction.

System Architecture
<br/>
The project follows a modular architecture using Python packages. The module directory contains all core logic files including fleet setup, vehicle definitions, and the main execution file. The system separates responsibilities across multiple files to ensure clarity, scalability, and maintainability.

Core Components
<br/><br/>
Vehicle
<br/>
Vehicle is an abstract base class that defines common attributes such as vehicle ID, model, battery percentage, maintenance status, and rental price. It enforces the implementation of a calculate_trip_cost method in all subclasses.

ElectricCar
<br/>
ElectricCar extends the Vehicle class and adds seating capacity as an additional attribute. It implements its own logic for calculating trip cost.

ElectricScooter
<br/>
ElectricScooter extends the Vehicle class and adds maximum speed limit as an additional attribute. It also provides a specific trip cost calculation.

FleetHub
<br/>
FleetHub manages all hubs and vehicles. It allows adding hubs, registering vehicles under hubs, preventing duplicate vehicle IDs, searching vehicles by hub name and battery percentage, grouping vehicles by type, counting fleet status based on maintenance condition, sorting vehicles by model, battery level, and rental price, and saving and loading fleet data using CSV and JSON formats.

Command Line Interface
<br/>
The main.py file provides a menu-driven command-line interface. Users can interactively choose operations such as adding hubs, adding vehicles, displaying vehicles, performing searches, sorting fleet data, and saving or loading data from files.

Data Persistence
<br/>
The system supports CSV and JSON file handling. CSV is used for structured tabular storage, while JSON is used for hierarchical and readable data storage. This allows fleet data to persist across program executions.

Concepts Used
<br/>
The project uses object-oriented programming concepts including abstraction, inheritance, and polymorphism. It also demonstrates modular design, file handling, data structures like lists and dictionaries, functional programming constructs, and command-line based user interaction.

How to Run the Project
Navigate to the project root directory and run the application using the command:
python -m module.main

Final Outcome
The Urban Mobility and Fleet Management System successfully demonstrates a real-world application of Python programming concepts. It provides a scalable and extensible framework for managing electric vehicle fleets and can be further enhanced by adding databases, graphical interfaces, or real-time tracking features.
