# -*- coding:utf-8 -*-
# 变量是用来代替内存地址的
# 变量一定要先定义，再使用（用赋值操作进行定义）
num = 5
print(num)
# print(a)
# 上述代码会出错，因为a在print语句之前没有被定义（赋值）
# 在python中，相同的常量对象（如2）是放在同一个内存地址中的，因此可以用判断变量的内存地址是否一致来判断变量存储的内容是否一致
a = 2
b = 2
print('id(a):',id(a))
print('id(b):',id(b))
print(id(a) == id(b))
a = 'Hello World'
print(a)
print('id(a):',id(a))
print(id(a) == id(b))
print('-'*100)
_1st = 100 # 数字不能作为变量名称的开头，下划线可以
# False = 3 # 不能把关键字作为变量使用
# 驼峰命名法
No_1st = 1000
姓名 = '张三' # 中文是可以做为变量使用的
print(姓名)
print('-'*100)
help('keywords')
# 查看python的关键字