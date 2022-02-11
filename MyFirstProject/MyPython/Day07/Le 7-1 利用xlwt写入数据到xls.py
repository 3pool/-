# -*- coding:utf-8 -*-
# 1.引入库
import xlwt
import random
# 2.创建工作簿
myBook = xlwt.Workbook(encoding='utf-8')
# 创建一个工作簿并设定编码
# 3.创建工作表
mySheet = myBook.add_sheet('学生成绩')
# 4.定位和写入
# mySheet.write(row_index,col_index,value)
# 4.1 写入表头
mySheet.write(0, 0, 'ID')
mySheet.write(0, 1, '语文')
mySheet.write(0, 2, '数学')
mySheet.write(0, 3, '英语')
# 4.2 写入数据：用嵌套的循环处理结构化的数据
for iRow in range(10):
    # 外层循环处理行
    mySheet.write(iRow+1, 0, iRow+1)
    # 写入ID，因为ID一行只需要一次，放在外层循环中，注意iRow+1既是行的索引，也是要写入的ID的值
    for iCol in range(3):
        # 内层循环处理列，去除ID列之后，只有3列
        mySheet.write(iRow + 1, iCol + 1,random.randint(50,100))
        # 在指定的单元格写入随机的成绩
# 5.把内存中的工作簿写入本地磁盘文件
myBook.save('score.xls')
