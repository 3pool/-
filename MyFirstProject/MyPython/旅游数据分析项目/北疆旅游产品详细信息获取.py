# 载入库
import csv
from bs4 import BeautifulSoup as bs
import os

tripInfo = []

def get_tripInfo():
    for root, dirs, files in os.walk('pages'):
        # 获取文件夹对应的根目录、子目录和目录中的文件名，其中files对应的目录中的文件名列表
        pass
    for eachFile in files:
        # 遍历职位文件的列表
        with open('pages/' + eachFile, 'r', encoding='utf-8') as pf:
            data_page = pf.read()
        tripSoup = bs(data_page,'html.parser')
        tagTripDiv = tripSoup.find('div',class_='main_col')
        itemTripDiv = tagTripDiv.find_all('div',class_='list_product_box js_product_item')
        for eachItem in itemTripDiv:
            try:
                departureSpan = eachItem.find('span',class_='list_product_place')
                departure = departureSpan.text
            except:
                departure = ''
            try:
                tripModeSpan = eachItem.find('span',class_='list_product_name')
                tripMode = tripModeSpan.text
            except:
                tripMode = ''
            try:
                transportP = eachItem.find('p', class_='list_product_black')
                transport = transportP.text
            except:
                transport = ''
            try:
                tripAgencyP = eachItem.find('p', class_='list_product_retail')
                tripAgency = tripAgencyP['title']
            except:
                tripAgency = ''
            try:
                tripsNumDiv = eachItem.find('div',class_='list_change_one')
                tripsNum = tripsNumDiv.text.replace('累计','').replace('人出游','')
            except:
                tripsNum = ''
            try:
                priceDiv = eachItem.find('div',class_='list_sr_price')
                price = priceDiv.text.split('￥')[1].replace('起','')
            except:
                price = ''
            try:
                titleP = eachItem.find('p',class_='list_product_title')
                title = titleP['title']
            except:
                title = ''
            try:
                isOptimizationSpan = eachItem.find('span',class_='list_product_youxuan')
                if isOptimizationSpan:
                    isOptimization = '优选'
                else:
                    isOptimization = '非优选'
            except:
                isOptimization = '非优选'
            try:
                tripTagsDiv = eachItem.find('div',class_='list_label_box')
                tripTagsSpan = tripTagsDiv.find_all('span','list_label_blue')
                tripTags = ''
                for eachTag in tripTagsSpan:
                    tripTags += eachTag.text+'/'
                tripTags = tripTags[:-1]
            except:
                tripTags = ''
            tripInfo.append((departure,tripMode,transport,tripAgency,tripsNum,price,title,isOptimization,tripTags))

            print('出发地：', departure)
            print('出团类型：', tripMode)
            print('出行工具：', transport)
            print('供应商：', tripAgency)
            print('出游人数:', tripsNum)
            print('价格:', price)
            print('标题:', title)
            print('是否优选:', isOptimization)
            print('标签:', tripTags)
            print('-' * 100)

def save_travelProducts():
    # 定义一个csv文件对象
    with open('trip.csv', 'w', encoding='utf-8', newline='') as csvFile:
        # 构建一个用来写入内容的writer对象
        writer = csv.writer(csvFile)
        # 写入内容
        title = ('departure','mode','transport','agency','number','price','title','isOptimization','tags')
        writer.writerow(title)
        writer.writerows(tripInfo)

get_tripInfo()
save_travelProducts()
