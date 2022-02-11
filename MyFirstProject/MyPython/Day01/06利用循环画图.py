import turtle
# 创建对象
t=turtle.Pen()
# 定义参数
t.speed(0)
t.pensize(1)
t.pencolor('red')
# 绘制开始
t.seth(10)    #初始角度
length = 0
while (length !=350):
    t.forward(length)
    t.right(89.5)
    length += 2
#停止绘制
turtle.done()