import math
print("At the prompts, please enter the following:\n")
print("\tCustomer's classification code (a character)")
print("\tNumber of days the vehicle was rented (an integer)")
print("\tOdometer reading at the start of the rental period (an integer)")
print("\tOdometer reading at the end of the rental period (an integer)\n")
while True:
    customer_code=input("Customer code: ")
    customer_code.lower()
    max_reading=999999
    if customer_code=='d':
        no_of_days=int(input("Number of days: "))
        odometer_start=int(input("Odometer reading at the start: "))
        odometer_end=int(input("Odometer reading at the end: "))
        if(odometer_end>= odometer_start):
            tenth=odometer_end-odometer_start
        else:
            tenth= (max_reading-odometer_start)+odometer_end+1
        miles=tenth/10
        #amount calculation as provided
        base_charge=60.00*no_of_days
        if miles<=100:
            amount=base_charge
        else:
            amount=base_charge+(0.25*miles) 
        #displaying all details  
        print("Customer summary:")
        print(f"\tclassification code: {customer_code}")
        print(f"\trental period (days): {no_of_days}")
        print(f"\todometer reading at start: {odometer_start}")
        print(f"\todometer reading at end: {odometer_end}")
        print(f"\tnumber of miles driven {miles}")
        print(f"\tamount due: {amount}")     
    elif customer_code=='b':
        no_of_days=int(input("Number of days: "))
        odometer_start=int(input("Odometer reading at the start: "))
        odometer_end=int(input("Odometer reading at the end: "))
        if(odometer_end>= odometer_start):
            tenth=odometer_end-odometer_start
        else:
            tenth= (max_reading-odometer_start)+odometer_end+1
        miles=tenth/10
        #amount calculation as provided
        base_charge=40.00*no_of_days
        amount=base_charge+(miles*0.25)
        #displaying all details  
        print("Customer summary:")
        print(f"\tclassification code: {customer_code}")
        print(f"\trental period (days): {no_of_days}")
        print(f"\todometer reading at start: {odometer_start}")
        print(f"\todometer reading at end: {odometer_end}")
        print(f"\tnumber of miles driven {miles}")
        print(f"\tamount due: {amount}")     
            
    elif customer_code=='w':
        no_of_days=int(input("Number of days: "))
        odometer_start=int(input("Odometer reading at the start: "))
        odometer_end=int(input("Odometer reading at the end: "))
        if(odometer_end>= odometer_start):
            tenth=odometer_end-odometer_start
        else:
            tenth= (max_reading-odometer_start)+odometer_end+1
        miles=tenth/10
        #amount calculation as provided
        weeks=math.ceil(no_of_days/7)
        base_charge=190.00*weeks
        if miles<=900:
            extra=0
        elif miles<=1500:
            extra=100.00*weeks    
        else:
            extra_miles=miles-(1500*weeks)
            extra=(200.00*weeks)+(0.25*extra_miles)
        amount=base_charge+extra     
        #displaying all details  
        print("Customer summary:")
        print(f"\tclassification code: {customer_code}")
        print(f"\trental period (days): {no_of_days}")
        print(f"\todometer reading at start: {odometer_start}")
        print(f"\todometer reading at end: {odometer_end}")
        print(f"\tnumber of miles driven {miles}")
        print(f"\tamount due: {amount}")     
    else: 
        break        
        
