#MUGISHA ALVIN ALLAN B33226
#OMARA CHRISPUS ADRIAN B33146
#KEJJE TEKA CHUANDRA B33242
#IYAMUMPAYE BRENDA B33237
def display_breakfast_menu():
    breakfast_menu = {
        1: "1. MILK TEA  AND MUFFINS       SHS.20000",
        2: "2. AFRICAN TEA  AND KATOGO      SHS. 15000"
    }
    print("\nBreakfast Menu:")
    for key, value in breakfast_menu.items():
        print(f"{key}. {value}")
    choice = int(input("Select an item by number: "))
    if choice in breakfast_menu:
        print(f"You ordered: {breakfast_menu[choice]}")
    else:
        print("Invalid choice.")

def display_lunch_menu():
    lunch_menu = {
        1: "1. CHIPS AND CHICKEN   SHS. 10000",
        2: "2.CHIPS,RICE AND LIVER SHS. 15000",
    }
    print("\nLunch Menu:")
    for key, value in lunch_menu.items():
        print(f"{key}. {value}")
    choice = int(input("Select an item by number: "))
    if choice in lunch_menu:
        print(f"You ordered: {lunch_menu[choice]}")
    else:
        print("Invalid choice.")

def main():
    print("Welcome to the Menu!")
    print("1. Breakfast")
    print("2. Lunch")
    
    menu_choice = input("Which menu would you like to see? (1 or 2): ")
    
    if menu_choice == "1":
        display_breakfast_menu()
    elif menu_choice == "2":
        display_lunch_menu()
    else:
        print("Invalid menu option.")

if __name__ == "__main__":
    main()
