from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim. color("red")
for _ in range(4):
    tim.forward(100)
    tim.left(90)
screen = Screen()
screen = screen.exitonclick()
