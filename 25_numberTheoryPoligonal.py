import math
n = int(input("Enter a square number: "))
#condition for checking square number
if int(math.sqrt(n)) != math.sqrt(n):
    print("Error: Not a perfect square.")
else:
    a = 1
    while a * (a + 1) // 2 < n:
        t1 = a * (a + 1) // 2  #1st triangular no.
        b = 1
        while b * (b + 1) // 2 < n:
            t2 = b * (b + 1) // 2  #2nd triangular no.
            if t1 + t2 == n:
                print("Triangular numbers are:", t1, "and", t2)
                print("They sum to:", n)
                exit()  
            b += 1
        a += 1
