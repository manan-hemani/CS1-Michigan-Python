while True:
    num=input("Please give me an integer (negative integer to quit): ")
    #condition for checking negative value
    if int(num)>0:
        print("\nMultiplicative loop:")
        mul=1
        count_mul=0
        res_mul=num
        res_add=num
        #loop for multiplicative       
        while True:
            if int(res_mul)//10!=0: #check for single digit
                for i in str(res_mul):
                    mul*=int(i)
                count_mul+=1
                print("product: ",mul)
                res_mul=mul
                mul=1#reset mul 
            else:
                break
        add=0
        count_add=0
        #loop for additive
        print("\nAdditive loop:")        
        while True:
            if int(res_add)//10!=0: #check for single digit
                for i in str(res_add):
                    add+=int(i)
                count_add+=1
                print("sum: ",add)
                res_add=add
                add=0#reset add 
            else:
                break        
        #final value printing
        print(f"\nFor the integer: {num}")    
        print(f"\tAdditive Persistence: {count_add} , Additive Root: {res_add}")
        print(f"\tMultiplicative Persistence: {count_mul} , Multiplicative Root: {res_mul}")
    else:
        print("Thanks for playing")
        break