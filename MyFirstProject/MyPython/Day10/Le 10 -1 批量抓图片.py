# -*- coding:utf-8 -*-
# 批量抓取豆瓣影星照片，并保存到本地
'''
思路：
1.处理翻页：用循环
2.从每个页面提取照片对应的url
3.在本地创建用于保存照片的文件夹
4.构建保存图片的文件名称
5.把提取到的照片url保存到本地文件
'''
# 载入库
import urllib.request
import requests
from bs4 import BeautifulSoup as bs
import re
import os

# 1.处理翻页
'''
https://movie.douban.com/celebrity/1354284/photos/?type=C&start=0&sortby=like&size=a&subtype=a
https://movie.douban.com/celebrity/1354284/photos/?type=C&start=30&sortby=like&size=a&subtype=a
https://movie.douban.com/celebrity/1354284/photos/?type=C&start=60&sortby=like&size=a&subtype=a
'''
def get_pics(pageno):
    # pageno是要抓取照片的页数
    # 1.1 构建翻页用的url
    for i in range(pageno):
        print('正在抓取第',i+1,'页图片，请稍后...')
        pic_url = 'https://movie.douban.com/celebrity/1354284/photos/?type=C&start=' + str(i*30) + '&sortby=like&size=a&subtype=a'
        # 目录页的url

        # 2.提取目录页中照片的url
        response = requests.get(pic_url,headers = {'User-Agent':'Mozilla / 5.0'})
        # 获取页面内容
        # print(response.text)    # 调试用
        # 2.1 将页面转成soup
        picSoup = bs(response.text,'html.parser')
        # print(picSoup)  # 调试用
        # 2.2 利用bs提取每张照片对应的img标签的src属性的值
        # 2.2.1 搜索包含所有图片的ul标签
        tagUl = picSoup.find('ul',class_='poster-col3 clearfix')
        # print(tagUl)    # 调试用
        # 2.2.2 搜索ul标签中所有的img标签
        tagImgs = tagUl.find_all('img')
        # 返回结果是所有img标签构成的结果集
        # print(tagImgs)  # 调试用
        # for img in tagImgs:   # 调试用
        #     print(img)    # 调试用
        # 3.创建文件集：为了方便管理，将每页上的照片都抓取到一个单独的文件夹中，文件夹的名称由页数的索引决定
        # os.makedirs()
        path = '李一桐\pic' + str(i+1)
        # 构建一个可变的路径名称
        os.makedirs(path,exist_ok=True)
        # 按照指定的路径和文件夹的名称创建文件夹

        # 4.构建保存的文件名（把图片文件的url转换成可以在本地保存的文件名）
        for img in tagImgs:
            # 遍历抓取到的图片标签
            img_url = img['src']
            # 抓取每个img标签的src属性，返回图片的url
            # print(img_url)  # 调试用
            img_name = img_url.split('/')[-1]
            # 对图片的url用'/'进行分割，取得的列表中的最后一项就是文件名
            # print(img_name)     # 调试用
            # 上面得到的图片文件名未带路径，不能直接保存，还需要和path结合起来，才能构成一个放置在指定文件夹下的图片文件名
            file_name = path + '/' + img_name
            # 因为'\'一般作为转义符的标识进行使用，为避免歧义，一般路径中可以用'/'代替
            # print(file_name)    # 调试用
            # 5.把抓取到的照片url下载到本地文件
            # urllib.request.urlretrieve()
            try:
                # 为了避免抓取图片出错，把抓取的动作放在try...except中
                # 因为豆瓣做了反爬处理，所以直接抓取图片，容易出现418错误，解决办法是在urlretrieve中加入request-headers
                opener = urllib.request.build_opener()
                # 创建一个opener对象
                opener.addheaders = [('User-Agent','Mozilla / 5.0')]
                # 为opener对象添加request-headers，注意添加的格式是列表中的元组
                urllib.request.install_opener(opener)
                # 将添加了request-headers的opener对象安装到request对象中
                urllib.request.urlretrieve(img_url,file_name)
                # urlretrieve的功能是把网络上的url抓取到本地，并存入指定的filename，实现下载的功能
            except Exception as e:
                print(e)


# 调试函数
get_pics(3)

'''
<ul class="poster-col3 clearfix">
    

        <li>
            <div class="cover">
                <a href="https://movie.douban.com/celebrity/1275620/photo/2007605347/" class="">
                    <img src="https://img1.doubanio.com/view/photo/m/public/p2007605347.webp" class="">
                </a>
            </div>

            <div class="prop">
                2501x3751
            </div>
                <div class="name">
            
                        <a href="https://movie.douban.com/celebrity/1275620/photo/2007605347/#comments">110回应</a>
                </div>
        </li>
</ul>
'''