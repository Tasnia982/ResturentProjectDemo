def restaurant():
    print("----------------- Welcome to Our Restaurant Sir / Madam -----------------")
    
    menu = {
        "Burger": 5.99,
        "Pizza": 7.99,
        "Sandwich": 6.99,
        "Salad": 4.99,
        "Black Coffee": 1.99,
        "White Coffee": 1.99,
        "Cappuccino": 2.99,
        "Tea": 1.99,
        "Ice Cream": 3.99,
        "Falooda": 4.99,
        "Set menu": 9.99, 
        "Combo": 10.99,
        "Cool Drinks": 1.99,
        "Orange Juice": 2.99,
        "Chocolate Milkshake": 3.99
    }

    print("Here are our menu items:")
    for item, price in menu.items():
        print(f"- {item} - ${price:.2f}")

    print("-------------------------------------------------------------------------")

    total_order = 0

    while True:
        select_item = input("Please select your choice of food from the menu above: ")
        
        if select_item in menu:
            total_order += menu[select_item]
            print(f"Your item '{select_item}' has been added to your order.")
        else:
            print("Invalid choice, please select a valid item from the menu.")

        option = input("Do you want to add anything else? (yes/no): ").strip().lower()
        if option != "yes":
            break

    print("-------------------------------------------------------------------------")
    print(f"The total cost of your order is ${total_order:.2f}")
    print("Thank you for your order. We will prepare your food.")

restaurant()

while True:
    again = input("Do you want to order again? (yes/no): ").strip().lower()
    
    if again == "yes":
        print("Welcome back to our restaurant!")
        print("-----------------------------------------------------------------------------")
        restaurant()
    else:
        print("Thank you for coming.")
        print("Exit")
        break
