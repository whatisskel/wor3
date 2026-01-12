
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_capacity(self):
        pass

    @abstractmethod
    def get_cost_per_km(self):
        pass

    @abstractmethod
    def is_available(self):
        pass

    @abstractmethod
    def assign(self):
        pass

    @abstractmethod
    def release(self):
        pass
