import turtle

def draw_spiral(length, t):
    if length < 500:
        t.forward(length)

        t.right(90)
        return draw_spiral(length + 5, t)

t = turtle.Turtle()
my_win = turtle.Screen()

t.down()
t.color("magenta")
t.speed(0)

draw_spiral(5, t)
my_win.exitonclick()


