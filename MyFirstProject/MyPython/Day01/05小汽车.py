import turtle
# 创建对象
t = turtle.Pen()
# 定义参数
t.speed(1)
t.pensize(1)
t.pencolor('red')
# 绘制车架
t.forward(200)
t.begin_fill()
t.fillcolor('red')
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()
# 绘制第一个轮胎
t.penup()
t.goto(15,-25)
t.pendown()
t.pencolor('black')
t.begin_fill()
t.fillcolor('black')
t.circle(35)
t.end_fill()

# 绘制第二个轮胎
t.penup()
t.goto(115,-25)
t.pendown()
t.pencolor('black')
t.begin_fill()
t.fillcolor('black')
t.circle(35)
t.end_fill()

# 停止执行
turtle.done()
