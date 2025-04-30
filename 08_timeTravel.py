import math
velocity=input("Please enter velocity (percentage of speed of light): ")
velocity_float=float(velocity)
c=299792458 
ship_weight=70000 
v=(velocity_float/100)*c 
gamma=1/math.sqrt(1-(v**2/c**2))
alpha_centauri= 4.3  
barnards_star= 6.0  
betelgeuse= 309 
andromeda_galaxy= 2000000
ship_weight_changed=ship_weight/math.sqrt(1-((velocity_float**2)/(100**2))) 
print(f"Ship is traveling at {velocity} % of the speed of light.")
print("At this speed:")
print(f"\tWeight of the shuttle is: {ship_weight_changed}")
print(f"\tPerceived time to travel to Alpha Centauri {alpha_centauri/gamma}")
print(f"\tPerceived time to travel to Barnard\’s Star {barnards_star/gamma}")
print(f"\tPerceived time to travel to Betelgeuse {betelgeuse/gamma}")
print(f"\tPerceived time to travel to Andromeda Galaxy {andromeda_galaxy/gamma}")