menu = {
    "cheese": 3,
    "milk": 10,
    "bread": 20,
    "coke": 14,
    "fanta": 14,
    "yoghurt": 25,
    "stony drink ": 15,
    "rice": 30,
    "maize": 25,
    "noodles": 10,
    "soap": 10
}

cart =[]
total = 0

print("------------MENU--------------------")
for key, value in menu.items():
    print(f"{key:10}: R{value:.2f}")

print("-------------------------------------")

while True:
    food = input("select an item (q to proceed to cart or cancel): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu[food]
    elif menu.get(food) != menu.items():
        print(f" We do not sell {food} here\n please enter the food in the list")


print("--------------------YOR ORDER--------------")
print("\nItems in your cart:")
for item in cart:
    print(f"- {item}: R{menu[item]:.2f}")
print(f"Total: R{total:.2f}")

print()
print(f"Total is: R{total:.2f}")

payment_amount = input("Enter amount you to pay: ")
payment = float(payment_amount)
if payment >= total:
    change = payment - total
    print(f"Your change is :R{change:.2f}")
    print("Thank you goodbye")
elif payment < total:
    short_amount = total - payment
    print(f"your payment is short by: R{short_amount}")
    add_amount = input("Do you want to add_amount or cancel  purchase (Yes/No)").lower()
    if add_amount == "yes":
        add_payment = float(input("Enter amount you want to add: "))
        change = add_payment - short_amount
        print(f"Your change is :R{change:.2f}")
        print("Thank you goodbye")
    else:
        print(" You do not afford , that okay we understand the economy is not good for everyone ")
else:
    print(" You do not afford , that okay we understand the economy is not good for everyone ")




