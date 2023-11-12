menu_items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_amount = 0

while True:
    try:
        item_input = input("Item: ").title()

        if item_input in menu_items:
            total_amount += menu_items[item_input]
            print("Total: $",end="")
            print("{:.2f}".format(total_amount))
    except EOFError:
        print()
        break
