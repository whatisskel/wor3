
from interfaces.repository import Repository

class OrderRepository(Repository):
    def __init__(self):
        self.orders = {}

    def add(self, order):
        self.orders[order.order_id] = order

    def get(self, obj_id):
        return self.orders.get(obj_id)

    def list_all(self):
        return list(self.orders.values())

    def update(self, order):
        self.orders[order.order_id] = order

    def remove(self, obj_id):
        del self.orders[obj_id]
