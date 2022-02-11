# -*- coding:utf-8 -*-
# 利用return实现
# 1.return 没有内容，相当于return None
def sumx(a,b):
    total = a+b
    print(total)
    return
    # return表示函数结束，之后的函数内容不会被执行，同时，函数也没有返回值
    sx = a*b
    print(sx)

sumx(1,2)
c = sumx(2,3)
print(c)
# c的内容为None，因为函数没有返回值，输出的5是函数的功能
print('-'*100)
# 2.带有内容的return
def sumx1(a,b):
    total = a+b
    print(total)
    return total

d = sumx1(2,4)
# 将函数的返回值赋予调用函数的对象，需要通过表达式的方式进行调用
print('d =',d)
print('-'*100)
# 注意：函数的功能和返回值之间没有半毛钱的关系
def sumx2(a,b):
    total = a+b
    print(total)
    return 100
e = sumx2(4,5)
print('e =',e)