# -*- coding:utf-8 -*-
# 抓取豆瓣电影top250每部影片的详细信息
'''
思路：
1.抓取影片的目录和目录对应的链接
1.1 处理目录页的翻页：用循环结合url实现
1.2 抓取目录页的内容：requests
1.3 将对应的目录页写入本地文件
1.4 从文件中提取详情页的链接
2.将抓取到的目录和链接写入磁盘文件
3.读取文件获得链接
4.利用链接进入详情页，抓取页面内容，并写入本地文件
5.读取详情页文件，从中提取需要的信息
6.把抓取到的信息写入表格
'''

# 0.预备工作
# 0.1 载入库
import requests
import re
from bs4 import BeautifulSoup as bs
import xlrd
import xlwt
import os


# 0.2 全局设置
linklist = []
# 存放详情页的链接
datalist = []
# 存放影片的所有信息

# 1.抓取影片的目录和目录对应的链接
# 1.1 处理目录页的翻页：用循环结合url实现
'''
https://movie.douban.com/top250?start=0&filter=
https://movie.douban.com/top250?start=25&filter=
https://movie.douban.com/top250?start=50&filter=
'''

# 1.2 抓取目录页的内容：requests
def get_index(pageno):
    # pageno是目录页的页码
    for i in range(0,pageno*25,25):
        # 构建翻页的url
        url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
        # print(url)  # 调试用
        print('正在抓取第',str(i//25+1),'页目录，请稍后...')
        # 抓取目录页内容
        response = requests.get(url,headers = {'User-Agent':'Mozilla / 5.0'})
        response.encoding = 'utf-8'
        # print(response.text)    # 调试用

        # 1.3 将对应的目录页写入本地文件
        # 构建一个用来存放目录页的文件夹
        os.makedirs('top250menu',exist_ok=True)
        # 构建用来写入的文件名，注意文件名中要包含路径
        filename = 'top250menu/index' + str(i//25+1) + '.txt'
        # 将抓取到的页面写入文件
        with open(filename,'w',encoding='utf-8') as tfp:
            tfp.write(response.text)

# 测试函数
get_index(10)