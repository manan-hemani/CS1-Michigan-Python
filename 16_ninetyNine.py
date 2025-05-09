print("We are going to play a game. I want you to pick a number then do a series of calculations. I bet I know what the result of those calculations will be!")
num_ans=int(input("*You* This will be the answer. Select a number 10-49: "))
player_num=int(input("*Player* Pick any number 50-99: "))
#trick for calculation
factor=str((abs(num_ans-99))+player_num)
remove_hundred_digit=int(factor[1:])+1 #converting to str then slicing it and type caste int to calculate further
res=player_num-int(remove_hundred_digit)
print(f"I said the answer was {res} and the calculation result is {num_ans}")