from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self, power):
        self.power = power
    
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def perform_service(self):
        pass

class ElectricEngine(Engine):
    def __init__(self, power, battery_capacity):
        super().__init__(power)
        self.battery_capacity = battery_capacity
    
    def start(self):
        return f"Electric engine with {self.power} HP and {self.battery_capacity}kWh battery starting."

    def stop(self):
        return "Electric engine stopping."

    def get_type(self):
        return "Electric Engine"
    
    def perform_service(self):
        return "Performing battery health check and electrical system inspection."

class GasEngine(Engine):
    def __init__(self, power, fuel_efficiency):
        super().__init__(power)
        self.fuel_efficiency = fuel_efficiency
    
    def start(self):
        return f"Gas engine with {self.power} HP and {self.fuel_efficiency} MPG starting."

    def stop(self):
        return "Gas engine stopping."

    def get_type(self):
        return "Gas Engine"
    
    def perform_service(self):
        return "Performing engine oil change and fuel system cleaning."

class HybridEngine(Engine):
    def __init__(self, power, battery_capacity, fuel_efficiency):
        super().__init__(power)
        self.battery_capacity = battery_capacity
        self.fuel_efficiency = fuel_efficiency
    
    def start(self):
        return f"Hybrid engine with {self.power} HP, {self.battery_capacity}kWh battery, and {self.fuel_efficiency} MPG starting."

    def stop(self):
        return "Hybrid engine stopping."
    
    def get_type(self):
        return "Hybrid Engine"
    
    def perform_service(self):
        return "Performing both electric and fuel system maintenance."

class Car:
    def __init__(self, engine_type, model):
        self.engine_type = engine_type
        self.model = model
        self.is_running = False

    def start_car(self):
        if not self.is_running:
            self.is_running = True
            return f"{self.model}: {self.engine_type.start()}"
        return f"{self.model} is already running."

    def stop_car(self):
        if self.is_running:
            self.is_running = False
            return f"{self.model}: {self.engine_type.stop()}"
        return f"{self.model} is already stopped."

    def engine_details(self):
        return f"{self.model}: Engine Type: {self.engine_type.get_type()}"

    def perform_service(self):
        return f"{self.model}: {self.engine_type.perform_service()}"

    def switch_engine(self, new_engine):
        self.engine_type = new_engine
        return f"{self.model}: Switched to a new {self.engine_type.get_type()}."

class ElectricCar(Car):
    def __init__(self, model, power, battery_capacity):
        super().__init__(ElectricEngine(power, battery_capacity), model)

    def charge_car(self):
        return f"{self.model}: Charging battery."

class GasCar(Car):
    def __init__(self, model, power, fuel_efficiency):
        super().__init__(GasEngine(power, fuel_efficiency), model)

    def refuel_car(self):
        return f"{self.model}: Refueling gas tank."

class HybridCar(Car):
    def __init__(self, model, power, battery_capacity, fuel_efficiency):
        super().__init__(HybridEngine(power, battery_capacity, fuel_efficiency), model)

    def refuel_car(self):
        return f"{self.model}: Refueling and charging hybrid system."

    def charge_car(self):
        return f"{self.model}: Charging battery."

# Creating instances of different cars with different engine types
electric_car = ElectricCar("Tesla Model S", 350, 100)
gas_car = GasCar("Ford Mustang", 450, 25)
hybrid_car = HybridCar("Toyota Prius", 150, 13, 50)

# Starting, stopping, and servicing the cars
print(electric_car.start_car())
print(gas_car.start_car())
print(hybrid_car.start_car())

print(electric_car.perform_service())
print(gas_car.perform_service())
print(hybrid_car.perform_service())

# Switching engines dynamically
new_engine = GasEngine(500, 30)
electric_car.switch_engine(new_engine)

# Demonstrating different actions
print(electric_car.refuel_car())
print(gas_car.refuel_car())
print(hybrid_car.charge_car())

# Stopping the cars
print(electric_car.stop_car())
print(gas_car.stop_car())
print(hybrid_car.stop_car())

# Showing engine details
print(electric_car.engine_details())
print(gas_car.engine_details())
print(hybrid_car.engine_details())
