mph=input("Please enter a speed in miles/hour: ")
mph_float=float(mph)
meters=mph_float*1609.34
hours_to_seconds=86400
barleycorn=117.647
furlong=220
mph_to_furlong=mph_float*8.0
mach_number=mph_float*(5280/3600)
mph_to_mps=mph_float*0.44704
speed_of_light=299792458
print(f"Original speed in mph is: {mph_float}")
print(f"Converted to barleycorn/day is: {((meters*barleycorn)/1)*24}")
print(f"Converted to furlongs/ fornight is: {(mph_to_furlong/1)*336}")
print(f"Converted to Mach number is: {mach_number/1130}")
print(f"Converted to the percentage of the speed of light is: {mph_to_mps/speed_of_light}")
print("Thanks for Playing")