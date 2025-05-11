print("Welcome to the vending machine change maker program")
nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0
print("Change maker initialized.")
print("Stock contains:")
print(nickels, "nickels")
print(dimes, "dimes")
print(quarters, "quarters")
print(ones, "ones")
print(fives, "fives")
while True:
    user_input = input("\nEnter the purchase price (xx.xx) or `q` to quit: ")
    if user_input == 'q':
        break
    try:
        if '.' not in user_input:
            raise ValueError
        dollars_cents = user_input.split('.')
        if len(dollars_cents) != 2:
            raise ValueError
        dollars = int(dollars_cents[0]) if dollars_cents[0] else 0
        cents = int(dollars_cents[1].ljust(2, '0'))
        price_cents = dollars * 100 + cents
        if price_cents < 0 or price_cents % 5 != 0:
            raise ValueError
    except ValueError:
        print("Illegal price: Must be a non-negative multiple of 5 cents.\n")
        continue
    amount_due = price_cents
    print("\nMenu for deposits:")
    print("'n' - deposit a nickel")
    print("'d' - deposit a dime")
    print("'q' - deposit a quarter")
    print("'o' - deposit a one dollar bill")
    print("'f' - deposit a five dollar bill")
    print("'c' - cancel the purchase")
    while amount_due > 0:
        print("Payment due:", amount_due // 100, "dollars and", amount_due % 100, "cents")
        deposit = input("Indicate your deposit: ")
        if deposit == 'n':
            amount_due -= 5
            nickels += 1
        elif deposit == 'd':
            amount_due -= 10
            dimes += 1
        elif deposit == 'q':
            amount_due -= 25
            quarters += 1
        elif deposit == 'o':
            amount_due -= 100
            ones += 1
        elif deposit == 'f':
            amount_due -= 500
            fives += 1
        elif deposit == 'c':
            change = price_cents - amount_due
            amount_due = change
            break
        else:
            print("Illegal selection:", deposit)
    if amount_due <= 0:
        change = -amount_due
        amount_due = 0
        if change == 0:
            print("No change due.")
        else:
            print("\nPlease take the change below.")
            give_quarters = 0
            give_dimes = 0
            give_nickels = 0
            while change >= 25 and quarters > 0:
                change -= 25
                quarters -= 1
                give_quarters += 1
            while change >= 10 and dimes > 0:
                change -= 10
                dimes -= 1
                give_dimes += 1
            while change >= 5 and nickels > 0:
                change -= 5
                nickels -= 1
                give_nickels += 1
            if give_quarters > 0:
                print(give_quarters, "quarters")
            if give_dimes > 0:
                print(give_dimes, "dimes")
            if give_nickels > 0:
                print(give_nickels, "nickels")
            if change > 0:
                print("\nMachine is out of change.")
                print("See store manager for remaining refund.")
                print("Amount due is:", change // 100, "dollars and", change % 100, "cents")
    print("\nStock contains:")
    print(nickels, "nickels")
    print(dimes, "dimes")
    print(quarters, "quarters")
    print(ones, "ones")
    print(fives, "fives")
total_cents = nickels * 5 + dimes * 10 + quarters * 25 + ones * 100 + fives * 500
print("\nTotal amount in stock:", total_cents // 100, "dollars and", total_cents % 100, "cents")