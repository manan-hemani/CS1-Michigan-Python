import math
print("Calculate Garden Requirements\n")
print("-----------------------------")
side_length=float(input("Please enter the side length for your garden (in feet) : "))
distance_btw_plant=float(input("Please enter the spacing between plants : "))
depth_flower_beds=float(input("Please enter the depth of garden soil (in feet) : "))
depth_fill=float(input("Please enter the depth for the fill(in feet) : "))

radius = side_length / 4

area_full_circle = math.pi * radius ** 2
area_semicircle = 0.5 * area_full_circle
total_planting_area = area_full_circle + 4 * area_semicircle  

plants_full_circle = int(area_full_circle // (distance_btw_plant ** 2))
plants_semicircle = int(area_semicircle // (distance_btw_plant ** 2))
total_plants = plants_full_circle + 4 * plants_semicircle

soil_full_circle = area_full_circle * depth_flower_beds / 27
soil_semicircle = area_semicircle * depth_flower_beds / 27
total_soil = soil_full_circle + 4 * soil_semicircle

total_garden_area = side_length ** 2
fill_area = total_garden_area - total_planting_area
total_fill = fill_area * depth_fill / 27

print("\n-----------------------------")
print("Requirements\n")
print(f"Plants for each semicircle garden: {plants_semicircle}")
print(f"Plants for the circle garden: {plants_full_circle}")
print(f"Total plants for garden: {total_plants}")
print(f"Soil for each semicircle garden: {soil_semicircle:.1f} cubic yards")
print(f"Soil for the circle garden: {soil_full_circle:.1f} cubic yards")
print(f"Total soil for the garden: {total_soil:.1f} cubic yards")
print(f"Total fill for the garden: {total_fill:.1f} cubic yards")