# Module 2 Challenge: Interactive Ordering System

## Description
This project implements an interactive ordering system for a food truck using Python. The program provides customers with a categorized menu, allows them to select items, specify quantities, and generates a receipt that includes the total price of all ordered items. The system ensures a smooth user experience with features like:

- **Input Validation**: Validates menu selections and quantity inputs to prevent errors.
- **Dynamic Menu Display**: Adapts to nested categories and subcategories within the menu.
- **Formatted Receipt**: Presents a clear and organized receipt, including item names, prices, quantities, and a calculated total.
- **Interactive Flow**: Customers can choose to add more items or complete their order.

The program uses Python data structures (dictionaries, lists) and control flow (loops, conditionals, match-case) to implement the interactive ordering process.

---

## How the Program Works
1. **Menu Setup**: 
   - The menu is stored in a nested dictionary structure with categories like "Snacks," "Meals," "Drinks," and "Dessert." Subcategories are used for specific items (e.g., different types of pizza or drinks).
   
2. **Order Initialization**: 
   - An empty list, `order`, is initialized to store customer selections. Each item in the list is a dictionary containing:
     - `Item name`: The name of the menu item.
     - `Price`: The price of the item.
     - `Quantity`: The quantity of the item ordered.

3. **Menu Display and Selection**:
   - Customers are presented with top-level menu categories. They can select a category by typing its corresponding number.
   - Once a category is selected, its items are displayed with names, prices, and item numbers for selection.

4. **Adding Items to the Order**:
   - Customers can select an item and specify the quantity. If the input for quantity is invalid, the program defaults it to 1.
   - The selected item, its price, and the specified quantity are added to the `order` list as a dictionary.

5. **Continuing or Ending the Order**:
   - After each item is added, the customer is asked whether they want to continue ordering. They can type "Y" or "N" (case-insensitive) to continue or end the session. Invalid responses prompt re-entry.

6. **Receipt Generation**:
   - Once the customer completes their order, the program generates a receipt. It loops through the `order` list, formats the item details with proper spacing, and calculates the total price using list comprehension.

7. **Total Calculation**:
   - The total price is computed by multiplying each item's price by its quantity and summing the results.

---

## Code Structure
The program is structured as follows:

1. **Menu Dictionary**:
   - Contains all categories, subcategories, and items with their respective prices.

2. **Order List**:
   - A list to store customer selections as dictionaries.

3. **Main Program**:
   - Handles menu display, input validation, order processing, and receipt generation.

4. **Receipt Formatting**:
   - Uses string manipulation to align columns for readability.

---

## How to Run
To run the program, follow these steps:

1. Clone the repository:
   git clone https://github.com/CCIEMikeG/python-challenge-1.git

2. Navigate to the project directory:
   cd python-challenge-1

3. Run the program:
   python menu.py


---

Welcome to the variety food truck.

From which menu would you like to order? 
1: Snacks
2: Meals
3: Drinks
4: Dessert
Type menu number: 1
You selected Snacks
What Snacks item would you like to order?
Item # | Item name                | Price
-------|--------------------------|-------
1      | Cookie                   | $0.99
2      | Banana                   | $0.69
3      | Apple                    | $0.49
4      | Granola bar              | $1.99
Type menu item number: 1
How many Cookies would you like? (default 1): 3
Added 3 Cookie(s) to your order.
Would you like to keep ordering? (Y/N): n

Thank you for your order!

---

Step 2: Receipt Display

This is what we are preparing for you.

Item name                 | Price  | Quantity
--------------------------|--------|----------
Cookie                    | $0.99  | 3

Total Price: $2.97


---

Acknowledgements

Starter code provided by the Module 2 Challenge instructions.
Guidance and support from course materials.
Shaw, Zed A. Learn Python the Hard Way. 3rd ed., Addison-Wesley, 2024.