import modules
import math

menu_dict = {
    1: ["milk 500l", 20, 10, 515],  # key, item, quantity, price, weight in grams ( using density)
    2: ["milk 1l", 10, 20, 1030],
    3: ["coke 500ml", 10, 11, 500],
    4: ["fanta 500ml", 11, 10, 500],
    5: ["stony 500ml", 3, 10, 500],
    6: ["sprite 500ml", 7, 10, 500],
    7: ["coke 1l", 50, 18, 1000],
    8: ["fanta 1l", 13, 16, 1000],
    9: ["stony 1l", 15, 16, 1000],
    10: ["sprite 1l", 18,  16, 1000],
    11: ["cheese slice", 20, 3, 28],
    12: ["eggs 6 pack", 33, 14, 348],
    13: ["rama 500g", 15,  13, 500],
    14: ["russian 60g", 60, 8, 60],
    15: ["arch 500g", 14, 50, 500],
    16: ["sugar 500g", 60, 14, 500],
    17: ["frisco 200g", 55,  23, 200],
    18: ["fries 71g", 13,  10, 71],
    19: ["fries 117g", 32, 16, 117],
    20: ["fries 190g", 10, 16, 1000],

}


print("*******************************************menu items ***********************************")
modules.display_menu(menu_dict)

print("*******************************************Purchasing ***********************************")
cart = modules.item_selection(menu_dict)
print("******************************************** Your cart ************************************")
total_amount_of_items = 0
total_amount_of_delivary = 0
for items in cart:
    print(f"{items[0]}--R{items[1]}\n quantity : {items[2]}, \n total price: R{items[3]},\n delivary cost R{items[4]}\n")
    total_amount_of_items += items[3]
    total_amount_of_delivary += items[4]

print(f"total amount to pay: R{total_amount_of_items: .2f}\ntotal amount od delivary: R{total_amount_of_delivary: .2f}")


payment = input("procced to payment yes or no: ").lower()

print("************************************payment***************************************")
modules.checkout(payment, cart, total_amount_of_items, total_amount_of_delivary)
