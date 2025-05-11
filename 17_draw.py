import turtle
import random
print("This program will draw circles of many colors.")
while True:
    num=input("Enter the number of circles to be drawn:")
    if num.isdigit():
        #draw square
        turtle.colormode(255)#for using rgb color values
        for _ in range(int(num)):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            turtle.fillcolor(r,g,b)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(100)
                turtle.right(90)
            turtle.end_fill()    
            turtle.right(30)   
        turtle.hideturtle()
        turtle.done()    
        break
    else:
        print("The number must be an integer and at least 1.\nPlease try again.\n")        
