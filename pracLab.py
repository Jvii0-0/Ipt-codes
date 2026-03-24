menu = {
    "americano": 85.0,
    "latte": 95.0,
    "cappuccino": 100.0,
    "mocha": 110.0,
    "espresso": 75.0
}

def display_menu():
    for i in menu:
        print(f"{i} - {menu[i]}")

def add_item():
    while True:
        item = input("Add item (exit to stop): ")
        if item == "exit":
            break
        price = float(input("Enter price: "))
        menu[item] = price

def process_order(menu):
    order = {}

    # take orders
    while True:
        item = input("Order item (done to finish): ").strip().lower()
        if item == "done":
            break
        if item not in menu:
            print("Not in menu.")
            continue

        try:
            qty = int(input("Qty: "))
            if qty <= 0:
                print("Invalid qty.")
                continue
        except:
            print("Invalid qty.")
            continue

        order[item] = order.get(item, 0) + qty

    if not order:
        return

    # discount
    disc = {"R":0, "SC":0.2, "PD":0.2, "VP":0.1}
    while True:
        d = input("Type (R/SC/PD/VP): ").upper()
        if d in disc:
            break
        print("Invalid.")

    # compute
    total = 0
    print("\nRECEIPT")
    for item, qty in order.items():
        sub = menu[item] * qty
        total += sub
        print(f"{item.title()} x{qty} - ₱{sub:.2f}")

    discount = total * disc[d]
    grand = total - discount

    print(f"Total: ₱{total:.2f}")
    print(f"Discount: ₱{discount:.2f}")
    print(f"Grand Total: ₱{grand:.2f}")

def remove_item():
    item = input("Item to remove: ")

    if item in menu:
         del menu[item]
         print("Item removed")
    else:
        print("Item not found")

def change_item(menu):
    old = input("Item to change: ")

    if old in menu:
        new = input("Item to add: ")

        menu[new] = menu[old]
        del menu[old]

        print("Item changed")
    else:
        print("Item not found")

def change_price():
    item = input("Item to update: ").lower()

    if item in menu:
        try:
            new_price = float(input("New price: "))
            menu[item] = new_price
            print("Updated")
        except:
            print("invalid price")
    else:
        print("not found")

def main():
    while True:
        print("""
              1: Menu
              2: Add
              3: Order
              4: Exit
              5: Remove item
              6: Change price
              7: Change item
              """)
        ch = input("Choice: ")

        if ch == "1":
            display_menu()
        elif ch == "2":
            add_item()
        elif ch == "3":
            process_order(menu)
        elif ch == "5":
            remove_item()
        elif ch == "6":
            change_price()
        elif ch == "7":
            change_item(menu)

main()

##raw_orders = """
##Americano, 85
##latte ,95.0
##CAPPUCCINO, one hundred
##Mocha,110.00
##espresso,75
##americano , 
##Latte,  95 pesos
##cappuccino,100.5
##mocha,- 
##Espresso, seventy five
##AMERICANO,85.00
##lattee, 90
##cappuccino ,100
##mocha, 110php
##espresso,
##"""
##
##orders = raw_orders.strip().split("\n")
##
##for row in orders:
##    parts = row.split(",")
##
##    if len(parts) < 2:
##        print(f"Skipped: {row}")
##        continue
##
##    name = parts[0].strip().lower()
##    price = parts[1].strip().lower()
##
##    if price.strip() == "" or price == "-":
##        continue
##
##    if not price.replace(".", "").isdigit():
##        continue
##
##    price = int(float(price))
##    print(f"{name} - {price:.2f}")
