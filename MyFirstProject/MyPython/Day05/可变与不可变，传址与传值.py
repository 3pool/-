# -*- coding:utf-8 -*-
# 可变对象：列表和字典，可以做局部的修改
# 不可变对象：整数、字符串、元组，不能做局部的修改
list1 = [1, 2, 3, 4]
print(list1)
list1[0] = 0
print(list1)
dic1 = {'a': 1, 'b': 2}
print(dic1)
dic1['a'] = -1
print(dic1)
print('-' * 100)
str1 = 'Hello'
# str1[0] = 'h'
num1 = 123
# num1[0] = 2
tup1 = (1, 2, 3)


# tup1[1] = 0
def funcx():
    list1[0] = 999
    dic1['b'] = 100


# 在函数内修改可变对象的局部
funcx()
print(list1)
print(dic1)

print('-' * 100)


# 把可变对象（列表，字典）作为参数传递给函数：传递给函数的是可变对象的内存地址（可变对象的索引或键的内存地址）
def funca(lista):
    lista[0] = -999
    print('函数中的lista:', lista)
    print('函数中lista的内存地址：', id(lista))


lista = [4, 3, 2, 1]
print('调用函数前的lista:', lista)
print('调用函数前lista的内存地址：', id(lista))

funca(lista)
print('调用函数后的lista:', lista)
print('调用函数后lista的内存地址：', id(lista))
# 使用可变对象作为参数，传递是可变对象自身的内存地址，这个操作被称为传址

print('-' * 100)


# 把不可变对象做为参数传递给函数，传递是内存中存放的值
def funcb(a):
    a = 0
    # 在函数内构建了一个和函数外的a同名的对象，和函数外的a不是同一个对象
    print('函数中的a:', a)
    print('函数中a的内存地址：', id(a))


a = 1
print('调用函数前的a:', a)
print('调用函数前a的内存地址：', id(a))
funcb(a)
print('调用函数后的a:', a)
print('调用函数后a的内存地址：', id(a))
# 传递的是不可变对象，其内存地址已经存放了原始的值，无法再修改为新的值，所以，将不可变对象作为参数传递的时候，传递的是不可变对象的值而非内存地址，该操作被称为传值