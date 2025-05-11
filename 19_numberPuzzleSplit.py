while True:
    num=input("Input a large whole number: ")
    if num.isdigit():
        split_input=input("Input the split (whole number): ")
        if split_input.isdigit():
            split_input=int(split_input)
            splitted=[]
            for i in range(0, len(num), split_input):
                current=int(num[i:i+split_input])
                splitted.append(current)
                if i+split_input< len(num):
                    next=int(num[i+split_input:i+2*split_input])
                    if current>=next:
                        flag=False
                flag=True
            print(splitted)    
            if flag:
                print("Sequence is increasing")
            else:
                print("Sequence is not increasing")                            
            break
        else:
            print("Input must be a whole number. Try again.")    
    else:
        print("Input must be a whole number. Try again.")        