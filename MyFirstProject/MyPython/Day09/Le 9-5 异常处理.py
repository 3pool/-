# -*- coding:utf-8 -*-
# 1，语法错误
# print 'hello'
# 语法错误，pycharm会有红色波浪线提示，容易发现和解决
# 2.非语法错误
a = 3
b = 0
# print(a/b)
# 语法没有错误，但执行过程中会产生错误，导致程序中断，这是我们需要处理的异常
# print('hello')
# 3.基本的异常处理
try:    # 开始进行异常处理
    print(a/b)  # 有可能产生异常的语句
except ZeroDivisionError as error1 :    # 捕捉指定的异常
    print(error1)   # 如果捕捉到异常，做什么事
else:
    print('没有异常')   # 没有捕捉到异常，做什么事
print('hello')
print('-'*100)
try:    # 开始进行异常处理
    print(a/2)  # 有可能产生异常的语句
except ZeroDivisionError as error1 :    # 捕捉指定的异常
    print(error1)   # 如果捕捉到异常，做什么事
else:
    print('没有异常')   # 没有捕捉到异常，做什么事
print('-'*100)

# 4.万能异常处理
try:
    print(a/b)
except Exception as error2:
    print('出现了异常：',error2)
else:
    print('没有异常')
print('-'*100)

# 5.不处理异常，只保证程序能继续运行
try:
    print(a/b)
except:
    pass
    # 什么都不做，只是保证程序结构的完整
else:
    print('没有异常')
print('继续抓取后面的数据')