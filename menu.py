# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Initialize order list
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    print("\nFrom which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # Get the customer's input
    menu_category = input("\nType menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            # Save the menu category name
            menu_category_name = menu_items[int(menu_category)]
            print(f"\nYou selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # Ask customer to input menu item number
            menu_selection = input("\nType menu item number: ")

            # Validate menu_selection is a number
            if menu_selection.isdigit():
                menu_selection = int(menu_selection)
                if menu_selection in menu_items.keys():
                    item_name = menu_items[menu_selection]["Item name"]
                    price = menu_items[menu_selection]["Price"]

                    # Ask for quantity
                    quantity = input(f"How many {item_name}s would you like? (default 1): ")
                    if not quantity.isdigit():
                        quantity = 1
                    else:
                        quantity = int(quantity)

                    # Add to order
                    order.append({
                        "Item name": item_name,
                        "Price": price,
                        "Quantity": quantity
                    })
                    print(f"Added {quantity} {item_name}(s) to your order.")
                else:
                    print("Invalid menu item number.")
            else:
                print("Invalid input. Please enter a number.")

        else:
            print("Invalid menu category.")
    else:
        print("Invalid input. Please enter a number.")

    # Ask if the customer wants to continue ordering
    while True:
        keep_ordering = input("Would you like to keep ordering? (Y/N): ").lower()
        match keep_ordering:
            case 'y':
                # Continue ordering
                break
            case 'n':
                # Stop ordering
                place_order = False
                print("\nThank you for your order!")
                break
            case _:
                # Invalid input
                print("Invalid input. Please enter Y or N.")

# Print the receipt
print("\nThis is what we are preparing for you.\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
for item in order:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]
    name_spaces = " " * (24 - len(item_name))
    print(f"{item_name}{name_spaces}| ${price:.2f}  | {quantity}")

# Calculate the total price
total = sum(item["Price"] * item["Quantity"] for item in order)
print("\nTotal Price: ${:.2f}".format(total))
