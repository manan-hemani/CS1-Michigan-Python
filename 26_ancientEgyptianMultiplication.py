flag = "y"
while flag == "y":
    print("Please input the 2 numbers:")
    a = int(input("Enter first number:"))
    b = abs(int(input("Enter second number:")))
    print(f"A = {a} and B = {b}")
    res = 0
    print("B was odd, we add A to make the product: ", a)
    while b > 0:
        if b % 2 == 1:
            res += a
        a *= 2
        b //= 2
        if b > 0:
            print(f"A = {a} and B = {b}")
    print("B was odd, we add A to make the product: ", res)
    if res > 0:
        print("Product is positive")
        print("the product of two numbers is: ", abs(res))
    else:
        print("Product is negative")
        print("the product of two numbers is: ", -abs(res))
    flag = input("Do you want to continue? (y/n):")
    print("=" * 20)
    if flag != "y":
        print("Bad input, quitting")
        exit()
