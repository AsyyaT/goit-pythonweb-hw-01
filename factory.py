import logging
from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(f"{make} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Car:
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make, model) -> Motorcycle:
        return Motorcycle(f"{make} (EU Spec)", model)


def create_vehicle(factory: VehicleFactory):
    car = factory.create_car("Ford", "Mustang")
    motorcycle = factory.create_motorcycle("Harley-Davidson", "Sportster")

    car.start_engine()
    motorcycle.start_engine()


us_factory = USVehicleFactory()
create_vehicle(us_factory)

eu_factory = EUVehicleFactory()
create_vehicle(eu_factory)
