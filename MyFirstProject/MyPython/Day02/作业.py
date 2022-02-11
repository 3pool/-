# print('我爱"我的祖国')
# print('''我爱"我的祖国''')
# print("我爱\"我的祖国")

import turtle
t = turtle.Pen()
t.speed(1)

t.pencolor('red')
t.begin_fill()
t.fillcolor('red')
t.circle(50)
t.end_fill()

t.penup()
t.goto(50,50)
t.pendown()

t.pencolor('blue')
t.begin_fill()
t.fillcolor('blue')
t.circle(50)
t.end_fill()

t.penup()
t.goto(100,100)
t.pendown()

t.pencolor('yellow')
t.begin_fill()
t.fillcolor('yellow')
t.circle(50)
t.end_fill()

t.penup()
t.goto(150,150)
t.pendown()

t.pencolor('purple')
t.begin_fill()
t.fillcolor('purple')
t.circle(50)
t.end_fill()

t.penup()
t.goto(185,235)
t.pendown()

t.pensize(20)
t.pencolor('orange')
t.begin_fill()
t.fillcolor('orange')
t.left(225)
t.forward(400)
t.end_fill()

turtle.done()


