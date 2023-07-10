from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0.0:
                self.started = True
            else:
                raise LowFuelError(f"Кончился бензин")

    def move(self, road):
        if self. fuel - (road* self.fuel_consumption) >= 0:
            self.fuel = self. fuel - (road * self.fuel_consumption)
        else:
            raise NotEnoughFuel(f"Не хватает топлива для перемещения")

