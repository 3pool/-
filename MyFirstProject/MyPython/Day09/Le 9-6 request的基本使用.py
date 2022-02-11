# -*- coding:utf-8 -*-
#  1.载入库
import requests

# 2.访问页面内容
url = 'http://www.baidu.com'
response = requests.get(url)
# 用get方法url对象，返回页面的内容
print(response)
# 直接输出response对象，得到的状态码
print(type(response))
print(response.text)
# 返回已经进行自动解码的字符串，但requests的自动解码功能在中文中容易出错，需要自己手动解码
print(type(response.text))
print('-'*100)
# 方法1，获取content，再手动解码
print(response.content.decode('utf-8'))
# 方法2. 先设定response的encoding属性，然后再获取解码后的text
print('-'*100)
response.encoding = 'utf-8'
print(response.text)

print('-'*100)

# 3.爬取具有反爬措施的网站
url1 = 'https://movie.douban.com/top250'
response1 = requests.get(url1)
print(response1)
# 如果抓不到内容，会返回错误的状态码，不会产生异常导致程序中断
print(response1.text)
# 抓不到内容。text为空
print('-'*100)
# 3.1 在requests中添加requests headers
myHeaders = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
# 先构建一个基于字典的request headers
response2 = requests.get(url1,headers = myHeaders)
# 直接将request headers加入get方法
print(response2)
print(response2.text)

print('-'*100)

# 4.抓取非文字性内容（图片）
# 抓取豆瓣明星图片
urlPic = 'https://img1.doubanio.com/view/photo/l/public/p2166038138.webp'
resPic = requests.get(urlPic)
print(resPic)
print(resPic.text)
# 针对非文字性的内容，用text返回的是乱码
print('-'*100)
print(resPic.content)
# content返回的是图片的字节流
# 将获取到的字节流写入磁盘文件
with open('image1.jpg','wb') as img:
    # wb是以二进制方式写入（针对字节流）
    img.write(resPic.content)