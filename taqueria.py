#menu as dictionary with prices in dollar
menu = {
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
def main():
    total = 0
    while True:
        try:
            # case-insensitive
            item = input("Item: ").title()
            # only items on the menu
            if item in menu:
                total = total + menu[item]
                print(f"${total:.2f}")
        except EOFError:
            # Ctrl-D ends the order, print() for a new line
            print()
            break


main()
