class Cafeteria:
    def __init__(self):
        self.menu = {}  # Dictionary to store menu items and prices
        self.orders = []  # List to store orders

    def add_menu_item(self, item, price):
        """Add or update a menu item."""
        self.menu[item] = price
        print(f"Menu item '{item}' added with price ${price:.2f}")

    def display_menu(self):
        """Display the menu."""
        if not self.menu:
            print("Menu is empty.")
            return
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")

    def place_order(self):
        """Place an order and calculate the total amount."""
        order = {}
        total_amount = 0.0

        print("Enter items to order (type 'done' when finished):")
        while True:
            item = input("Item: ").strip()
            if item.lower() == 'done':
                break
            if item in self.menu:
                quantity = int(input(f"Quantity of {item}: "))
                if item in order:
                    order[item] += quantity
                else:
                    order[item] = quantity
                total_amount += self.menu[item] * quantity
            else:
                print(f"'{item}' is not on the menu.")

        if order:
            self.orders.append(order)
            print("\nOrder Summary:")
            for item, quantity in order.items():
                print(f"{item}: {quantity} x ${self.menu[item]:.2f}")
            print(f"Total Amount: ${total_amount:.2f}")
        else:
            print("No items were ordered.")

    def show_orders(self):
        """Display all placed orders."""
        if not self.orders:
            print("No orders have been placed.")
            return
        print("Orders:")
        for idx, order in enumerate(self.orders, start=1):
            print(f"Order {idx}:")
            total_amount = 0.0
            for item, quantity in order.items():
                print(f"  {item}: {quantity} x ${self.menu[item]:.2f}")
                total_amount += self.menu[item] * quantity
            print(f"  Total Amount: ${total_amount:.2f}")

def main():
    cafeteria = Cafeteria()

    # Adding some items to the menu
    cafeteria.add_menu_item("Burger", 5.99)
    cafeteria.add_menu_item("Fries", 2.49)
    cafeteria.add_menu_item("Soda", 1.99)
    cafeteria.add_menu_item("Coffee", 2.99)

    while True:
        print("\nCafeteria Management System")
        print("1. Display Menu")
        print("2. Place Order")
        print("3. Show Orders")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            cafeteria.display_menu()
        elif choice == '2':
            cafeteria.place_order()
        elif choice == '3':
            cafeteria.show_orders()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
