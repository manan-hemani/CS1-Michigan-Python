n=int(input("Please input the order of square: "))
start=int(input("Please input the top left number: "))
print("The Latin Square is:")
for i in range(n):
    for j in range(n):
        val=(start-1+i+j)%n+1
        print(val,end=" ")
    print()    