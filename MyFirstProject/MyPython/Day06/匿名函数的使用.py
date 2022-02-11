# -*- coding:utf-8 -*-
# lambda 匿名函数
# 1.无参数的匿名函数
a = lambda :'Hello world'
# 构建了一个匿名函数，该函数的返回值是Hello world
# 将该匿名函数赋予对象a
print(a)
# 直接访问a是访问一个匿名函数对象
print(a())
# 用a()的方式进行访问
print(lambda :'Hello world' ())
# 针对无参数的匿名函数，通常需要通过赋予一个对象来访问
print('-'*100)
# 2.带参数的匿名函数
c = lambda x : x**2
print(c(5))
# 构建一个求平方的匿名函数，赋予c对象，再通过对c对象的调用返回函数的结果
print('匿名函数',lambda x:x**2(5))