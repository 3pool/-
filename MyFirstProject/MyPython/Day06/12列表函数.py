# -*- coding:utf-8 -*-
# 列表元素的添加删除
# 添加
list1 = list(range(8))
print(list1)
list1.append(100)  # 添加一个元素
list1.extend([-1,-2]) # 添加多个元素
print(list1)
list1.insert(0,-1) # 在指定的索引位置上插入新的值
print(list1)
# list1.insert(0,-3,-2)
# insert只能插入一个元素
list1.insert(0,[-3,-2])
print(list1)
# 删除
del list1[0]
print(list1)
list1.pop()
# 从列表中取出一个元素，会把取出的元素赋予调用pop函数的对象
print(list1)
item1 = list1.pop()
print(item1)
print(list1)
list1.remove(100)
# 按照值进行删除
print(list1)
item2 = list1.remove(-1)
# remove只删除，不返回值
print(item2)
print(list1)

print('-'*100)
# 排序
import random
list2 = []
list3 = []
for i in range(10):
    list2.append(random.randint(1,10))
    list3.append(random.randint(1,10))
print('list2:',list2)
print('list3:',list3)
list2.sort()
# 默认是升序
print('排好序的list2:',list2)
list3.sort(reverse=True)
# 降序处理
print('排好序的list3:',list3)
print(list3[-1::-1])
list4 = list('hello')
list4.sort()
print(list4)
# 字符串也可以排序
# list5 = [1,2,3,'he','l','o']
# list5.sort()
# 排序不能针对混合的内容（如字符串和数字）