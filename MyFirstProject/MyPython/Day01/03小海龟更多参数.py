import turtle

t = turtle.Pen()

t.speed(1)
t.pensize(5)
t.pencolor('green')

t.forward(100)
t.begin_fill()
t.fillcolor('red')
t.circle(50)
t.end_fill()
turtle.done()
