gasoline=input("Please Enter the number of Gallons of gasoline: ")
gasoline_float=float(gasoline)
print("Original number of Gasoline: ",gasoline_float)
one_gallon=3.7854
one_barrel=19.5
co2=20.0
btu=115000
ethanol=75700
price=4.00
print(f"{gasoline_float} gallons is the equivalent of {gasoline_float*one_gallon} litres")
print(f"{gasoline_float} gallons of gasoline requires {gasoline_float/one_barrel} bareels of oil")
print(f"{gasoline_float} gallons of gasoline produces {gasoline_float*co2} pounds of CO2")
print(f"{gasoline_float} gallons of gasoline is energy equivalent to {(gasoline_float*btu)/ethanol} gallons of ethanol")
print(f"{gasoline_float} gallons of gasoline requires {gasoline_float*price} US dollars")
print("Thanks for playing")

#Points to Ponder
# if 0 is inputted then all will become 0
# if string inputted then will generate error can't convert string value to float