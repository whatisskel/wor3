
from repositories.order_repository import OrderRepository
from repositories.vehicle_repository import VehicleRepository
from services.pricing_service import PricingService
from services.order_service_impl import OrderServiceImpl
from models.truck import Truck
from models.van import Van
from ui.console_ui import ConsoleUI

def main():
    order_repo = OrderRepository()
    vehicle_repo = VehicleRepository()

    vehicle_repo.add(Truck(1))
    vehicle_repo.add(Van(2))

    pricing_service = PricingService()
    order_service = OrderServiceImpl(order_repo, vehicle_repo, pricing_service)

    ui = ConsoleUI(order_service)
    ui.run()

if __name__ == "__main__":
    main()
