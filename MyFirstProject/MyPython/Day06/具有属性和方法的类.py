# -*- coding:utf-8 -*-
# 2.具有属性和方法的类
class Asset():
    name = '股票'
    # 类的属性

    def funcA(self):
        # self是在类中定义函数时自带的第一个位置的参数，指代的是对象自身，一般不需要修改，调用方法的时候也不需要传入
        print('上涨')
        # 类的方法

asset2 = Asset()
# 实例化类构建对象
print(asset2)
print('asset2:',asset2.name)
# 利用.语法访问对象的属性
asset2.funcA()
# 利用.语法调用对象的方法，注意要写上()
# import random
# a = random.randint(1,10)
print('-'*100)
asset3 = Asset()
print('asset3:',asset3.name)
asset3.funcA()
# asset3和asset2具有同样的属性和方法，asset3的特征和asset2一样（name属性的值都是股票）