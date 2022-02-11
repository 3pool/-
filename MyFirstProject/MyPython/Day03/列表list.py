# 1.列表List
# 有序且可变的容器 有序，可变
# 1.1 生成列表
list1 = [1,2,3,4,'hello',True,[1,2,3]]
print(list1)
print(type(list1))
# 上述方法是直接创建列表

str1 = 'hello'
list2 = list(str1)
print(list2)
# 将字符串转换为列表，会得到一个由字符串中每个字符构成的列表，字符串是一个序列，可以进行迭代和遍历

num1 = 123456
# list3 = list(num1)
# print(list3)
# 并非所有的数据类型都可以转换为列表，整数不是一个序列，无法进行迭代和遍历，因此无法转换成列表

list1.append('abc')
print(list1)

list2.extend(['a','b'])
print(list2)

list3 = ['c','d']
list2.append(list3)
print(list2)

list2.extend(list3)
print(list2)
