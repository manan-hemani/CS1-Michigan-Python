import math

print("\nMenu Options:")
print("A. Display the value of the factorial of N")
print("B. Display the value of the sine of X (in radians)")
print("C. Display the value of the cosine of X (in radians)")
print("M. Display the menu options")
print("Q. Quit the program")
while True:
    choice = input("\nEnter your option: ").lower()
    if choice == 'a':
        n = int(input("Enter a positive integer N: "))
        if n >= 0:
            result = 1
            i = 2
            while i <= n:
                result *= i
                i += 1
            print("Factorial of", n, "is:", result)
        else:
            print("Please enter a non-negative integer.")
    elif choice == 'b':
        x = float(input("Enter value of X in radians: "))
        print("Sine of", x, "is:", math.sin(x))
    elif choice == 'c':
        x = float(input("Enter value of X in radians: "))
        print("Cosine of", x, "is:", math.cos(x))
    elif choice == 'm':
        print("\nMenu Options:")
        print("A. Display the value of the factorial of N")
        print("B. Display the value of the sine of X (in radians)")
        print("C. Display the value of the cosine of X (in radians)")
        print("M. Display the menu options")
        print("Q. Quit the program")
    elif choice == 'q':
        print("Exiting program.")
        break
    else:
        print("Invalid option.")
        print("\nMenu Options:")
        print("A. Display the value of the factorial of N")
        print("B. Display the value of the sine of X (in radians)")
        print("C. Display the value of the cosine of X (in radians)")
        print("M. Display the menu options")
        print("Q. Quit the program")
