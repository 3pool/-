# -*- coding:utf-8 -*-
# 字典是无序且可变的容器，存储的形式是键值对{key1:value1,key2:value2}
# 1.字典的创建
# 1.1 先创建一个空字典，再添加内容
dict1 = {}
dict1['name'] = 'Tom'
# 为字典dict1中name键进行赋值，如果该键存在，就是修改键值对的值，如果该键不存在，就是创建一个新的键值对，相当于在字典中添加元素
print(dict1)
# 1.2 直接创建字典
dict2 = {'姓名':'张三','年龄':20,'爱好':['游泳','游戏','美食']}
print(dict2)
# 1.3 通过构造函数创建
dict3 = dict(name='张三',age =22)
# 使用赋值表达式进行创建，=左边的内容成为字典的键，右边的内容成为字典的值
print(dict3)
# dic3x = dict('hello')
# 会报错，因为无法分辨键和值
# 1.4 fromkeys()方法
dict4 = {}.fromkeys(('1st','2nd','3rd'),'python')
print(dict4)
dict5 = {}.fromkeys(('1st','2nd','3rd'),('python','java','c'))
print(dict5)
# fromkeys创建的字典，所有的键对应的值都是相同的，一般用于字典的初始化

# 2.字典的访问
# 2.1 访问单个的元素：字典的键
print(dict4)
# print(dict4[1])
# 字典是不能用索引进行访问
print(dict4['2nd'])
# 返回2nd键对应的值
print(dict4.keys())  # 返回字典中所有的键
print(dict4.values())  # 返回字典中所有的值
# 2.2 遍历字典
list1 = list(range(8))
for item in list1:
    print(item,end=' ')
print()
for item in dict4 :
    print(item,end = ' ')
# 通过循环遍历字典，实质上是遍历的字典的键
print()
for key in dict4.keys():
    print(key)
    print(dict4[key])
# 先遍历字典的键，再通过字典的键来访问字典的值
print('-'*100)
# 3.字典的修改：修改的是字典的值，字典的键无法修改
print(dict4)
dict4['2nd'] = 'java'
# 对字典中已存在的键进行赋值，就是修改字典的键值对（修改的是键值对的值）
print(dict4)
dict4['2rd'] = 'C++'
# 对字典中不存在的键进行赋值，是创建新的键值对
print(dict4)
print('-'*100)
# 4.删除字典的内容
del dict4['2rd']
# 通过del字典中的键来删除键值对
print(dict4)
del dict4
# 直接删除整个字典
# print(dict4)
# 再访问就出错
dict5.clear()
# 清空字典的内容，返回一个空字典
print(dict5)