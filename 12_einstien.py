print("This is a puzzle favored by Einstein. You will be asked to enter three digit number, where the hundred's digit differs from the one's digit by at least two. The procedure will always yield 1089")
num=input("Give me a number: ")
num_rev=num[::-1]
print(f"For the number: {num} the reverse number is: {num_rev}")
if(num>num_rev):
    num_difference=int(num)-int(num_rev)
else:
    num_difference=int(num_rev)-int(num)
print(f"The difference between {num} and {num_rev} is {num_difference}")
num_difference_rev=str(num_difference)
num_difference_rev=num_difference_rev[::-1]
print(f"The reversed differnece is: {num_difference_rev}")
print(f"The sum of: 198 and revDiff is: {198+int(num_difference_rev)}")       