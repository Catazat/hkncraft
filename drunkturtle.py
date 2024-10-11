import turtle
import random
turtle.title("Drunk Turtle")
turtle.lt(90)
while True:
    for loop in range(random.randint(1,50)):
        turtle.speed(random.randint(1,15))
        turtle.pencolor(random.choice(["Black", "Red", "Blue", "Green"]))
        turtle.right(random.randint(-360,360))
        turtle.forward(random.randint(1,100))
    turtle.stamp()
    turtle.home()
