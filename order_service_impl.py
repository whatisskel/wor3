
from interfaces.order_service import OrderService
from models.order import Order

class OrderServiceImpl(OrderService):
    def __init__(self, order_repo, vehicle_repo, pricing_service):
        self.order_repo = order_repo
        self.vehicle_repo = vehicle_repo
        self.pricing_service = pricing_service
        self.next_id = 1

    def create_order(self, client_name, distance, cargo_type):
        order = Order(self.next_id, client_name, distance, cargo_type)
        self.order_repo.add(order)
        self.next_id += 1
        return order.order_id

    def assign_vehicle(self, order_id):
        order = self.order_repo.get(order_id)
        for vehicle in self.vehicle_repo.list_all():
            if vehicle.is_available():
                vehicle.assign()
                order.assign_vehicle(vehicle)
                self.order_repo.update(order)
                return True
        return False

    def calculate_price(self, order_id):
        order = self.order_repo.get(order_id)
        price = self.pricing_service.calculate(
            order.distance, order.vehicle.get_cost_per_km()
        )
        order.set_price(price)
        self.order_repo.update(order)
        return price

    def start_delivery(self, order_id):
        order = self.order_repo.get(order_id)
        order.start()
        self.order_repo.update(order)

    def get_order_status(self, order_id):
        order = self.order_repo.get(order_id)
        return order.status
