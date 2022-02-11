# -*- coding:utf-8 -*-
# 1.载入库
import csv
# 2.开启文件准备写入
with open('new.csv','w',encoding='utf-8',newline='') as csvFile:
# newline=''，是不在每一行后面添加换行符
# 3.构建一个用来写入内容的writer对象
    writer = csv.writer(csvFile)
# 4.写入
# 4.1 写入表头，用单行方式
    title = ['序号','网站','网站名称']
    writer.writerow(title)
    # 写入单行，容器中的每一项会成为csv的一列
# 4.2 写入内容，用多行的方式，内容必须是一个嵌套的容器
    memo = [
        [1,'http://www.baidu.com','百度'],
        [2,'http://www.jd.com','京东'],
        [3,'http://www.taobao.com','淘宝']
    ]
    writer.writerows(memo)