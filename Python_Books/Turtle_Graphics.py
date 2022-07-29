#  It is possible to draw using a turtle in Python. By typing in commands
#  and using loops, you can create intricate patterns.

import turtle

turtle.shape("circle")
scr = turtle.Screen()

for i in range(0, 5):
    turtle.forward(190)
    turtle.right(90)
    turtle.fillcolor("red")
    scr.bgcolor("yellow")
    turtle.left(0)
    turtle.pensize(5)
turtle.hideturtle()
turtle.showturtle()
turtle.exitonclick()

# Turtle library is a special defined library in Python. It is used when we need. So, I am not going forward yet.