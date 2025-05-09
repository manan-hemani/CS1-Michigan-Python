print("Guess a six-digit number SLAYER so that following equation is true,where each letter stands for the digit in the position shown:")
print("\nSLAYER + SLAYER + SLAYER = LAYERS\n")
number=input("Enter your Guess for SLAYER: ")
result=int(number)*3
if len(number)!=6:
    print("Your guess is incorrect:\nSLAYER must be a 6-digit number.\nThanks for Playing.")
elif len(str(result))!=6:
    print(f"Your guess is incorrect:\nSLAYER + SLAYER + SLAYER = {result}\nLAYERS = {number}\nThanks for Playing.")
else:
    print(f"Your guess is correct:\nSLAYER + SLAYER + SLAYER = {result}\nLAYERS = {number}\nThanks for Playing.")           
    
#new learning for me: can't use int datatype and len() because it is not an iterable type and len() only works on iterable so type casted it into str and then checked for length in line 7    