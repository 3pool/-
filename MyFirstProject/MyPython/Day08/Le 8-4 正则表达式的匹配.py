# -*- coding:utf-8 -*-
import re
# 1.关于大小写
str1 = 'Hello world'
pn1 = re.compile(r'hello')
result1 = re.match(pn1,str1)
print('result1:',result1)
pn2 = re.compile(r'hello',re.I)
# re.I是匹配是忽略大小写
result2 = re.match(pn2,str1)
print('result2:',result2)

print('-'*50+'位置问题'+'-'*50)
# 2.位置问题
str3 = 'yes hello'
pn3 = re.compile(r'hello')
result3 = re.match(pn3,str3)
print('result3:',result3)
result4 = re.search(pn3,str3)
print('result4:',result4)
# search是在整个字符串中进行匹配的操作，匹配到的话，返回Match Object，匹配不到返回None
print(result4.group())
print(result4.span())

print('-'*50+'数量问题'+'-'*50)
# 3.数量问题
str5 = 'yes hello,no hello'
pn5 = re.compile(r'hello')
result5 = re.search(pn5,str5)
print('result5:',result5)
# search只做一次匹配，返回第一次匹配到的结果
result6 = re.findall(pn5,str5)
print('result6:',result6)
# findall返回的是字符串中所有匹配到的子串，结果是一个子串构成的列表
for item in result6:
    print(item)
pn7 = 'hella'
result7 = re.findall(pn7,str5)
print('result7:',result7)
# findall匹配不到任何内容的时候，返回的结果是空列表

print('-'*50+'位置和数量问题'+'-'*50)
# 4.既有数量，又有位置
result8 = re.finditer(pn5,str5)
print('result8:',result8)
# finditer返回的是由 Match object构成的迭代器，可以用循环遍历，如果找不到，返回空的迭代器
for item in result8:
    print(item)
    print(item.group())
    print(item.span())

print('-'*50+'模糊匹配-代词'+'-'*50)
# 5.模糊查找-代词
str9 = 'http://www.4abc5abc.com'
# 要找出4和5
pn9 = re.compile(r'\d')
# \d代表数字
result9 = re.findall(pn9,str9)
print('result9:',result9)
# 代词后面没有量词，只代表1个字符，\d代表1个数字
# 正则表达式匹配到的都是字符串，哪怕是数字
# 如果要查找4abc,5abc
# 代词也可以和固定的字符搭配使用
pn10 = re.compile('\dabc')
# 代表要匹配的是以一个数字开头，abc结尾的字符串
result10 = re.findall(pn10,str9)
print('result10:',result10)

print('-'*50+'模糊匹配-代词-量词'+'-'*50)
# 6、要查找的字符串长度不固定-量词配合代词
str11 = 'one1two22three333four4444five55555'
# 提取所有由数字构成的子串[1,22,333,4444,55555]
pn11 = re.compile(r'\d')
result11 = re.findall(pn11,str11)
print('result11:',result11)
# \d 只代表1个数字
pn12 = re.compile(r'\d+')
# *+?在使用的时候不需要加上{}
result12 = re.findall(pn12,str11)
print('result12:',result12)

print('-'*50+'拆分split'+'-'*50)
# 7.用正则表达式进行拆分
str12 = 'Tom is a good boy, Rose is a beautiful girl.'
# 使用空格作为分隔符进行拆分
print(str12.split(' '))
# 字符串的split方法，返回结果是子串构成的列表
pn13 = re.compile(r' ')
print(re.split(pn13,str12))
# re.split,如果用单个的空格进行拆分，字符串的split和re.split效果一一样，返回的都是由拆分结果构成的列表
str12x = 'Tom is  a good \t boy, Rose is \n a beautiful girl.'
print('str.split',str12x.split(' '))
#str.split只能针对规范的情况进行处理
print('re.split:',re.split(r'\s',str12x))
print('re.split:',re.split(r'\s+',str12x))
# 借助代词和量词，re.split可以实现比str.split更加灵活方便的拆分处理

print('-'*50+'替换sub/subn'+'-'*50)
# 8.用正则表达式进行替换
sDate = '2021-07-15'
# 替换成2021/07/15
print(re.sub(r'\-',r'/',sDate))
print(re.subn(r'\-',r'/',sDate))
# sub直接返回替换后的结果，subn返回一个元组，包括替换的结果和替换的次数