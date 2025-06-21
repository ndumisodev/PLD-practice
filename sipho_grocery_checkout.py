# import math

# pie = math.pi
# print(pie)


# Create a list of items


grocery_items = ["Milk", "Juice", "Meat", "Eggs", "Maize Meal",
                 "Fish", "Spices", "Soup", "Washing Powder", "Rice"]
grocery_prices = [30, 20, 100, 60, 120, 150, 120, 60, 350, 300]
quantity_items = [5, 2, 3, 15, 20, 10, 7, 0, 1, 4]

selected_items = []
cost_selected_items = []

# Display grocery list
print("\nAvailable Items:\n")
for index, item in enumerate(grocery_items):
    print(
        f"{index}: {item} - R{grocery_prices[index]} - Stock: {quantity_items[index]}")

# Shopping selection loop
while True:
    try:
        user_input = int(
            input("\nSelect item number (0 - 9), or -1 to finish: "))

        if user_input == -1:
            break
        elif 0 <= user_input < len(grocery_items):
            if quantity_items[user_input] > 0:
                selected_items.append(grocery_items[user_input])
                cost_selected_items.append(grocery_prices[user_input])
                quantity_items[user_input] -= 1
                print(
                    f"{grocery_items[user_input]} added to cart. Remaining stock: {quantity_items[user_input]}")
            else:
                print(f"Sorry, {grocery_items[user_input]} is out of stock.")
        else:
            print("Invalid number. Choose between 0 - 9 or -1 to exit.")
    except ValueError:
        print("Please enter a valid number.")

# Print cart summary
print("\nSelected items:")
for item in set(selected_items):
    count = selected_items.count(item)
    print(f"- {item} x{count}")

# Calculate total cost


def total_cost_selected_items():
    return sum(cost_selected_items)


costs_items = total_cost_selected_items()
print(f"\nTotal cost of selected items: R{costs_items}")

# Ask for budget
while True:
    try:
        budget_input = int(input("How much money do you have? R"))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Handle cost decision


def handle_cost(budget_input, costs_items):
    while budget_input < costs_items:
        print(f"\nYou're short by R{costs_items - budget_input}")
        shortage_question = input(
            "Add money (YES), Remove items (RSI), or Cancel (NO)? ").strip().upper()

        if shortage_question == "YES":
            try:
                add_amount = int(input("Enter amount to add: R"))
                budget_input += add_amount
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif shortage_question == "RSI":
            if not selected_items:
                print("Your cart is empty. Nothing to remove.")
                break

            print(f"Cart items: {selected_items}")
            item_to_remove = input("Enter item name to remove: ").strip()

            if item_to_remove in selected_items:
                index_to_remove = selected_items.index(item_to_remove)
                selected_items.pop(index_to_remove)
                removed_cost = cost_selected_items.pop(index_to_remove)
                item_index = grocery_items.index(item_to_remove)
                quantity_items[item_index] += 1
                costs_items -= removed_cost
                print(f"{item_to_remove} removed. New total: R{costs_items}")
            else:
                print("Item not found in cart.")

        elif shortage_question == "NO":
            print("Transaction cancelled due to insufficient funds.")
            return

        else:
            print("Invalid choice. Please enter YES, RSI, or NO.")

# I need to add delivery cost should someone wants their food delivered at home.
# Based on the costs_items if its > R1000 free delivery but if not charge it based on the number of items

    if budget_input >= costs_items:
        print(
            f"\nTransaction successful! Your change is R{budget_input - costs_items}")


# Call cost handler
handle_cost(budget_input, costs_items)

print("Thank you for shopping with us!")
