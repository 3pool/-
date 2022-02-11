# -*- coding:utf-8 -*-
# 1.最基本的推导式：list = [item for item in iterable]
# 构建一个[1,2,3,4,5]的列表
list1 = [1,2,3,4,5]
print('手动创建：',list1)
list2 = list(range(1,6))
print('range转换：',list2)
# 用循环进行构建
list3 = [] # 先构建一个空列表
for item in range(1,6):
    # 遍历1-5的序列
    list3.append(item)
print('用循环添加：',list3)
# 把循环改成推导式：
list4 = [item for item in range(1,6)]
print('推导式：',list4)
print('-'*100)
# 2.复杂一点的推导式： list = [item 相关的表达式 for item in iterable]
# [1,4,9,16,25]
# 先用循环实现
list5 = []
for item in range(1,6):
    list5.append(item ** 2)
print(list5)
# 把循环改成推导式
list6 = [item ** 2 for item in range(1,6)]
print(list6)
print('-'*100)
# 3.更复杂的推导式：list = [item 相关的表达式 for item in iterable if 条件]
# [1,9,25,49,81]
# 循环实现：
list7 = []
for item in range(1,10):
    if item % 2 == 1:
        # 如果是奇数
        list7.append(item ** 2)
print(list7)
# 改成推导式
list8 = [item ** 2 for item in range(1,10) if item % 2 == 1]
print(list8)