# -*- coding:utf-8 -*-
a = input('请输入一个数字：')
# 暂停程序的执行，直到用户敲击回车键
print(a)
print(type(a))
b = input('请输入另一个数字')
print('a+b=',a+b)
# 用input返回的结果是字符串，如果要进行算数运算，必须做显式的数据转换
print('a+b=',int(a)+int(b))
# 为了避免数值类型的问题，建议在接受用户输入的同时就进行数据的转换
c = float(input('请输入第三个数字：'))
d = float(input('请输入第四个数字：'))
print('%.2f + %.2f = %.2f'%(c,d,c+d))