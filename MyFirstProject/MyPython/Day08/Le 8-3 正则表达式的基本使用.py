# -*- coding:utf-8 -*-
# 1.载入库
import re

# 2.构建一个正则表达式匹配对象
pn = re.compile(r'hello')
# 构建一个包含'hello'5个字符的正则表达式匹配对象
print(pn)
print(type(pn))

# 3.尝试进行匹配
result1 = re.match(pn,'hello')
result2 = re.match(pn,'hellla')
result3 = re.match(pn,'yes,hello')
result4 = re.match(pn,'helloworld')
# re.match是从首字符开始进行匹配，如果字符串开始的字符不匹配，返回None，如果匹配上，返回一个Match Object

# 4.输出匹配的结果
print('result1:',result1)
print('result2:',result2)
print('result3:',result3)
print('result4:',result4)

# 5.输出匹配结果中的更多信息
print('-'*100)
print('result1:',result1.group())
# group()返回匹配到的子串
# print('result2:',result2.group())
# 如果没有匹配到，返回None,None没有group()
print('result1.span:',result1.span())
# span返回一个元组，记录了匹配到的子串在字符串中的起始和结束索引
# print('result2.span:',result2.span())

# 6.利用判断处理是否匹配到
print('-'*100)
if result1 == None:
    print('没有匹配到')
else:
    print('匹配到，内容是：',result1.group())

if result2:
    print('匹配到，内容是：', result2.group())
else:
    print('没有匹配到')
# 任何非None的对象，在判断时都等价于True,None等价于False