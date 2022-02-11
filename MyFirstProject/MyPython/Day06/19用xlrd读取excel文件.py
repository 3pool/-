# -*- coding:utf-8 -*-
# 1.载入库
import xlrd
print('打开工作簿')
# 2.打开工作簿
myBook = xlrd.open_workbook('某公司贸易数据.xls')
# 开启指定的文件，并赋予myBook对象
print(myBook)
print('-'*100)
# 3.打开工作表
print('打开产品类别表')
mySheet = myBook.sheet_by_index(0)
print(mySheet)
# 4.访问数据
print('按行访问')
print('-'*100)
rows = mySheet.nrows
# 返回所有数据的行数
print(rows)
for iRow in range(rows):
    # 遍历所有行的索引
    print(mySheet.row_values(iRow))
    # 返回表中每一行的数据
# 5.特定位置进行访问
print(mySheet.cell(1,1).value)
# cell是按照行，列的索引来访问数据
# 6.遍历访问所有数据
print('遍历访问')
print('-'*100)
rows = mySheet.nrows
# 返回所有数据的行数
columns = mySheet.ncols
# 返回所有列对应的列数
print(columns)
for iRow in range(rows):
    # 外层循环处理行
    for iCols in range(columns):
        # 内层循环处理列
        print(mySheet.cell(iRow,iCols).value,end='\t\t\t\t\t')
        # 返回行列索引对应的单元格值
    print()