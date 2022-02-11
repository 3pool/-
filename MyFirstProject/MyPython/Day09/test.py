import requests
from bs4 import BeautifulSoup as bs
url = 'http://www.baidu.com'
response = requests.get(url)
response.encoding = 'utf-8'
soup = bs(response.content,'html.parser')
# 把抓取到的页面转换成一个BeautifulSoup对象
print(response.content)
print(type(response.content))
