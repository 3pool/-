# -*- coding:utf-8 -*-
# 循环控制往往和条件判断结合
str1 = 'hello world'
for letter in str1:
    print(letter)
print('-'*100)
# 遇到空格结束循环
for letter in str1:
    if letter == ' ':
        break # 终止整个循环
    print(letter)
print('-'*100)
# 遇到空格跳过空格
for letter in str1:
    if letter == ' ':
        continue # 跳过本次循环，继续后面的循环
    print(letter)
print('-'*100)
# 保持程序结构完整
for letter in str1:
    pass
    # 作为占位符使用，通常用来保持程序结构的完整性，不执行任何功能
print('hello')
# 循环之后要做的事情