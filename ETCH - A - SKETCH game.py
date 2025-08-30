from turtle import Turtle,Screen

tim =Turtle()
screen = Screen()

def move_forward():
    return tim.forward(10)


def move_backward():
    return tim.back(10)


def move_counterclockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_clockwise():
    new_heading = tim.heading() + 350
    tim.setheading(new_heading)


def clear_screen():
    return tim.reset()


screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_counterclockwise,"a")
screen.onkey(move_clockwise,"d")
screen.onkey(clear_screen,"c")
screen.exitonclick()
