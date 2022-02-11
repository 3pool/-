# -*- coding:utf-8 -*-
# 1.载入库
import urllib.request
import re
import requests
from bs4 import BeautifulSoup as bs
# 从bs4库中载入BeautifulSoup对象，并起一个别名bs

# 2.关于bs的基本使用
url = 'http://www.baidu.com'
response = requests.get(url)
response.encoding = 'utf-8'
soup = bs(response.content,'html.parser')
# 把抓取到的页面转换成一个BeautifulSoup对象
print(soup)
print(type(soup))

print('-'*100)
# 3.访问soup对象中的tag对象（html标签）
# bs把所有的html标签都视为tag对象，tag对象之间存在相互嵌套的包含关系，可以直接利用.语法访问soup对象中的某个tag，返回的结果是第一个符合要求的tag
print(soup.head)
# 访问soup对象中第一个名称是head的tag(HTML标签),如果该tag是一个双标签，返回的是两个标签中的所有内容
print(type(soup.head))
print(soup.title)
print(soup.meta)
# 3.1 Tag对象的属性：name,attrs
print(soup.meta.name)
# 返回Tag的名称，标签名
print(soup.meta.attrs)
# 以字典形式返回Tag的所有属性和属性值
print(soup.meta.attrs['content'])
# 返回Tag属性的值
print(soup.meta['content'])
# 对attrs简化之后的写法

print('-'*100)

#  4.访问标签中的文本 string/text
print(soup.title)
print(soup.title.string)
# string返回标签中包含的文本，本身是一个NavigableString对象，可以当成字符串使用
print(type(soup.title.string))
print(soup.meta.string)
# 如果标签中没有文本，返回None

print('-'*100)

# 4.1 特殊情况下的文本访问
strHtml = '<a href="http://www.baidu.com"><img src="1.jpg">百度一下，你就知道</a>'
soup1 = bs(strHtml,'html.parser')
print(soup1.a)
print(soup1.a.string)
# 使用string返回文本的时候，有时候容易收到tag中包含的其他tag的干扰，此时用string往往获取不到文本
print(soup1.a.text)
# text返回标签中包含的文字信息，不受其他tag的影响，text返回的是标准的字符串
print(type(soup1.a.text))

print('-'*100)

# 5.find_all和find
# 5.1 通过名称进行查找
print(soup.a)   # 百度首页中第一个a标签
print(soup.find('a'))   # 返回第一个a标签
print(soup.find_all('a'))
print(type(soup.find_all('a')))     # 搜索所有的a标签，返回的对象是一个结果集，可以视为一个序列进行处理
allATag = soup.find_all('a')
for tag in allATag:
    print(tag)

print('-'*100)

# 5.2 通过属性查找
# <a class="bri" href="//www.baidu.com/more/" name="tj_briicon" style="display: block;">更多产品</a>
print(soup.find('a',attrs = {'class':'bri','name':'tj_briicon'}))
# 利用属性搜寻标签时，attrs对应的表达式要写成字典形式，属性名对应字典的键，属性值对应字典的值
'''
<a class="mnav" href="http://news.baidu.com" name="tj_trnews">新闻</a>
<a class="mnav" href="http://www.hao123.com" name="tj_trhao123">hao123</a>
<a class="mnav" href="http://map.baidu.com" name="tj_trmap">地图</a>
<a class="mnav" href="http://v.baidu.com" name="tj_trvideo">视频</a>
<a class="mnav" href="http://tieba.baidu.com" name="tj_trtieba">贴吧</a>
'''
print(soup.find_all('a',attrs={'class':'mnav'}))
allAmnav = soup.find_all('a',class_ = 'mnav')
# 可以省略attrs字典，直接写成属性 = 属性值的形式，class是python的关键字，要改成class_
for tag in allAmnav:
    print(tag.string)

print('-'*100)

# 5.3 通过文本进行查找
print(soup.find('a',text='关于百度'))
# 查找文本中包含百度的所有a标签
print(soup.find_all('a',text = '*百度*'))
# python的字符串不支持以*作为通配符的写法
print(soup.find_all('a',text = re.compile(r'.*?百度.*?')))
# 使用正则表达式和Beautiful Soup结合完成模糊查询