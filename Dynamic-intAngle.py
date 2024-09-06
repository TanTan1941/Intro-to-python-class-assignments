import turtle
myTurtle = turtle.Turtle()


# using '/' to divide 360 by whatever intSides equals

intLen = 100
intSides = 12
intAngle = 360/intSides

turtle.begin_fill()
for x in range(intSides):
    turtle.forward(intLen)
    turtle.right(intAngle)
turtle.end_fill()

screen = turtle.Screen()
screen.exitonclick()
