from turtle import *

t1 = Turtle()
t1.color("orange")
t1.width(50)


t2 = Turtle()
t2.color("#960018")
t2.width(50)


t3 = Turtle()
t3.color("green")
t3.width(50)

t1.penup()
t1.goto(0, 200)
t1.pendown()

t2.penup()
t2.goto(0, 250)
t2.pendown()

t3.penup()
t3.goto(0, 300)
t3.pendown()

t1.forward(400)
t2.forward(400)
t3.forward(400)

exitonclick()

