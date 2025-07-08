class Menu:
    def __init__(self):
        self.breakfast_menu = {
            1: {"name": "Milk tea and bread", "price": 5000},
            2: {"name": "African tea and katogo", "price": 7000},
            3: {"name": "Juice, samosa and chaps", "price": 8000},
        }
        self.lunch_menu = {
            1: {"name": "Chips and liver", "price": 12000},
            2: {"name": "Pilau and beef", "price": 8900},
        }
        self.order = []

    def display_menu(self):
        print("Breakfast menu:")
        for key, value in self.breakfast_menu.items():
            print(f"{key}. {value['name']} - {value['price']} UGX")
        print("\nLunch menu:")
        for key, value in self.lunch_menu.items():
            print(f"{key}. {value['name']} - {value['price']} UGX")

    def take_order(self):
        print("\nWhat would you like to order?")
        print("1. Breakfast")
        print("2. Lunch")
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            menu_type = self.breakfast_menu
            menu_name = "Breakfast"
        elif choice == "2":
            menu_type = self.lunch_menu
            menu_name = "Lunch"
        else:
            print("Invalid choice.")
            return

        item = int(input(f"Select a {menu_name} item by number: "))
        if item in menu_type:
            self.order.append(menu_type[item])
            print(f"You ordered: {menu_type[item]['name']} - {menu_type[item]['price']} UGX")
        else:
            print("Invalid item selected.")

    def show_order(self):
        if not self.order:
            print("No items ordered yet.")
            return
        print("\nYour order:")
        total = 0
        for item in self.order:
            print(f"{item['name']} - {item['price']} UGX")
            total += item['price']
        print(f"Total: {total} UGX")

if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()
    menu.take_order()
    menu.show_order()