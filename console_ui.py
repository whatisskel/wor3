
class ConsoleUI:
    def __init__(self, order_service):
        self.order_service = order_service

    def run(self):
        while True:
            print("\n1. Create order")
            print("2. Assign vehicle")
            print("3. Calculate price")
            print("4. Start delivery")
            print("5. Order status")
            print("0. Exit")

            choice = input("Choose: ")
            if choice == "1":
                name = input("Client name: ")
                dist = int(input("Distance: "))
                cargo = input("Cargo type: ")
                oid = self.order_service.create_order(name, dist, cargo)
                print("Order created with ID:", oid)

            elif choice == "2":
                oid = int(input("Order ID: "))
                print("Assigned:", self.order_service.assign_vehicle(oid))

            elif choice == "3":
                oid = int(input("Order ID: "))
                print("Price:", self.order_service.calculate_price(oid))

            elif choice == "4":
                oid = int(input("Order ID: "))
                self.order_service.start_delivery(oid)
                print("Delivery started")

            elif choice == "5":
                oid = int(input("Order ID: "))
                print("Status:", self.order_service.get_order_status(oid))

            elif choice == "0":
                break
