
from abc import ABC, abstractmethod

class OrderService(ABC):
    @abstractmethod
    def create_order(self, client_name, distance, cargo_type):
        pass

    @abstractmethod
    def assign_vehicle(self, order_id):
        pass

    @abstractmethod
    def calculate_price(self, order_id):
        pass

    @abstractmethod
    def start_delivery(self, order_id):
        pass

    @abstractmethod
    def get_order_status(self, order_id):
        pass
