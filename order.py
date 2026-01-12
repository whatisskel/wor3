
class Order:
    def __init__(self, order_id, client_name, distance, cargo_type):
        self.order_id = order_id
        self.client_name = client_name
        self.distance = distance
        self.cargo_type = cargo_type
        self.vehicle = None
        self.price = 0
        self.status = "CREATED"

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.status = "VEHICLE_ASSIGNED"

    def set_price(self, price):
        self.price = price

    def start(self):
        self.status = "IN_PROGRESS"

    def complete(self):
        self.status = "COMPLETED"
