while True:
    customer_code=input("Enter customer code: ")
    customer_code.lower()
    max_reading=999999999
    if customer_code=='c' :
        beginning=int(input("Enter beginning meter reading: "))
        ending=int(input("Enter ending meter reading: "))
        print("Customer code: ",customer_code)
        print("Beginning meter reading: ",beginning)
        print("Ending meter reading: ",ending)
        if(ending>= beginning):
            tenth=ending-beginning
        else:
            tenth= (max_reading-beginning)+ending+1
        gallons_used=tenth/10
        #amount calculation as per given in pdf
        if gallons_used<=4000000:
            amount=1000.00
        else:
            extra_rate=gallons_used-4000000
            amount=1000.00+0.00025*extra_rate           
        print("Gallons of water used: ",gallons_used)
        print("Amount billed: $",amount)
    elif customer_code=='r':
        beginning=int(input("Enter beginning meter reading: "))
        ending=int(input("Enter ending meter reading: "))
        print("Customer code: ",customer_code)
        print("Beginning meter reading: ",beginning)
        print("Ending meter reading: ",ending)
        if(ending>= beginning):
            tenths=ending-beginning
        else:
            tenth= (max_reading-beginning)+ending+1
        gallons_used=tenth/10
        #amount calculation as per given in pdf
        amount=5.00+0.0005*gallons_used       
        print("Gallons of water used: ",gallons_used)
        print("Amount billed: $",amount)
    elif customer_code=='i':
        beginning=int(input("Enter beginning meter reading: "))
        ending=int(input("Enter ending meter reading: "))
        print("Customer code: ",customer_code)
        print("Beginning meter reading: ",beginning)
        print("Ending meter reading: ",ending)
        if(ending>= beginning):
            tenths=ending-beginning
        else:
            tenth= (max_reading-beginning)+ending+1
        gallons_used=tenth/10
        #amount calculation as per given in pdf
        if gallons_used<=4000000:
            amount=1000.00
        elif gallons_used<=10000000:
            amount=2000.00    
        else:
            extra_rate=gallons_used-10000000
            amount=2000.00+0.00025*extra_rate           
        print("Gallons of water used: ",gallons_used)
        print("Amount billed: $",amount)
    else:
        break
        
        