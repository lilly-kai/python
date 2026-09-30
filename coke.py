#. Once the user has inputted at least 50 cents
total = 0
while total < 50:
#insert a coin, one at a time, each time informing the user of the amount due
    coin = int(input("Insert a coin: "))
#Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
    if coin == 25:
        total = total + 25
    elif coin == 10:
        total = total + 10
    elif coin == 5:
        total = total + 5
    if total < 50:
        print("Amount Due:", 50 - total)
#output how many cents in change the user is owed.
print ("Change Owed:", total - 50)
