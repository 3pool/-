import math as m
# 1.向上取整
import random

print(m.ceil(1.6))
print(m.ceil(-1.6))

# 2.向下取整
print(m.floor(1.6))
print(m.floor(-1.6))

# 3.转换为整数，与小数无关
print(int(1.6))
print(int(-1.6))

# 4.四舍五入，与符号无关
print(round(1.6))
print(round(-1.6))

# 5.取绝对值
print(abs(-1.6))

# 6.求平方
print(m.sqrt(3))

# 7.其他函数
print(max(1,5,78,3,4,19))
print(max(list(range(1,98))))
print(max('hello world'))
# print('最大值 max:',max(1,2,4,'hello'))

print('-'*100)

print('randint:',random.randint(1,10))
# 返回[1,10]的随机整数
print('random:',random.random())
# 返回[0,1)之间的小数
print('choice:',random.choice([1,2,3,5]))
# 从序列中随机抽取一个值
print('choice:',random.choice(range(9)))
print('choice:',random.choice('hello'))
print('randrange:',random.randrange(9))
# 从range中随机返回一个结果