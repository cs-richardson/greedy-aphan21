"""
This program is to convert the change owed to number of quarters, dimes, nickels and pennies.
Coded by Ann Phan, help from stackoverflow.com to code for the check if an input is a positive float.
"""
while True:
    try:
        change_owed = float(input("How much change is owed?"))
        if change_owed < 0: 
            print("Sorry, positive floats only.")
            continue
        break
    except ValueError:
        print("Sorry, numbers only.")

total_coins = int (change_owed * 100)

quarters = int(total_coins / 25)
if quarters == 1:
    print("You need 1 quarter.")
elif quarters > 1 or not_quarters == 0:
    print("You need", quarters, "quarters.")
not_quarters = int(total_coins % 25)

dimes = int(not_quarters / 10)
if dimes == 1:
    print("You need 1 dime.")
elif dimes > 1:
    print("You need", dimes, "dimes.")
not_dimes = int(not_quarters % 10)
    
nickels = int(not_dimes / 5)
if nickels == 1:
    print("You need 1 nickel.")
elif nickels > 1:
    print("You need", nickels, "nickels.")
not_nickels = int(not_dimes % 5)

pennies = int(not_nickels)
if pennies == 1:
    print("You need 1 penny.")
elif pennies > 1:
    print("You need", pennies, "pennies.")




        








