# -*- coding:utf-8 -*-
# 默认参数：在定义函数时做了赋值的参数，调用的时候可以忽略，如果忽略，直接传递定义时的赋值
# print('hello',1,2)
def func04(name,age=18,gender ='f'):
    print('Hello',name)
    print('Age:',age)
    print('Gender:',gender)

func04('张三',20,'m') # 简单调用，为每个参数传递值
func04(gender='m',name = '李四',age=19) # 关键字调用，为每个参数传递值
func04('王二',18) # 简单调用，忽略了gender，此时会用默认的f传递进去
func04(name='Tom') # 关键字调用，只给name传递值，其他两个参数会以默认值传递进去