# -*- coding:utf-8 -*-
# 1.载入库
import xlrd
import xlutils.copy
# 载入xlutils中的copy对象
# 2.利用xlrd打开要修改的工作簿
myBook = xlrd.open_workbook('score.xls')
# 3.在开启的工作簿上复制出一个用来进行修改的副本
myBookX = xlutils.copy.copy(myBook)
# 利用xlutils中的copy对象的copy方法获取一个用来进行修改的工作簿，这个复制出来的工作簿是可写的
# 4.定位到要修改的工作表
mySheetX = myBookX.get_sheet(0)
# 利用索引返回指定的工作表
print(mySheetX)
# 5.修改内容（在修改的位置进行写入）
mySheetX.write(0, 0, '学号')
# 6.把修改过的副本写入到磁盘文件
myBookX.save('score1.xls')
