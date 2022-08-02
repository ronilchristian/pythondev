import turtle
import turtle as t

tim = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.setheading(tim.heading() + 10)


def turn_right():
    tim.setheading(tim.heading() - 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
