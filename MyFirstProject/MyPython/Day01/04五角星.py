import turtle
# 创建对象
t = turtle.Pen()
# 定义参数
t.speed(1)
t.pensize(1)
t.pencolor('red')
# 执行内容
t.forward(100)
t.begin_fill()
t.fillcolor('red')
# 绘制第一个角
for i in range(5):
    t.left(72)
    t.forward(100)
    if i < 4:
        t.right(144)
        t.forward(100)
t.end_fill()
# 停止执行
turtle.done()
