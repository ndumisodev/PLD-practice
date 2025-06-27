import math


def display_menu(menu_dict):
    print("Available Products and their price:")
    for key, value in menu_dict.items():
        name = value[0]  # product name
        price = value[2]  # price
        print(f"{key}. {name} - R{price}")


def item_selection(menu_dict):
    cart = []
    while True:
        food = int(input("select an item using numbers (0 to proceed to cart or cancel if you did not add any food): "))
        if food == 0:
            break
        elif food in menu_dict:
            item_name = menu_dict[food][0]   # the food name is in index 0
            available_quantity_in_stock = menu_dict[food][1]  # the second index in for quantity
            price = menu_dict[food][2]  # the third index if for the price not
            item_weight = menu_dict[food][3]  # weight of each product in grams

            quantity_input = int(input(f"enter the quantity of {item_name} -- R{price} you want: "))

            if quantity_input <= available_quantity_in_stock:
               total_price = quantity_input * price
               menu_dict[food][1] -= quantity_input
               delivary_cost = quantity_input * item_weight * (2/200)  # 200g cost R2 delivery
               delivary_cost_of_items = round(delivary_cost, 2)
               cart.append([item_name, price, quantity_input, total_price, delivary_cost_of_items])

               print(f'added {quantity_input} * {item_name} to cart')
            else:
                print(f"out of stock for {food}.and you want {quantity_input} and dwe have {available_quantity_in_stock}")

        else:
            print(f"we do not sell {food} here. enter the food by number in the list:  ")

    return cart


def checkout(payment, cart, total_amount_of_items, total_amount_of_delivary):


    if payment == "yes":
        amount_to_pay = float(input('Enter amount you want to pay: '))

        if amount_to_pay >= total_amount_of_items:
            change = amount_to_pay - total_amount_of_items
            print("\n*************** Free delivery for purchases of R1000 or more *******************")

            delivery_option = input("Do you want delivery or will you collect in store? (yes/no): ").lower()

            if delivery_option == "yes" and total_amount_of_items >= 1000:
                print(f"\nYour change is R{change:.2f}\nYou got free delivery since you spent R1000 or more.")
            elif delivery_option == "yes" and total_amount_of_items < 1000:
                print(f"\nDelivery fee is R{total_amount_of_delivary:.2f}")
                pay_delivery = float(input("Enter delivery fee amount to proceed: "))
                change = (amount_to_pay - total_amount_of_items) + (pay_delivery - total_amount_of_delivary)
                print(f"\nYour change is R{change:.2f}\nThank you, goodbye!")
            else:
                print(f"\nYour change is R{change:.2f}. Collect your items in Collection Room 411.")

        else:
            while amount_to_pay < total_amount_of_items:
                amount_short = total_amount_of_items - amount_to_pay
                print(f"\nYour money is short by R{amount_short:.2f}")
                try:
                    option = int(
                        input("Do you want to:\n1. Add more money\n2. Remove items from cart\nEnter option (1 or 2): "))
                    if option == 1:
                        add_amount = float(input("Enter additional amount: "))
                        amount_to_pay += add_amount
                    elif option == 2:
                        while True:
                            if not cart:
                                print("Your cart is empty. Cannot proceed.")
                                return

                            print("\nYour cart:")
                            for i, item in enumerate(cart):
                                print(f"{i + 1}. {item[0]} - quantity: {item[2]}, total: R{item[3]:.2f}")

                            try:
                                remove_index = int(input("Enter number of item to remove (0 to cancel): ")) - 1
                                if remove_index == -1:
                                    break
                                elif 0 <= remove_index < len(cart):
                                    removed_item = cart.pop(remove_index)
                                    print(f"Removed {removed_item[0]} from cart.")

                                    # Recalculate totals
                                    total_amount_of_items = sum(item[3] for item in cart)
                                    total_amount_of_delivary = sum(item[4] for item in cart)

                                    print(f"\nUpdated item total: R{total_amount_of_items:.2f}")
                                    print(f"Updated delivery total: R{total_amount_of_delivary:.2f}")

                                    # If cart total now less than amount paid, break and proceed
                                    if amount_to_pay >= total_amount_of_items:
                                        print("\nYou now have enough money.")
                                        break
                                else:
                                    print("Invalid item number.")
                            except ValueError:
                                print("Please enter a valid number.")
                    else:
                        print("Invalid option. Choose 1 or 2.")
                except ValueError:
                    print("Please enter a number.")

            # Finalize if enough after changes
            if amount_to_pay >= total_amount_of_items:
                change = amount_to_pay - total_amount_of_items
                delivery_option = input("Do you want delivery or collect in store? (yes/no): ").lower()

                if delivery_option == "yes" and total_amount_of_items >= 1000:
                    print(f"\nYour change is R{change:.2f}. Free delivery applied.")
                elif delivery_option == "yes":
                    print(f"\nDelivery fee is R{total_amount_of_delivary:.2f}")
                    pay_delivery = float(input("Enter delivery fee: "))
                    change = (amount_to_pay - total_amount_of_items) + (pay_delivery - total_amount_of_delivary)
                    print(f"\nYour change is R{change:.2f}. Thank you!")
                else:
                    print(f"\nYour change is R{change:.2f}. Collect from Collection Room 411.")

    elif payment == "no":
        print("You chose not to proceed. Cart cancelled.")
