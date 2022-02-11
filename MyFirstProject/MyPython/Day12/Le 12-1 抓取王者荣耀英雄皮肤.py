# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

# 使用requests抓取，无效
def get_pics_by_requests():
    url = 'https://pvp.qq.com/web201605/herodetail/131.shtml'
    response = requests.get(url)
    response.encoding = 'gbk'
    print(response.text)    # 调试用
    print('-'*100)
    soup = bs(response.text,'html.parser')
    tagUl = soup.find('ul', class_='pic-pf-list pic-pf-list3')
    print(tagUl)
    print('-'*100)
    tagLi = tagUl.find_all('li')
    # 找不到，因为是放在注释里的
    # print(tagLi)
    myContents = tagUl.contents
    # contents返回tag的子对象
    # print(myContents)
    # print(len(myContents))
    strLi = myContents[1]
    print(strLi)
    print('-'*100)
    tagImgs = bs(strLi,'html.parser').find_all('img')
    print(tagImgs)
    for img in tagImgs:
        print(img['src'])

# 使用selenium抓取
def get_pics_by_selenium():
    # 1.创建浏览器
    browser = webdriver.Chrome()
    # 调用Chrome函数，创建一个google chrome对象（浏览器）
    # 2.访问url
    url = 'https://pvp.qq.com/web201605/herodetail/131.shtml'
    browser.get(url)
    # 3.返回页面内容
    strPage = browser.page_source
    # 返回当前chrome浏览器中页面的内容，对象类型是字符串
    # print(strPage)  # 调试用
    # print(type(strPage))    # 调试用

    # 4.抓取皮肤图片（利用BeautifulSoup实现）
    picSoup = bs(strPage,'html.parser')
    tagUl = picSoup.find('ul',class_='pic-pf-list pic-pf-list3')
    # print(tagUl)    # 调试用
    pics = tagUl.find_all('img')
    for pic in pics:
        print(pic['data-imgname'])
    print('-'*100)

    # 5.利用Selenium自身完成
    # 5.1 如何在selenium中返回对象
    # browser.find_element_by_id()
    # browser.find_element_by_tag_name()
    # browser.find_element_by_xpath()
    # find_element是返回符合条件的单个对象
    # browser.find_elements_by_tag_name()
    # find_elements是返回符合条件的所有对象，结果是列表
    emUl = browser.find_element_by_class_name('pic-pf-list')
    print(emUl)
    print(type(emUl))
    # 在元素上也可以使用find_类的方法
    emImgs = emUl.find_elements_by_tag_name('img')
    print(emImgs)   # 调试用
    print(type(emImgs))  # 调试用
    for item in emImgs:
        print(item.get_attribute('data-imgname'))
    print('-'*100)
    # 5.2 如何在selenium中返回对象的元素
    # < li > <iclass ="curr" > < img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-smallskin-1.jpg" alt="" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-1.jpg" data-title="青莲剑仙" data-icon="0" > < / i > < p > 青莲剑仙 < / p > < / li >
    # xxx.text 返回标签的文本
    # xxx.get_attribute('属性名称') 返回标签属性对应的值
    emLi = emUl.find_elements_by_tag_name('li')
    # print(emLi)
    for item in emLi:
        print(item.text)

    print('-'*100)
    for i in range(len(emLi)):
        print(emLi[i].text,'：https:' + emImgs[i].get_attribute('data-imgname'))
    input('暂停中，请按回车继续')
    # 暂停
    browser.quit()
    # 关闭浏览器




# 测试函数
# get_pics_by_requests()
get_pics_by_selenium()
'''
<ul class="pic-pf-list pic-pf-list3" data-imgname="青莲剑仙&amp;0|范海辛&amp;0|千年之狐&amp;12|凤求凰&amp;20|敏锐之力&amp;30|鸣剑·曳影&amp;26"><li><i class=""><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-smallskin-1.jpg" alt="" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-1.jpg" data-title="青莲剑仙" data-icon="0"></i><p>青莲剑仙</p></li><li><i class=""><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-smallskin-2.jpg" alt="" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-2.jpg" data-title="范海辛" data-icon="0"></i><p>范海辛</p></li><li><i class=""><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-smallskin-3.jpg" alt="" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-3.jpg" data-title="千年之狐" data-icon="12"></i><p>千年之狐</p></li><li><i class="curr"><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-smallskin-4.jpg" alt="" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-4.jpg" data-title="凤求凰" data-icon="20"></i><p>凤求凰</p></li><li><i class=""><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-smallskin-5.jpg" alt="" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-5.jpg" data-title="敏锐之力" data-icon="30"></i><p>敏锐之力</p></li><li><i class=""><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-smallskin-6.jpg" alt="" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-6.jpg" data-title="鸣剑·曳影" data-icon="26"></i><p>鸣剑·曳影</p></li></ul>
'''
'''
<ul class="pic-pf-list pic-pf-list3" data-imgname="青莲剑仙&amp;0|范海辛&amp;0|千年之狐&amp;12|凤求凰&amp;20|敏锐之力&amp;30|鸣剑·曳影&amp;26"><li><i class="curr"><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-smallskin-1.jpg" alt="" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-1.jpg" data-title="青莲剑仙" data-icon="0"></i><p>青莲剑仙</p></li><li><i><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-smallskin-2.jpg" alt="" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-2.jpg" data-title="范海辛" data-icon="0"></i><p>范海辛</p></li><li><i><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-smallskin-3.jpg" alt="" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-3.jpg" data-title="千年之狐" data-icon="12"></i><p>千年之狐</p></li><li><i><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-smallskin-4.jpg" alt="" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-4.jpg" data-title="凤求凰" data-icon="20"></i><p>凤求凰</p></li><li><i><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-smallskin-5.jpg" alt="" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-5.jpg" data-title="敏锐之力" data-icon="30"></i><p>敏锐之力</p></li><li><i><img src="//game.gtimg.cn/images/yxzj/img201606/heroimg/131/131-smallskin-6.jpg" alt="" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/131/131-bigskin-6.jpg" data-title="鸣剑·曳影" data-icon="26"></i><p>鸣剑·曳影</p></li></ul>
'''