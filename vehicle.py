import logging
from typing import Type

logging.basicConfig(level=logging.INFO)


class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self, message: str) -> None:
        logging.info(f"{self.make} {self.model}: {message}")


class Car(Vehicle):
    def __init__(self, make: str, model: str):
        super().__init__(make, model)

    def start_car_engine(self) -> None:
        self.start_engine("Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str):
        super().__init__(make, model)

    def start_motorcycle_engine(self) -> None:
        self.start_engine("Мотор заведено")


class VehicleFactory:
    def create_car(self, make: str, model: str) -> Type[Car]:
        return Car(make, model)

    def create_motorcycle(self, make: str, model: str) -> Type[Motorcycle]:
        return Motorcycle(make, model)


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Type[Car]:
        car = super().create_car(make, model)
        car.region = "(US Spec)"
        return car

    def create_motorcycle(self, make: str, model: str) -> Type[Motorcycle]:
        motorcycle = super().create_motorcycle(make, model)
        motorcycle.region = "(US Spec)"
        return motorcycle


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Type[Car]:
        car = super().create_car(make, model)
        car.region = "(EU Spec)"
        return car

    def create_motorcycle(self, make: str, model: str) -> Type[Motorcycle]:
        motorcycle = super().create_motorcycle(make, model)
        motorcycle.region = "(EU Spec)"
        return motorcycle


# Використання
US_car_factory = USVehicleFactory()
us_car = US_car_factory.create_car("Ford", "F-150")
us_car.start_car_engine()
logging.info(us_car.make, us_car.model, us_car.region)

US_motorcycle_factory = USVehicleFactory()
us_motorcycle = US_motorcycle_factory.create_motorcycle("Harley-Davidson", "Sportster")
us_motorcycle.start_motorcycle_engine()
logging.info(us_motorcycle.make, us_motorcycle.model, us_motorcycle.region)

EU_car_factory = EUVehicleFactory()
eu_car = EU_car_factory.create_car("BMW", "X5")
eu_car.start_car_engine()
logging.info(eu_car.make, eu_car.model, eu_car.region)

EU_motorcycle_factory = EUVehicleFactory()
eu_motorcycle = EU_motorcycle_factory.create_motorcycle("Ducati", "Monster")
eu_motorcycle.start_motorcycle_engine()
logging.info(eu_motorcycle.make, eu_motorcycle.model, eu_motorcycle.region)
