
from interfaces.repository import Repository

class VehicleRepository(Repository):
    def __init__(self):
        self.vehicles = {}

    def add(self, vehicle):
        self.vehicles[vehicle.vehicle_id] = vehicle

    def get(self, obj_id):
        return self.vehicles.get(obj_id)

    def list_all(self):
        return list(self.vehicles.values())

    def update(self, vehicle):
        self.vehicles[vehicle.vehicle_id] = vehicle

    def remove(self, obj_id):
        del self.vehicles[obj_id]
