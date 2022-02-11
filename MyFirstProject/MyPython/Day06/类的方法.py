class sale_smoke():
    def __init__(self,brand,age):
        self.brand = brand
        self.age = age
    def smoke(self):
        if self.age < 18:
            print('不卖给未成年人')
        else:
            if self.brand == '阳光利群':
                price = 23
                print(price)
            elif self.brand == '和天下':
                price = 100
                print(price)

sale_smoke1 = sale_smoke('和天下',17)
sale_smoke1.smoke()






# -*- coding:utf-8 -*-
# 4.类的方法
# class Asset():
#
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#
#     def print_price(self):
#         print(self.name,'的价格是',self.price)
#     # 利用类的方法来访问类的属性
#
# asset6 = Asset('黄金',400)
# print(asset6.name)
# print(asset6.price)
# asset6.print_price()

