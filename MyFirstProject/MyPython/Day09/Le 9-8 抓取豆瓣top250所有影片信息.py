# -*- coding:utf-8 -*-
# 抓取豆瓣电影TOP250全部影片的信息，用requests+beautiful soup实现，用xlwt写入本地文件
'''
思路：
1.处理翻页：用循环处理
2.获取每个页面的内容：requests
3.从页面中提取信息：bs+re
4.把提取到的信息写入文件：xlwt
'''

# 1.处理翻页
# 1.1 找到翻页的规律
'''
https://movie.douban.com/top250

https://movie.douban.com/top250?start=0&filter=
https://movie.douban.com/top250?start=25&filter=
https://movie.douban.com/top250?start=50&filter=
'''

def get_page(pageno):
    # pageno是要抓取的页面数量
    # 用循环处理翻页
    for pagen in range(0,pageno*25,25):
        url = 'https://movie.douban.com/top250?start=' + str(pagen) + '&filter='
        # 构建一个翻页用的url
        print(url)
        # 用requests.get 抓取每页的数据
        # 把抓到的页面写入txt文件

def get_movieinfo():
    # 读取每个txt文件，提取需要的信息，拼成一个大列表
    pass

def sav2xls():
    # 用xlwt把大列表写入xls文件
    pass


# 调试程序
get_page(10)