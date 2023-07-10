from homework_02.base import Vehicle

"""
создайте класс `Car`, наследник `Vehicle`
"""


class Car(Vehicle):
    engine = "default"

    def set_engine(self, Engine):
        self.engine = Engine
