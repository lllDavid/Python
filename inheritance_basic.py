class Engine:
    def start(self):
        return "Engine starting"

class ElectricEngine(Engine):
    def start(self):
        return "Electric engine starting"

class GasEngine(Engine):
    def start(self):
        return "Gas engine starting"

class Car:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start_car(self):
        return self.engine_type.start()

class ElectricCar(Car):
    def __init__(self):
        super().__init__(ElectricEngine())  

class GasCar(Car):
    def __init__(self):
        super().__init__(GasEngine())  

electric_car = ElectricCar()
gas_car = GasCar()

print(electric_car.start_car())  
print(gas_car.start_car())  
