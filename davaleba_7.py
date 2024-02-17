from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, max_speed=0, current_speed=0):
        self.max_speed = max_speed
        self.current_speed = current_speed

    def start_engine(self):
        return "car started"

    def stop_engine(self):
        return "car stopped"

class SportCar(Car):
    def __init__(self, max_speed=0, current_speed=0):
        super().__init__(max_speed, current_speed)

    def start_engine(self):
        return "sport car started"

    def stop_engine(self):
        return "sport car stopped"
