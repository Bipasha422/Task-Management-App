from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car started")
    def stop(self):
        print("car stop")
C=Car()
C.start()
C.stop()             