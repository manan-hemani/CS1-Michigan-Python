import turtle
import math
print("This program calculates the acute angle between two lines using slopes.")
print("Line 1: from origin (0,0) to Point 1")
print("Line 2: from Point 1 to Point 2")
print("It will draw both lines and display the angle.\n")
x1 = float(input("Enter x coordinate of Point 1: "))
y1 = float(input("Enter y coordinate of Point 1: "))
x2 = float(input("Enter x coordinate of Point 2: "))
y2 = float(input("Enter y coordinate of Point 2: "))

#turtle graphics
t=turtle.Turtle()
t.penup()
t.goto(0,0)
t.pendown()
t.goto(x1,y1)
t.goto(x2,y2)
turtle.done()

#angle calculation
m1=(y1-0)/(x1-0)
m2=(y2-y1)/(x2-x1)
if (1+(m1*m2) == 0):
    angle_deg=90.0
else:    
    angle_rad=math.atan(abs((m2-m1)/(1+m1*m2)))
    angle_deg=math.degrees(angle_rad)
print(f"\nThe acute angle between the lines is: {angle_deg} degrees")