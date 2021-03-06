# -*- coding:utf-8 -*-
# 2.带参数的自定义函数
def func2(name):
    print('Hello',name)

# func2()
# 会报错
# 注意：带有参数的自定义函数在调用的时候必须加入参数
func2('张三')
func2(123445)
func2([1,2,3])
# python是动态数据类型的语言，因此，自定义函数的参数不需要指定数据类型，参数的类型要根据函数的功能进行设置

def func2a(num):
    # 计算数值的平方
    print(num ** 2)

# func2a('张三')
# 会报错，因为函数的功能只能使用数字，传入字符串无法操作
func2a(10)