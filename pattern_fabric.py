class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self, message):
        print(f"{self.make} {self.model}: {message}")

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
    def start_car_engine(self):
        self.start_engine("Двигун запущено")

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
    def start_motorcycle_engine(self):
        self.start_engine("Мотор заведено")

class VehicleFactory:
    def create_car(self, make, model):
        return Car(make, model)
    
    def create_motorcycle(self, make, model):
        return Motorcycle(make, model)
    
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        car = super().create_car(make, model)
        car.region = '(US Spec)'
        return car
    
    def create_motorcycle(self, make, model):
        motorcycle = super().create_motorcycle(make, model)
        motorcycle.region = '(US Spec)'
        return motorcycle
    
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        car = super().create_car(make, model)
        car.region = '(EU Spec)'
        return car
    
    def create_motorcycle(self, make, model):
        motorcycle = super().create_motorcycle(make, model)
        motorcycle.region = '(EU Spec)'
        return motorcycle

# Використання
US_car_factory = USVehicleFactory()
us_car = US_car_factory.create_car("Ford", "F-150")
us_car.start_car_engine()
print(us_car.make, us_car.model, us_car.region)

US_motorcycle_factory = USVehicleFactory()
us_motorcycle = US_motorcycle_factory.create_motorcycle("Harley-Davidson", "Sportster")
us_motorcycle.start_motorcycle_engine()
print(us_motorcycle.make, us_motorcycle.model, us_motorcycle.region)

EU_car_factory = EUVehicleFactory()
eu_car = EU_car_factory.create_car("BMW", "X5")
eu_car.start_car_engine()
print(eu_car.make, eu_car.model, eu_car.region)

EU_motorcycle_factory = EUVehicleFactory()
eu_motorcycle = EU_motorcycle_factory.create_motorcycle("Ducati", "Monster")
eu_motorcycle.start_motorcycle_engine()
print(eu_motorcycle.make, eu_motorcycle.model, eu_motorcycle.region)
