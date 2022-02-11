# -*- coding:utf-8 -*-
# 抓取王者荣耀所有英雄的详情页内容，并写入本地文件
'''
1.抓目英雄的图片地址、名称和详情页链接地址并保存到本地文件
1.1 抓目录页内容：webdriver+re
1.3 把抓取到的信息写入本地文件：csv
'''

from selenium import webdriver
import re
import csv

# 创建列表用于存储英雄图片地址、名称和详情页链接地址的列表
heroMenu = []

# 构建浏览器并利用正则获取英雄图片地址、名称和详情页链接地址
def get_heros():
    # 构建一个浏览器对象
    browser = webdriver.Chrome()
    # 定义URL
    heroUrl = 'https://pvp.qq.com/web201605/herolist.shtml'
    # 打开浏览器
    browser.get(heroUrl)
    # 获取页面内容
    response = browser.page_source
    # print(response)   调试用
    # 获取包含所有英雄图片地址的列表
    pn_imgUrl = re.compile(r'<li><a href=.*?src="//(.*?)".*?</a></li>')
    imgUrl = re.findall(pn_imgUrl,response)
    # print(imgUrl)     调试用
    # 获取所有英雄的名称
    pn_heroName = re.compile(r'<li><a href="herodetail/.*?" target="_blank"><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/.*?alt=".*?">(.*?)</a></li>')
    heroName = re.findall(pn_heroName,response)
    # print(heroName)   调试用
    # 获取所有英雄的链接地址
    pn_heroDetail = re.compile(r'<li><a href="(.*?)" target="_blank"><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/.*?</a></li>')
    heroDetail = re.findall(pn_heroDetail,response)
    # print(heroDetail)     调试用
    # 通过循环将获取到的信息添加在列表中
    for i in range(len(heroName)):
        print('英雄图片地址：',imgUrl[i])
        print('英雄名称：', heroName[i])
        print('英雄链接：', heroDetail[i])
        # 将获取到的信息逐个添加到列表中
        heroMenu.append((imgUrl[i],heroName[i],heroDetail[i]))
        print('-'*100)
    print(heroMenu)
    return heroMenu

# 将获取的到信息保存到本地csv文件中
def save_heros(heroMenu):
    # 定义一个csv文件对象
    with open('hero.csv', 'w', encoding='utf-8', newline='') as csvFile:
        # 构建一个用来写入内容的writer对象
        writer = csv.writer(csvFile)
        # 写入内容
        writer.writerow(heroMenu)

# 执行函数
save_heros(get_heros())

'''
<li><a href="herodetail/538.shtml" target="_blank"><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/538/538.jpg" width="91" height="91" alt="云缨">云缨</a></li>
'''