print("Welcome to the Simple Calculator!")
print("You can use +, -, *, / operations")
while True:
    num1 = input("Enter the first number: ")
    op = input("Enter the operator (+, -, *, /): ")
    num2 = input("Enter the second number: ")
    # Check if inputs are digits or valid floats
    if num1.replace(".", "", 1).isdigit() and num2.replace(".", "", 1).isdigit():
        num1 = float(num1)
        num2 = float(num2)
        # Perform calculation
        if op == "+":
            result = num1 + num2
            print("Result:", result)
        elif op == "-":
            result = num1 - num2
            print("Result:", result)
        elif op == "*":
            result = num1 * num2
            print("Result:", result)
        elif op == "/":
            if num2 == 0:
                print("Error: Division by zero.")
            else:
                result = num1 / num2
                print("Result:", result)
        else:
            print("Invalid operator.")
    else:
        print("Invalid input. Please enter numeric values.")
    # Continue confirmation
    again = input("Do you want to perform another calculation? (y/n): ").strip().lower()
    if again != "y":
        print("Thanks for using the Calculator")
        break
