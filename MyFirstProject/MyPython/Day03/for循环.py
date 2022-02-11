# -*- coding:utf-8 -*-
# 1.用for循环遍历序列
list1 = list(range(9))  # 0-8的列表
for item in list1:
    print(item)
print('-'*100)
# 用for循环遍历字符串
str1 = 'Hello,world'
for letter in str1:
    print(letter)
# 上述方式是用for循环直接遍历序列，访问序列中的每个对象
print('-'*100)
# 2.借助索引间接遍历序列
# range的用法：返回一个整数序列，range(begin,end,step),返回一个左闭右开的整数序列，默认从0开始
a = range(0,9)
print(a)
# range对象无法直接访问其中的元素，可以利用循环遍历
for i in range(0,9):
    print(i)
# 借助range返回有效的索引范围
print('-'*100)
print(list1)
print('list1的有效索引范围：',0,len(list1)-1)
print(range(0,len(list1)))
print(range(len(list1))) # 因为range也是返回一个左闭右开的区间，所以能访问的最后一个元素正好是len(list1)-1，正好是有效的索引范围边界
print('-'*100)
for i in range(len(list1)):
    # 遍历list1的索引
    print(list1[i])
# 用索引遍历一般用于多个列表同时遍历的时候
list2 = list(range(1,10)) # 返回一个1-9的列表
print('list1:',list1)
print('list2:',list2)
for myIndex  in range(len(list1)):
    print(list1[myIndex] + list2[myIndex])
print('-'*100)
# 小尾巴
str2 = 'hello'
for letter in str2:
    print(1)
# for循环是遍历序列中的每个对象，但循环中药执行的操作可以和序列没有直接关系，只是把序列作为一个计数的标志