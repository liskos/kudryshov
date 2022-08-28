import turtle
turtle.pd()
turtle.speed(99)
n = 20
turtle.lt(90)
for i in range(7):
    turtle.fd(10*n)
    turtle.rt(120)

for x in range(1,10):
    for y in range(1,10):
        turtle.up()
        turtle.goto(x*n,y*n)
        turtle.down()
        turtle.circle(0.3)
input()