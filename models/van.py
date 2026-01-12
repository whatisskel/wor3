
from interfaces.vehicle import Vehicle

class Van(Vehicle):
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.capacity = 3000
        self.cost_per_km = 3
        self.available = True

    def get_capacity(self):
        return self.capacity

    def get_cost_per_km(self):
        return self.cost_per_km

    def is_available(self):
        return self.available

    def assign(self):
        self.available = False

    def release(self):
        self.available = True
