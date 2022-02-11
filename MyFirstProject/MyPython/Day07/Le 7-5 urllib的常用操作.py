# -*- coding:utf-8 -*-
# 1.载入库
import urllib.request
# urllib是http请求库，是python自带的，request是发送http请求的对象
# 2.抓取指定url的页面内容
response = urllib.request.urlopen('http://www.baidu.com/')
# 开启指定的url，把对应的页面内容拉取到本地，赋予response对象
# 3.输出抓取到的信息
print(response)
# 3.1 read()
# 返回未经解码的字节流，需要用decode转换成字符串
# print(response.read().decode('utf-8'))
# 3.2 readlines()
# 返回所有行的字节六组成的列表
# print(response.readlines())
# for line in response.readlines():
#     print(line.decode('utf-8'))
# 3.3 其他常用方法
# 3.3.1 getcode()返回服务器发回的状态码，200表示连接成功
# print(response.getcode())
# 3.3.2 info() 返回服务器的响应头信息
print(response.info())