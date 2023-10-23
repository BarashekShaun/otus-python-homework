from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload
"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        if (cargo + self.cargo) <= self.max_cargo:
            self.cargo = cargo
        else:
            raise CargoOverload(f"Перегруз")

    def remove_all_cargo(self):
        remove = self.cargo
        self.cargo = 0
        return remove
