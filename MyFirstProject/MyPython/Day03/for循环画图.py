# -*- coding:utf-8 -*-
# 用for循环实现1+2+3+...+100=？
# 把1~100视为一个序列，用for循环直接遍历该序列，并逐个取出进行求和
total = 0 # 存储和
for i in range(1,101):
    # 遍历1~100的序列
    total += i
print('1+2+3+...+100=%d'%(total))
print('-'*100)
# 用for循环绘制多彩螺旋线
import turtle
t = turtle.Pen()
t.speed(100)
colors = ['red','green','blue','yellow'] # 设定颜色列表
for i in range(100):
    # 循环，绘制的圈数
    t.color(colors[i%4])
    # i%4的结果在0~3之间重复，正好是色彩列表的有效索引访问，这条语句是从色彩列表中循环取得不同的颜色
    # t.color('red')
    t.forward(i)
    # 用变化的长度生成螺旋线
    t.left(91)
turtle.done()