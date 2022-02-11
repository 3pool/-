# -*- coding:utf-8 -*-
# 元组：有序且不可变的容器对象（元组中的元素创建之后无法修改）
# 1.元组的创建
# 1.1 直接创建
tup1 = ('Python',1,2,3,'Java',True,[1,23],{'name':'Tom'})
print(tup1)
print(type(tup1))
# 1.2 通过tuple函数进行转换，用来进行转换的对象要是可迭代的
tup2 = tuple([1,2,3])
tup3 = tuple('Hello')
print(tup2)
print(tup3)
# tup4 = tuple(123) # 整数不可迭代，无法转换为元组
print('-'*100)
# 2.访问元组的元素：元组是有序的容器，可以利用索引和切片进行访问，与列表类似
tup4 = tuple(range(1,10))
print(tup4)
print(tup4[0]) # 第一个元素
print(tup4[-1]) # 最后一个元素
print(tup4[1:-1]) # 从2-8
# 元组的遍历
for item in tup4:
    print(item,end=' ')
print()
print('-'*100)
# 3.对元组的其他操作
list1 = list(range(5))
print(list1)
list1[0] = -90
print(list1)
# tup4[0] = -100
# 'hello'[0] = 'H'
# 元组与字符串类似，其元素不支持本地修改（不可变对象）
print(len(tup4))  # 访问长度（元素数量）
print(tup4 + tup4)  # 连接
print(tup4 * 2)   # 复制
print(5 in tup4) # 判断是否在元组中
tup4 = (1,2,3)
# 元组可以重新赋值，实质上是把元组绑定到了其他的内存地址上，相当于创建了一个新的元组
print(tup4)
print('-'*100)
# 4.删除
# 元组可以删除整体，但不能删除元组中的元素
print(tup4)
# del tup4[0]
# del 'hello'[0]
# 元组和字符串类似，不能直接删除元素
del tup4
print('-'*100)
# 集合：无序且不重复的容器
# 应用：对列表去重
list2 = [1,2,3] * 3
print(list2)
list3 = list(set(list2))
# 返回去重之后的列表
print(list3)