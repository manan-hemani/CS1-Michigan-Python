print("This is a puzzle favored by Gen. MacArthur. You will be asked to secretly type in your birth month (as an integer) and your age The computer will make a special calculation, yielding a new integer The computer will then calculate, using only that special number, your birth month and age")
month=int(input("Give me your birth month: "))
age=int(input("Give me your age: "))
special_num=125
print("The special number is: ",special_num)
#calculation
calculation=((((((month*2)+5)*50)+age)-365)+115)
calculation=str(calculation)
print(f"The computer calculates then that you were born in the {calculation[0]} month and are {calculation[1:3]} years old")