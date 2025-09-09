# Process Abstraction EXample

from abc import ABC, abstractmethod

# Abstract base class
class vechile(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# child class car
class car(vechile):
    def start(self):
        print("Car started.......")

    def stop(self):
        print("Car stoped....")

class Bike(vechile):
    def start(self):
        print("Bike started.......")

    def stop(self):
        print("Bike stoped.....")

v1 = car()
v1.start()
v1.stop()
# Car started.......
# Car stoped....

v2 = Bike()
v2.start()
v2.stop()
# Bike started.......
# Bike stoped.....