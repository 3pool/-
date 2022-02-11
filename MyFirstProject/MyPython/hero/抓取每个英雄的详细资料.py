# -*- coding:utf-8 -*-
# 抓取王者荣耀所有英雄的详情页内容，并写入本地文件
'''
1.抓取详情页内容
1.1 打开保存的链接文件，获取详情页链接
1.2 针对详情页进行信息抓取：selenium+re
1.3 把详情页内容写入磁盘文件：csv
'''

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re
import time
import csv

# 构建一个用于存储英雄详细信息的列表
heroInfos = []
# 构建一个用于识别英雄角色的字典
heroSortMenu = {'1':'战士','2':'法师','3':'坦克','4':'刺客','5':'射手','6':'辅助'}

# 读取csv文件中每个英雄的链接,并获取每个英雄的详细信息
def get_heroinfos():
    # 构建一个浏览器对象
    browser = webdriver.Chrome()
    # 定义一个csv文件对象，用于读取所有英雄的链接
    with open('hero.csv', 'r',encoding='utf-8') as csvFile:
        # 读取csv文件的内容
        result = csv.reader(csvFile)
        # 构建循环来读取文件信息
        for iRow in result:
            for iColumn in iRow:
                # print(iColumn)    调试用
                # 由于获取到的信息是字符串，需要进行处理后在使用
                heroDetail = iColumn.split("'")[-2]
                # 创建每个英雄链接的URL
                heroUrl = 'https://pvp.qq.com/web201605/' + heroDetail
                # 打开浏览器
                browser.get(heroUrl)
                # 获取浏览器页面内容
                response = browser.page_source
                # 转换成soup对象
                heroSoup = bs(response,'html.parser')
                # print(heroSoup)   调试用

                try:
                    # 获取包含英雄详情的div标签
                    tagHeroDiv = heroSoup.find('div',class_ = 'cover')
                    # 获取英雄的名称
                    tagHeroName = tagHeroDiv.find('h2',class_ = 'cover-name').text
                    print('英雄名称：', tagHeroName)
                except:
                    tagHeroName = ''

                try:
                    # 获取包含英雄角色的span标签
                    tagHeroSpan = tagHeroDiv.find('span',class_ = 'herodetail-sort')
                    # 获取英雄的角色
                    pn_tagHeroSpan = re.compile(r'<span class="herodetail-sort"><i class="herodetail-sort-(.*?)"></i></span>')
                    heroSort = heroSortMenu[re.findall(pn_tagHeroSpan,str(tagHeroSpan))[0]]
                    # print(heroSortKey[0])
                    print('英雄角色：',heroSort)
                except:
                    heroSort = ''

                try:
                    # 获取包含英雄生存能力的span标签
                    tagBar1Span = tagHeroDiv.find('span',class_ = 'cover-list-bar data-bar1 fl')
                    # 获取英雄的生存能力
                    heroBar1 = tagBar1Span.find('i',class_ = 'ibar')['style'][6:]
                    print('生存能力：',heroBar1)
                except:
                    heroBar1 = ''

                try:
                    # 获取包含英雄攻击伤害的span标签
                    tagBar2Span = tagHeroDiv.find('span', class_='cover-list-bar data-bar2 fl')
                    # 获取英雄的攻击伤害
                    heroBar2 = tagBar2Span.find('i', class_='ibar')['style'][6:]
                    print('攻击伤害：',heroBar2)
                except:
                    heroBar2 = ''

                try:
                    # 获取包含英雄技能效果的span标签
                    tagBar3Span = tagHeroDiv.find('span', class_='cover-list-bar data-bar3 fl')
                    # 获取英雄的技能效果
                    heroBar3 = tagBar3Span.find('i', class_='ibar')['style'][6:]
                    print('技能效果：',heroBar3)
                except:
                    heroBar3 = ''

                try:
                    # 获取包含英雄上手难度的span标签
                    tagBar4Span = tagHeroDiv.find('span', class_='cover-list-bar data-bar4 fl')
                    # 获取英雄的上手难度
                    heroBar4 = tagBar4Span.find('i', class_='ibar')['style'][6:]
                    print('上手难度：',heroBar4)
                except:
                    heroBar4 = ''

                print('-'*100)
                # 将获取到的所有信息添加到列表中
                heroInfos.append((tagHeroName,heroSort,heroBar1,heroBar2,heroBar3,heroBar4))

                # 暂停5秒
                time.sleep(5)
    # 返回列表作为结果
    return heroInfos

# 将获取到的列表中的信息保存到本地csv文件中
def save_heroinfos(heroinfos):
    # 定义一个csv文件对象
    with open('herodetail.csv', 'w', encoding='utf-8', newline='') as csvFile:
        # 构建一个用来写入内容的writer对象
        writer = csv.writer(csvFile)
        # 写入内容
        writer.writerow(heroinfos,end = '/t')

save_heroinfos(get_heroinfos())

'''
<span class="cover-list-bar data-bar1 fl"><b class="icon"></b><i class="ibar" style="width:60%"></i></span>
'''