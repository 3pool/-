# -*- coding:utf-8 -*-
# 1.载入库
import urllib.request
# urllib是http请求库，是python自带的，request是发送http请求的对象
# 2.抓取指定url的页面内容
response = urllib.request.urlopen('http://www.baidu.com/')
# 开启指定的url，把对应的页面内容拉取到本地，赋予response对象
# 3.输出抓取到的信息
print(response.read().decode('utf-8'))