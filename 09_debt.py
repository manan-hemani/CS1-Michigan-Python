debt=input("What is the debt number: ")
debt_int=int(debt)
denomination=input("What denomination of the currency: ")
denomination_int=int(denomination)
num_bills=debt_int/denomination_int
bill_thickness=0.0043
height=num_bills*(bill_thickness/66360)
eart_to_moon=238857
avg_distance=height/eart_to_moon
print(f"The debt {debt_int} has a height in miles of {denomination_int} 's, {height}")
print(f"That is {avg_distance} times the average distance from the earth to the moon")