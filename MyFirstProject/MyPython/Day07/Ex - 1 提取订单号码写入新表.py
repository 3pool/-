# -*- coding:utf-8 -*-
# 1.载入库
import xlrd
import xlwt
# 2.打开xls文件
myBook = xlrd.open_workbook('公司1-2月数据.xls')
print(myBook) #调试用
# 3.打开工作表
sheetJan = myBook.sheets()[0]
print(sheetJan) #调试用
sheetFeb = myBook.sheets()[1]
print(sheetFeb) #调试用
# 4.提取1月和2月的订单编号
rowsJan = sheetJan.nrows # 返回表的行数
rowsFeb = sheetFeb.nrows # 返回表的行数
print(rowsJan,rowsFeb) #调试用
listNum = []
# 构建一个空列表，用来存储要写入的订单号码
for row1 in range(1,rowsJan):
    # 遍历1月表的行，注意因为有表头，所以索引从1开始
    listNum.append(sheetJan.cell(row1,0).value)
    # 提取1月的订单号码，添加到listNum中
print(listNum) #调试用
for row2 in range(1,rowsFeb):
    # 遍历2月表的行，注意因为有表头，所以索引从1开始
    listNum.append(str(int(sheetFeb.cell(row2,0).value)))
    # 提取2月的订单号码，添加到listNum中，因为2月的订单号码是浮点数，用int转换为整数，再转换成字符串
print(listNum) #调试用
# 5.构建一个用来写入的工作簿
newBook = xlwt.Workbook()
newBook = xlwt.Workbook()
# 6.在工作簿中创建用来写入的工作表
newSheet = newBook.add_sheet('订单号码')
# 7.在工作表中写入数据
# 7.1 写入表头
newSheet.write(0,0,'订单号码')
# 7.2 写入数据
for iRow in range(len(listNum)):
    # 外层循环处理行，这里因为只有一列，所以不用写内层循环，循环的次数就是列表中元素的数量，也就是要写入的行数
    newSheet.write(iRow+1,0,listNum[iRow])
    # 在指定的单元格写入对应的数据，循环变量正好就是列表的索引
# 8.把工作簿保存到磁盘文件
newBook.save('订单.xls')

