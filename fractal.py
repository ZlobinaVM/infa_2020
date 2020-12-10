
import turtle
 
size = 600
n = 5
turtle.shape('turtle')
turtle.speed(0)
turtle.tracer(False, 1)


def koch_curve(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
        turtle.right(120)
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
 
 
def draw_koch_snowflake(size, n):
    for i in range(3):
        koch_curve(size, n)
        turtle.right(120)
 
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
 
draw_koch_snowflake(size, n)
turtle.exitonclick()
