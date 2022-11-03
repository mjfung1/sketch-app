from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(100)


def move_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "d")
screen.onkey(move_right, "a")
screen.onkey(clear, "c")