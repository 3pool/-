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
            # 行内的列不换行
        print()
        # 外层循环换行