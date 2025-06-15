# import math

# pie = math.pi
# print(pie)


# Create a list of items


grocery_items = ["Milk", "Juice", "Meat", "Eggs", "Maize Meal",
                 "Fish", "Spices", "Soup", "Washing Powder", "Rice"]
grocery_prices = [30, 20, 100, 60, 120, 150, 120, 60, 350, 300]
selected_items = []
cost_selected_items = []

# user_input = int(input(
#     "Please select grocery items by using numbers between 0 to 5, once done add -1: "))

# if user_input == 0:
#     selected_items.append(grocery_items[0])
#     pass
# elif user_input == 1:
#     selected_items.append(grocery_items[1])
#     pass
# elif user_input == 2:
#     selected_items.append(grocery_items[2])
#     pass
# elif user_input == 3:
#     selected_items.append(grocery_items[3])
#     pass
# elif user_input == 4:
#     selected_items.append(grocery_items[4])
#     pass
# elif user_input == -1:
#     print("Thank you for shopping with us!")
# else:
#     print("You have input invalid values, should be between -1 to 5")

# but i need a while to keep iterating or asking the user to input the values

# enumerate will keep the pair of index elements
for index, item in enumerate(grocery_items):
    print(f"{index}: {item} - R{grocery_prices[index]}")

while True:
    try:
        user_input = int(input("Select item number (0 - 4), or -1 to finish:"))

        if user_input == -1:
            break
        elif 0 <= user_input < len(grocery_items):
            selected_items.append(grocery_items[user_input])
        else:
            print(
                "Invalid number. Please enter a valid number (0 - 4) or -1 to exit cart")
    except ValueError:
        print("Please print a valid number")

print("Selected items: ")
for item in selected_items:
    print(f"- {item}")


def total_cost():
    return sum(grocery_prices)

# if there's milk in the selected item then add the price of milk in the empty list then return the total cost


def totalcost_selected_items():
    if "Milk" in selected_items:
        cost_selected_items.append(grocery_prices[0])
    if "Juice" in selected_items:
        cost_selected_items.append(grocery_prices[1])
    if "Meat" in selected_items:
        cost_selected_items.append(grocery_prices[2])
    if "Eggs" in selected_items:
        cost_selected_items.append(grocery_prices[3])
    if "Maize Meal" in selected_items:
        cost_selected_items.append(grocery_prices[4])
    if "Fish" in selected_items:
        cost_selected_items.append(grocery_prices[5])
    if "Spices" in selected_items:
        cost_selected_items.append(grocery_prices[6])
    if "Soup" in selected_items:
        cost_selected_items.append(grocery_prices[7])
    if "Washing powder" in selected_items:
        cost_selected_items.append(grocery_prices[8])
    if "Rice" in selected_items:
        cost_selected_items.append(grocery_prices[9])
    return sum(cost_selected_items)


costs_items = totalcost_selected_items()
print(f"Cost of selected items: R{costs_items}")

budget_input = int(input("How much money do you have?"))
# I need to catch any error if someone types anything beside the value


def cost(budget_input, costs_items):
    if budget_input >= costs_items:
        return print(
            f"You're within the budget and your change is R{budget_input - costs_items}")
    elif budget_input < costs_items:
        shortage_question = input("Do you want to add more money (YES/NO)?")
        if (shortage_question == "YES"):
            add_amount = int(input("How much money do you want to add?: "))
            adjusted_budget = add_amount + budget_input
            if (adjusted_budget >= costs_items):
                print(
                    f"You're within the budget and your change is R{adjusted_budget - costs_items}")
        elif shortage_question == "NO":
            print("Insufficient funds. You cannot make any purchase!")
    else:
        return print("Invalid input, please enter a number!")


print(cost(budget_input, costs_items))

# print("Selected items: ")
# for item in selected_items:
#     print(f"- {item}")

print(f"The total cost of all the grocery items: \n  {total_cost()}")

print(
    f"The total cost of all the selected items: {costs_items}")

print(f"The change: R{budget_input - costs_items}")

print("Thank you for shopping with us!")
