# Program to sell Products

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        if item.name in self.inventory:
            self.inventory[item.name].quantity += quantity
        else:
            self.inventory[item.name] = item

    def display_inventory(self):
        print("Current Inventory:")
        for item in self.inventory.values():
            print(f"{item.name}: ${item.price} - Quantity: {item.quantity}")

    def sell_item(self, item_name, quantity):
        if item_name in self.inventory:
            item = self.inventory[item_name]
            if item.quantity >= quantity:
                item.quantity -= quantity
                total_price = item.price * quantity
                print(f"Sold {quantity} {item_name}(s) for ${total_price}")
            else:
                print("Insufficient quantity.")
        else:
            print("Item not found in inventory.")

def main():
    store = Store()

    # Adding initial items to the store
    items = {
        'Turmeric powder': {"Quantity in 'Packets'": 100, "Price": 150},
        'Sugar': {"Quantity in 'Packets'": 100, "Price": 180},
        'Rice': {"Quantity in 'Packets'": 100, "Price": 300},
        'Brown Rice': {"Quantity in 'Packets'": 100, "Price": 350},
        'Wheat Flour': {"Quantity in 'Packets'": 100, "Price": 400},
        'Maida': {"Quantity in 'Packets'": 100, "Price": 280},
        'Soybean powder': {"Quantity in 'Packets'": 100, "Price": 280},
        'Red Chilli Powder': {"Quantity in 'Packets'": 100, "Price": 500},
        'Garlic Powder': {"Quantity in 'Packets'": 100, "Price": 150},
        'Instant Noodles': {"Quantity in 'Packets'": 100, "Price": 100},
        'Cereals': {"Quantity in 'Packets'": 100, "Price": 200},
        'Bread': {"Quantity in 'Packets'": 100, "Price": 280},
        'Pulses': {"Quantity in 'Packets'": 100, "Price": 250},
        'Crystal Salt': {"Quantity in 'Packets'": 100, "Price": 70},
        'Powder Salt': {"Quantity in 'Packets'": 100, "Price": 90},
        'Chat Masala': {"Quantity in 'Packets'": 100, "Price": 150},
        'Pepper Powder': {"Quantity in 'Packets'": 100, "Price": 150},
        'Instant Coffee': {"Quantity in 'Packets'": 100, "Price": 300},
        'Tea': {"Quantity in 'Packets'": 100, "Price": 180},
        'Cooking oil': {"Quantity in 'Packets'": 100, "Price": 470},
        'Ghee': {"Quantity in 'Packets'": 100, "Price": 450},
        'Raisins': {"Quantity in 'Packets'": 100, "Price": 780},
        'Nuts': {"Quantity in 'Packets'": 100, "Price": 1000},
        'Peanuts': {"Quantity in 'Packets'": 100, "Price": 100},
        'Dates': {"Quantity in 'Packets'": 100, "Price": 230},
        'Vanilla Essence': {"Quantity in 'Packets'": 100, "Price": 100},
        'Pasta': {"Quantity in 'Packets'": 100, "Price": 290},
        'Cocoa Powder': {"Quantity in 'Packets'": 100, "Price": 150},
        'Macaroni': {"Quantity in 'Packets'": 100, "Price": 180},
        'Mayonaisse': {"Quantity in 'Packets'": 100, "Price": 80},
        'Tomato Ketchup': {"Quantity in 'Packets'": 100, "Price": 430},
        'Beverages': {"Quantity in 'Packets'": 100, "Price": 270},
        'Cheese block': {"Quantity in 'Packets'": 100, "Price": 570},
        'Fresh cream': {"Quantity in 'Packets'": 100, "Price": 140},
        'Milk Pack': {"Quantity in 'Packets'": 100, "Price": 150},
        'Toothpaste': {"Quantity in 'Packets'": 100, "Price": 170},
        'Toothbrush': {"Quantity in 'Packets'": 100, "Price": 120},
        'Bathing Soap': {"Quantity in 'Packets'": 100, "Price": 170},
        'Shampoo': {"Quantity in 'Packets'": 100, "Price": 270},
        'Shaving cream': {"Quantity in 'Packets'": 100, "Price": 320},
        'Lays Snacks': {"Quantity in 'Packets'": 100, "Price": 50},
        'Cheetos Snacks': {"Quantity in 'Packets'": 100, "Price": 50},
        'Doritos Snacks': {"Quantity in 'Packets'": 100, "Price": 100},
        'Candles Snacks': {"Quantity in 'Packets'": 100, "Price": 50},
        'Batteries': {"Quantity in 'Packets'": 100, "Price": 200},
        'Light bulbs': {"Quantity in 'Packets'": 100, "Price": 350},
        'Bandages': {"Quantity in 'Packets'": 100, "Price": 50}
    }

    for item_name, item_details in items.items():
        item = Item(item_name, item_details["Price"], item_details["Quantity in 'Packets'"])
        store.add_item(item, item_details["Quantity in 'Packets'"])

    while True:
        print("\n1. Display Inventory")
        print("2. Sell Item")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            store.display_inventory()
        elif choice == "2":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            store.sell_item(item_name, quantity)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



#                     *****************  REVENUE & GST *****************
def Revenue(sales_revenue, other_revenue):  # REVENUE
    Gross_Revenue = sales_revenue + other_revenue  # Sales Revenue + Other Revenue
    return Gross_Revenue  # GROSS REVENUE

def GST(sales_revenue, other_revenue):  # Taxes
    General_Sales_Tax = Revenue(sales_revenue, other_revenue) * 18 / 100
    return General_Sales_Tax

sales_revenue = 50000
other_revenue = 50000
gross_revenue = Revenue(sales_revenue, other_revenue)
# print("Gross Revenue:", gross_revenue) #print Gross Revenue
general_sales_tax = GST(sales_revenue, other_revenue)
# print("General Sales Tax:", general_sales_tax) #print General Sales Tax

#                     ***************** Ending REVENUE & GST *****************

#                        **********  Employs Wages  **********
def Employs_Wages():
    employ_Wages = {
        'Sales Associates': [
            {'Name': 'Ali', 'Salary': 35000,},
            {'Name': 'Ahmed', 'Salary': 32000},
            {'Name': 'Omer', 'Salary': 34000},
        ],
        'Customer Service Representatives': [
            {'Name': 'Fasee', 'Salary': 35000},
        ],
        'Cashiers': [
            {'Name': 'Zahid', 'Salary': 20000},
            {'Name': 'Aarham', 'Salary': 22000},
            {'Name': 'Hamza', 'Salary': 24000},
        ],
        'Visual Merchandisers': [
            {'Name': 'Hassan', 'Salary': 15000},
            {'Name': 'Usman', 'Salary': 17000},
        ],
        'Managers': [
            {'Name': 'M.Roshaan Riaz', 'Salary': 55000},
        ],
        'Inventory Control Specialist': [
            {'Name': 'M.Umer', 'Salary': 45000},
        ]
    }
    return employ_Wages


def calculate_total_wages():
    total_wages = 0
    for employee_type, employees in Employs_Wages().items():
        print(f"\n{employee_type}:")
        for employee in employees:
            print(f"Name: {employee['Name']}, Salary: {employee['Salary']}")
            total_wages += employee['Salary']
        print()  # Adding an empty line for better readability between job titles
    return total_wages

# total_wages = calculate_total_wages()  # Print Wages With Name & Specilization
# print("\nTotal Wages:", total_wages)  # Print Total Wages
#
#
# #                               **********Employs Wages End**********
# # ////////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# #                                  **********Expenses**********
#
# def Rent():  # Rent / Mortgage
#     Rent: int = 50000
#     return Rent
#
#
# def Utilities():  # Utilities
#     Utilities: int = 5000
#     return Utilities
#
#
# def Office_Supplies():  # Office Supplies
#     Office_Supplies: int = 10000
#     return Office_Supplies
#
#
# def Internet_Phone():  # Internet & Phone
#     Internet_Phone: int = 5000
#     return Internet_Phone
#
#
# def Travel():  # Travel
#     Travel: int = 10000
#     return Travel
#
#
# def Miscellaneous_Expenses():  # Taxes
#     Miscellaneous_Expenses: int = 10000
#     return Miscellaneous_Expenses
#
#
# def Expenses():  # EXPENSES
#     Total_Expense = total_wages + Rent() + Utilities() + Office_Supplies() + Internet_Phone() + Travel() + Miscellaneous_Expenses()+general_sales_tax # Wages and Benefits
#     return Total_Expense
# print(Expenses())
#                                  **********Expenses Ends Here**********



# COST OF GOODS SOLD
# COGS
# TOTAL COGS


# GROSS PROFIT
# Gross Revenue - COGS

# NET INCOME
# Gross Profit - Total Expenses

# ____________________Final Product_________________________________
#
#
# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def Save_Item(self,filename='Items.jason'):
#         data={
#             'name':self.name,
#             'price':self.price,
#             'quantity':self.quantity
#         }
#         try:
#             with open(filename, 'w') as file:
#                 json.dump(data, file)
#         except IOError:
#             print("Error: Unable to save item data to file.")
#
# class Store:
#     def __init__(self):
#         self.inventory = {}
#         self.sales_revenue = 0
#         self.other_revenue = 0
#
#     def add_item(self, item, quantity):
#         if item.name in self.inventory:
#             self.inventory[item.name].quantity += quantity
#         else:
#             self.inventory[item.name] = item
#
#     def display_inventory(self):
#         print("Current Inventory:")
#         for item in self.inventory.values():
#             print(f"{item.name}: ${item.price} - Quantity: {item.quantity}")
#
#     def sell_item(self, item_name, quantity):
#         if item_name in self.inventory:
#             item = self.inventory[item_name]
#             if item.quantity >= quantity:
#                 item.quantity -= quantity
#                 total_price = item.price * quantity
#                 print(f"Sold {quantity} {item_name}(s) for ${total_price}")
#                 self.sales_revenue += total_price
#             else:
#                 print("Insufficient quantity.")
#         else:
#             print("Item not found in inventory.")
#
# def Revenue(sales_revenue, other_revenue):  # REVENUE
#     Gross_Revenue = sales_revenue + other_revenue  # Sales Revenue + Other Revenue
#     return Gross_Revenue  # GROSS REVENUE
#
# def main():
#     store = Store()
#
#     # Adding initial items to the store
#     items = {
#         'Turmeric powder': {"Quantity in 'Packets'": 100, "Price": 150},
#         'Sugar': {"Quantity in 'Packets'": 100, "Price": 180},
#         'Rice': {"Quantity in 'Packets'": 100, "Price": 300},
#         'Brown Rice': {"Quantity in 'Packets'": 100, "Price": 350},
#         'Wheat Flour': {"Quantity in 'Packets'": 100, "Price": 400},
#         'Maida': {"Quantity in 'Packets'": 100, "Price": 280},
#         'Soybean powder': {"Quantity in 'Packets'": 100, "Price": 280},
#         'Red Chilli Powder': {"Quantity in 'Packets'": 100, "Price": 500},
#         'Garlic Powder': {"Quantity in 'Packets'": 100, "Price": 150},
#         'Instant Noodles': {"Quantity in 'Packets'": 100, "Price": 100},
#         'Cereals': {"Quantity in 'Packets'": 100, "Price": 200},
#         'Bread': {"Quantity in 'Packets'": 100, "Price": 280},
#         'Pulses': {"Quantity in 'Packets'": 100, "Price": 250},
#         'Crystal Salt': {"Quantity in 'Packets'": 100, "Price": 70},
#         'Powder Salt': {"Quantity in 'Packets'": 100, "Price": 90},
#         'Chat Masala': {"Quantity in 'Packets'": 100, "Price": 150},
#         'Pepper Powder': {"Quantity in 'Packets'": 100, "Price": 150},
#         'Instant Coffee': {"Quantity in 'Packets'": 100, "Price": 300},
#         'Tea': {"Quantity in 'Packets'": 100, "Price": 180},
#         'Cooking oil': {"Quantity in 'Packets'": 100, "Price": 470},
#         'Ghee': {"Quantity in 'Packets'": 100, "Price": 450},
#         'Raisins': {"Quantity in 'Packets'": 100, "Price": 780},
#         'Nuts': {"Quantity in 'Packets'": 100, "Price": 1000},
#         'Peanuts': {"Quantity in 'Packets'": 100, "Price": 100},
#         'Dates': {"Quantity in 'Packets'": 100, "Price": 230},
#         'Vanilla Essence': {"Quantity in 'Packets'": 100, "Price": 100},
#         'Pasta': {"Quantity in 'Packets'": 100, "Price": 290},
#         'Cocoa Powder': {"Quantity in 'Packets'": 100, "Price": 150},
#         'Macaroni': {"Quantity in 'Packets'": 100, "Price": 180},
#         'Mayonaisse': {"Quantity in 'Packets'": 100, "Price": 80},
#         'Tomato Ketchup': {"Quantity in 'Packets'": 100, "Price": 430},
#         'Beverages': {"Quantity in 'Packets'": 100, "Price": 270},
#         'Cheese block': {"Quantity in 'Packets'": 100, "Price": 570},
#         'Fresh cream': {"Quantity in 'Packets'": 100, "Price": 140},
#         'Milk Pack': {"Quantity in 'Packets'": 100, "Price": 150},
#         'Toothpaste': {"Quantity in 'Packets'": 100, "Price": 170},
#         'Toothbrush': {"Quantity in 'Packets'": 100, "Price": 120},
#         'Bathing Soap': {"Quantity in 'Packets'": 100, "Price": 170},
#         'Shampoo': {"Quantity in 'Packets'": 100, "Price": 270},
#         'Shaving cream': {"Quantity in 'Packets'": 100, "Price": 320},
#         'Lays Snacks': {"Quantity in 'Packets'": 100, "Price": 50},
#         'Cheetos Snacks': {"Quantity in 'Packets'": 100, "Price": 50},
#         'Doritos Snacks': {"Quantity in 'Packets'": 100, "Price": 100},
#         'Candles Snacks': {"Quantity in 'Packets'": 100, "Price": 50},
#         'Batteries': {"Quantity in 'Packets'": 100, "Price": 200},
#         'Light bulbs': {"Quantity in 'Packets'": 100, "Price": 350},
#         'Bandages': {"Quantity in 'Packets'": 100, "Price": 50}
#     }
#
#     for item_name, item_details in items.items():
#         item = Item(item_name, item_details["Price"], item_details["Quantity in 'Packets'"])
#         store.add_item(item, item_details["Quantity in 'Packets'"])
#
#     while True:
#         print("\n1. Display Inventory")
#         print("2. Sell Item")
#         print("3. Calculate Revenue")
#         print("4. Calculate Expenses")
#         print("5. Exit")
#
#         choice = input("Enter your choice: ")
#
#         if choice == "1":
#             store.display_inventory()
#         elif choice == "2":
#             item_name = input("Enter item name: ")
#             quantity = int(input("Enter quantity: "))
#             store.sell_item(item_name, quantity)
#         elif choice == "3":
#             total_revenue = Revenue(store.sales_revenue, store.other_revenue)
#             print(f"Total Revenue: ${total_revenue}")
#         elif choice == "4":
#             total_expenses = Expenses()
#             print(f"Total Expenses: ${total_expenses}")
#         elif choice == "5":
#             print("Exiting program.")
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
# if __name__ == "__main__":
#     main()
#
# def Revenue(sales_revenue, other_revenue):  # REVENUE
#     Gross_Revenue = sales_revenue + other_revenue  # Sales Revenue + Other Revenue
#     return Gross_Revenue  # GROSS REVENUE
#
# def GST(sales_revenue, other_revenue):  # Taxes
#     General_Sales_Tax = Revenue(sales_revenue, other_revenue) * 18 / 100
#     return General_Sales_Tax
#
# def Employs_Wages():
#     employ_Wages = {
#         'Sales Associates': [
#             {'Name': 'Ali', 'Salary': 35000,},
#             {'Name': 'Ahmed', 'Salary': 32000},
#             {'Name': 'Omer', 'Salary': 34000},
#         ],
#         'Customer Service Representatives': [
#             {'Name': 'Fasee', 'Salary': 35000},
#         ],
#         'Cashiers': [
#             {'Name': 'Zahid', 'Salary': 20000},
#             {'Name': 'Aarham', 'Salary': 22000},
#             {'Name': 'Hamza', 'Salary': 24000},
#         ],
#         'Visual Merchandisers': [
#             {'Name': 'Hassan', 'Salary': 15000},
#             {'Name': 'Usman', 'Salary': 17000},
#         ],
#         'Managers': [
#             {'Name': 'M.Roshaan Riaz', 'Salary': 55000},
#         ],
#         'Inventory Control Specialist': [
#             {'Name': 'M.Umer', 'Salary': 45000},
#         ]
#     }
#     return employ_Wages
#
# def calculate_total_wages():
#     total_wages = 0
#     for employee_type, employees in Employs_Wages().items():
#         print(f"\n{employee_type}:")
#         for employee in employees:
#             print(f"Name: {employee['Name']}, Salary: {employee['Salary']}")
#             total_wages += employee['Salary']
#         print()  # Adding an empty line for better readability between job titles
#     return total_wages
#
# # print(calculate_total_wages())
# print("\nTotal Wages:", total_wages)
#
# def Rent():  # Rent / Mortgage
#     Rent: int = 50000
#     return Rent
#
#
# def Utilities():  # Utilities
#     Utilities: int = 5000
#     return Utilities
#
#
# def Office_Supplies():  # Office Supplies
#     Office_Supplies: int = 10000
#     return Office_Supplies
#
#
# def Internet_Phone():  # Internet & Phone
#     Internet_Phone: int = 5000
#     return Internet_Phone
#
#
# def Travel():  # Travel
#     Travel: int = 10000
#     return Travel
#
#
# def Miscellaneous_Expenses():  # Taxes
#     Miscellaneous_Expenses: int = 10000
#     return Miscellaneous_Expenses
#
# def Expenses():  # EXPENSES
#     total_expense = calculate_total_wages()+ Rent() + Utilities() + Office_Supplies() + Internet_Phone() + Travel() + Miscellaneous_Expenses()
#     return total_expense

#-------------------------------------------------------------------------

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def save_item(self, filename='Items.txt'):
        data = f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}\n"
        try:
            with open(filename, 'a') as file:
                file.write(data)
        except IOError as e:
            print(f"Error: Unable to save item data to file: {e}")

class Store:
    def __init__(self):
        self.inventory = {}
        self.sales_revenue = 0
        self.other_revenue = 0

    def add_item(self, item, quantity):
        if item.name in self.inventory:
            self.inventory[item.name].quantity += quantity
        else:
            self.inventory[item.name] = item

    def display_inventory(self):
        print("Current Inventory:")
        for item in self.inventory.values():
            print(f"{item.name}: ${item.price} - Quantity: {item.quantity}")

    def sell_item(self, item_name, quantity):
        if item_name in self.inventory:
            item = self.inventory[item_name]
            if item.quantity >= quantity:
                item.quantity -= quantity
                total_price = item.price * quantity
                print(f"Sold {quantity} {item_name}(s) for ${total_price}")
                self.sales_revenue += total_price
            else:
                print("Insufficient quantity.")
        else:
            print("Item not found in inventory.")

def calculate_total_expenses():
    expenses = {
        'Rent': 50000,
        'Utilities': 5000,
        'Office Supplies': 10000,
        'Internet & Phone': 5000,
        'Travel': 10000,
        'Miscellaneous': 10000
    }
    return sum(expenses.values())

def calculate_total_wages():
    wages = {
        'Sales Associates': 35000,
        'Customer Service Representatives': 35000,
        'Cashiers': 22000,
        'Visual Merchandisers': 17000,
        'Managers': 55000,
        'Inventory Control Specialist': 45000
    }
    return sum(wages.values())

def calculate_gst(sales_revenue, other_revenue):
    return (sales_revenue + other_revenue) * 0.18

def calculate_total_revenue(sales_revenue, other_revenue):
    return sales_revenue + other_revenue

def main():
    store = Store()


    items = {
        'Turmeric powder': {"Quantity in 'Packets'": 100, "Price": 150},
        'Sugar': {"Quantity in 'Packets'": 100, "Price": 180},
        'Rice': {"Quantity in 'Packets'": 100, "Price": 300},

    }

    for item_name, item_details in items.items():
        item = Item(item_name, item_details["Price"], item_details["Quantity in 'Packets'"])
        store.add_item(item, item_details["Quantity in 'Packets'"])

    while True:
        print("\n1. Display Inventory")
        print("2. Sell Item")
        print("3. Calculate Revenue")
        print("4. Calculate Expenses")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            store.display_inventory()
        elif choice == "2":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity in 'Packets': "))
            store.sell_item(item_name, quantity)
        elif choice == "3":
            total_revenue = calculate_total_revenue(store.sales_revenue, store.other_revenue)
            print(f"Total Revenue: Rs:{total_revenue}")
        elif choice == "4":
            total_expenses = calculate_total_expenses()
            print(f"Total Monthly Expenses: Rs:{total_expenses}")
        elif choice == "5":
            print("Generating report...")
            total_revenue = calculate_total_revenue(store.sales_revenue, store.other_revenue)
            total_expenses = calculate_total_expenses()
            total_profit = total_revenue - total_expenses
            gst = calculate_gst(store.sales_revenue, store.other_revenue)

            print("\n----- REPORT -----")
            print(f"\nTotal Revenue: Rs:{total_revenue}")
            print(f"\nTotal Expenses Monthly: Rs:{total_expenses}")
            print(f"\nTotal Profit Monthly: Rs:{total_profit/30}")
            print(f"\nGST: Rs:{gst}")
            print("------------------")

            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()