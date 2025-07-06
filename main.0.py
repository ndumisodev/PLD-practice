from tkinter import *

root = Tk()
root.title("Grocery Cart")
root.geometry("1270x685")
root.iconbitmap("billing.ico")

# Configure main window grid
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

# Heading
headingLabel = Label(root,
                     text="Grocery Billing System",
                     font=("times new roman", 30, "bold"),
                     bg="lightblue",
                     fg="black",
                     bd=12,
                     relief=RIDGE)
headingLabel.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

# Customer Details Frame
customer_details_frame = LabelFrame(root,
                                    text="Customer Details",
                                    font=("times new roman", 15, "bold"),
                                    fg="black",
                                    bg="lightblue",
                                    bd=8,
                                    relief=RIDGE)
customer_details_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)


Label(customer_details_frame, text="Name", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=0, column=0, padx=10, pady=5)
Entry(customer_details_frame, font=("arial", 15), bd=5).grid(row=0, column=1, padx=10)

Label(customer_details_frame, text="Phone", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=0, column=2, padx=10, pady=5)
Entry(customer_details_frame, font=("arial", 15), bd=5).grid(row=0, column=3, padx=10)

Label(customer_details_frame, text="Bill Number", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=0, column=4, padx=10, pady=5)
Entry(customer_details_frame, font=("arial", 15), bd=5).grid(row=0, column=5, padx=10)

Button(customer_details_frame, text="SEARCH", font=("arial", 12, "bold"), bd=5, relief=RAISED, padx=20).grid(row=0, column=6, padx=10)

# Main Product Frames
productsFrame = Frame(root)
productsFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

productsFrame.columnconfigure((0, 1, 2, 3), weight=1)

# Cosmetics Frame
cosmeticsFrame = LabelFrame(productsFrame, text='Cosmetics', font=("times new roman", 15, "bold"),
                            fg='black', bg='lightblue', bd=8, relief=RIDGE)
cosmeticsFrame.grid(row=0, column=0, padx=5, sticky="nsew")

Label(cosmeticsFrame, text="Bath Soap", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=0, column=0, sticky="w", pady=5)
Entry(cosmeticsFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=0, column=1, padx=5, pady=5)

Label(cosmeticsFrame, text="Face Cream", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=1, column=0, sticky="w", pady=5)
Entry(cosmeticsFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=1, column=1, padx=5, pady=5)

Label(cosmeticsFrame, text="Face Wash", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=2, column=0, sticky="w", pady=5)
Entry(cosmeticsFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=2, column=1, padx=5, pady=5)

Label(cosmeticsFrame, text="Hair Spray", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=3, column=0, sticky="w", pady=5)
Entry(cosmeticsFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=3, column=1, padx=5, pady=5)

Label(cosmeticsFrame, text="Hair Gel", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=4, column=0, sticky="w", pady=5)
Entry(cosmeticsFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=4, column=1, padx=5, pady=5)

Label(cosmeticsFrame, text="Body Lotion", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=5, column=0, sticky="w", pady=5)
Entry(cosmeticsFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=5, column=1, padx=5, pady=5)

# Grocery Frame
groceryFrame = LabelFrame(productsFrame, text='Grocery', font=("times new roman", 15, "bold"),
                          fg='black', bg='lightblue', bd=8, relief=RIDGE)
groceryFrame.grid(row=0, column=1, padx=5, sticky="nsew")

Label(groceryFrame, text="Rice", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=0, column=0, sticky="w", pady=5)
Entry(groceryFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=0, column=1, padx=5, pady=5)

Label(groceryFrame, text="Oil", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=1, column=0, sticky="w", pady=5)
Entry(groceryFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=1, column=1, padx=5, pady=5)

Label(groceryFrame, text="Daal", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=2, column=0, sticky="w", pady=5)
Entry(groceryFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=2, column=1, padx=5, pady=5)

Label(groceryFrame, text="Wheat", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=3, column=0, sticky="w", pady=5)
Entry(groceryFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=3, column=1, padx=5, pady=5)

Label(groceryFrame, text="Sugar", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=4, column=0, sticky="w", pady=5)
Entry(groceryFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=4, column=1, padx=5, pady=5)

Label(groceryFrame, text="Tea", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=5, column=0, sticky="w", pady=5)
Entry(groceryFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=5, column=1, padx=5, pady=5)

# Drinks Frame
drinksFrame = LabelFrame(productsFrame, text='Drinks', font=("times new roman", 15, "bold"),
                         fg='black', bg='lightblue', bd=8, relief=RIDGE)
drinksFrame.grid(row=0, column=2, padx=5, sticky="nsew")

Label(drinksFrame, text="Coke", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=0, column=0, sticky="w", pady=5)
Entry(drinksFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=0, column=1, padx=5, pady=5)

Label(drinksFrame, text="Pepsi", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=1, column=0, sticky="w", pady=5)
Entry(drinksFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=1, column=1, padx=5, pady=5)

Label(drinksFrame, text="Sprite", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=2, column=0, sticky="w", pady=5)
Entry(drinksFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=2, column=1, padx=5, pady=5)

Label(drinksFrame, text="Fanta", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=3, column=0, sticky="w", pady=5)
Entry(drinksFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=3, column=1, padx=5, pady=5)

Label(drinksFrame, text="Mooza", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=4, column=0, sticky="w", pady=5)
Entry(drinksFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=4, column=1, padx=5, pady=5)

Label(drinksFrame, text="Lemon Twist", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=5, column=0, sticky="w", pady=5)
Entry(drinksFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=5, column=1, padx=5, pady=5)

# Bill Area
billframe = Frame(productsFrame, bd=8, relief=RIDGE)
billframe.grid(row=0, column=3, padx=5, sticky="nsew")

Label(billframe, text="Bill Area", font=("times new roman", 15, "bold"), fg="black", bg="lightblue", bd=8, relief=RIDGE).pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billframe, font=("arial", 15), yscrollcommand=scrollbar.set)
textarea.pack(fill=BOTH, expand=True)

scrollbar.config(command=textarea.yview)

# Bill Menu
billmenuFrame = LabelFrame(root, text="Bill Menu", font=("times new roman", 15, "bold"),
                           fg="black", bg="lightblue", bd=8, relief=RIDGE)
billmenuFrame.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

Label(billmenuFrame, text="Cosmetic Price", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=0, column=0, padx=10, pady=5, sticky="w")
Entry(billmenuFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=0, column=1, padx=5)

Label(billmenuFrame, text="Grocery Price", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=1, column=0, padx=10, pady=5, sticky="w")
Entry(billmenuFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=1, column=1, padx=5)

Label(billmenuFrame, text="Cold Drink Price", font=("times new roman", 15, "bold"), fg="blue", bg="lightblue").grid(row=2, column=0, padx=10, pady=5, sticky="w")
Entry(billmenuFrame, font=("arial", 15, "bold"), bd=5, width=10).grid(row=2, column=1, padx=5)

root.mainloop()
