# -*- coding:utf-8 -*-
# 抓取豆瓣电影top250首页的信息
import urllib.request

url = 'https://movie.douban.com/top250'  #  要抓取的url
# response = urllib.request.urlopen(url)
# 因为豆瓣做了反爬处理，所以直接用urllib.request.urlopen会报错
# print(response.read().decode('utf-8'))
# 1.先构建一个用于联系服务器的request headers，用字典实现
myHeaders = {
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
# 2.构建一个包含request-headers的Request对象（请求对象），利用urllib.request.Request来进行构建
myRequest = urllib.request.Request(url,headers = myHeaders)

# 3.利用构建好的Request对象开启具有反爬措施的页面，urllib.request.urlopen
response = urllib.request.urlopen(myRequest)

# 4.观察返回的结果
print(response.read().decode('utf-8'))