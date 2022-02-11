# -*- coding:utf-8 -*-
# 3.类的构造函数__init__()
class Asset():
    '''
    定义一个具有初始属性的类
    '''
    def __init__(self,name,price):
        self.name = name
        self.price = price
        # 将构造函数传入的参数赋予对象的属性

# asset4 = Asset()
# 当使用__init__函数构建带有属性的对象时，由于__init__函数中构建了对应的参数，因此，我们在实例化类创建对象时，就要把参数的值传递进去，否则就会出错
asset4 = Asset('股票',20.98)
print('asset4:',asset4.name,asset4.price)

asset5 = Asset('比特币',65000)
print('asset5:',asset5.name,asset5.price)