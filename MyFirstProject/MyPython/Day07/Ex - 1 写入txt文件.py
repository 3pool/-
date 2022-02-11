# -*- coding:utf-8 -*-
Stocks = [{'商品名称': 'AA', '价格': 39.48, '日期': '6/11/2007',
         '时间': '9:36am', '幅度': -0.18, '数量': 181800},
        {'商品名称': 'AIG', '价格': 71.38, '日期': '6/11/2007',
         '时间': '9:36am', '幅度': -0.15, '数量': 195500},
        {'商品名称': 'AXP', '价格': 62.58, '日期': '6/11/2007',
         '时间': '9:36am', '幅度': -0.46, '数量': 935000}]
# 写入磁盘文件的内容是字符串
# print(Stocks[0].keys()) # 调试用
title = ','.join(Stocks[0].keys())
# 把字典的键用,连接起来生成字符串
# print(title) # 调试用
file = open('a.txt','w',encoding='utf-8')
# 写入表头
file.write(title + '\n')

for stock in Stocks:
    # 遍历列表
    strMemo = ''
    # 构建一个空字符串，用来存储要写入的内容
    # print(stock) # 调试用
    for item in stock.values():
        # 遍历字典的值
        # print(item) # 调试用
        strMemo += ',' + str(item)
        # 将字典的值添加到字符串中
        # print(strMemo) # 调试用
    file.write(strMemo[1:] + '\n')
    # 写入内容

file.close()