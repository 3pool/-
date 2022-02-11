# -*- coding:utf-8 -*-
# 1.载入库
import csv
# 2.开启文件
with open('test.csv','r') as csvFile:
# 3.读取csv文件的内容
    result = csv.reader(csvFile)
    print(result)
    for item in result:
        # 使用循环遍历读取到的迭代器
        print(item)
        # csv.reader返回的是一个以列表元素构成的一个容器/序列，每一行对应一个列表，每一列对应列表中的一项，实质上是一个嵌套的容器

print('-'*100)
# 用嵌套的循环处理csv的嵌套序列对象
# 2.开启文件
with open('test.csv','r') as csvFile:
# 3.读取csv文件的内容
    result = csv.reader(csvFile)
    for iRow in result:
        # 外层循环处理行
        for iColumn in iRow:
            print(iColumn,end='\t')
            print(type(iColumn))
            # 行内的列不换行
        print()
        # 外层循环换行

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
    writer.writerow(memo)