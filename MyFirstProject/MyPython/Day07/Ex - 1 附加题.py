# -*- coding:utf-8 -*-
import xlrd
from xlutils.copy import copy

#1.打开原始文件取数据
myBook = xlrd.open_workbook('公司1-2月数据.xls')
# print(myBook)
mySheet1 = myBook.sheet_by_name('1月')
mySheet2 = myBook.sheet_by_name('2月')
# print(mySheet1)
# mySheet1.write(0,5,'金额')  # 用xlrd开启的表是只读对象，无法写入

#2.复制工作簿，转换成可写对象
myBookx = copy(myBook)
# print(myBookx)

#3.提取复制过后的工作簿中的表，以便进行写入操作
mySheet1x = myBookx.get_sheet(0)
mySheet2x = myBookx.get_sheet(1)
# print(mySheet2x)

#4.计算并写入订单的金额，创建两个列表存储1月和2月每个订单的金额，以便后续求总金额和最大订单金额
listMoney1 = []
listMoney2 = []

mySheet1x.write(0,5,'金额')   # 生成新表的表头
mySheet2x.write(0,5,'金额')

# rows = mySheet1x.nrows #求出最大的行数
# 利用旧表的索引来遍历新表
for rowno in range(1,mySheet1.nrows):
    # 利用行索引遍历（旧表和新表的行索引一致）
    moeny = float(mySheet1.row(rowno)[2].value) * float(mySheet1.row(rowno)[3].value) * (1-float(mySheet1.row(rowno)[4].value))
    # 计算每个订单的金额：单价*数量*（1-折扣）
    mySheet1x.write(rowno,5,moeny)
    # 在同一行索引上的第6列写入订单的金额
    listMoney1.append(moeny)
    # 把计算出的每个订单金额添加到列表中
mySheet1x.write(rowno+1,0,'总金额')
mySheet1x.write(rowno+1,5,sum(listMoney1)) # 计算总金额并写入到指定的位置

for rowno in range(1,mySheet2.nrows):
    # 利用行索引遍历（旧表和新表的行索引一致）
    moeny = float(mySheet2.row(rowno)[2].value) * float(mySheet2.row(rowno)[3].value) * (1-float(mySheet2.row(rowno)[4].value))
    # 计算每个订单的金额：单价*数量*（1-折扣）
    mySheet2x.write(rowno,5,moeny)
    # 在同一行索引上的第6列写入订单的金额
    listMoney2.append(moeny)
    # 把计算出的每个订单金额添加到列表中
mySheet2x.write(rowno+1,0,'总金额')
mySheet2x.write(rowno+1,5,sum(listMoney2)) # 计算总金额并写入到指定的位置

# 5.找出1月和2月最大金额对应的订单信息
# 5.1 求出最大金额
maxMoney1 = max(listMoney1)
maxMoney2 = max(listMoney2)
# print(maxMoney1)
# print('l' in 'hello')
# print('hello'.index('l')) # 用index可以返回序列中某个值对应的首次出现的索引
maxM1 = listMoney1.index(maxMoney1)
maxM2 = listMoney2.index(maxMoney2)
# print(maxM1)
# print(mySheet1.row(maxM1+1))
# 找出最大金额在列表中的索引，利用该索引找到最大金额订单所在的行，注意因为列表和原始数据表相比较，少了表头这一行，因此定位的时候，要在返回的索引上+1，才能得到正确的订单所在行
# print(mySheet1.row(maxM1+1)[0].value) # 获取订单编号
# print(type(mySheet1.row(maxM1+1)[0]))
print('1月最大金额订单：\n','订单号码：',mySheet1.row(maxM1+1)[0].value,'订单金额：',max(listMoney1))
print('2月最大金额订单：\n','订单号码：',mySheet2.row(maxM2+1)[0].value,'订单金额：',max(listMoney2))

# 6.提取1、2月订单号码，写入新表
myBookx.add_sheet('订单号码') # 在复制出来的工作簿中添加一张新的表，准备写入订单号码
mySheet3x = myBookx.get_sheet(2) # 定位到新添加的Worksheet
# print(mySheet3x)
mySheet3x.write(0,0,'订单号码')
# print(mySheet1.col(0)[1].value) # 返回第一条订单的编号
lineno = 1
# 构建一个变量，用来存储当前准备写入的行号，因为第一行是标题，所以索引从1开始
for info in mySheet1.col(0)[1:]:
    # 遍历旧表1（1月）订单的第1列（订单号码），跳过第一行（第一行是表头）
    # print(info.value)
    mySheet3x.write(lineno,0,info.value)
    # 在新表3中指定的位置写入1月订单信息
    lineno += 1 # 行号（指针）递增1

for info in mySheet2.col(0)[1:]:
    mySheet3x.write(lineno,0,info.value)
    lineno += 1


# 测试写入磁盘
myBookx.save('result.xls')