# -*- coding:utf-8 -*-
# 用嵌套的循环处理二维结构：标准的二维结构
for iRow in range(1,7):
    # 用外层的循环处理行
    for iColumn in range(1,7):
        # 用内层的循环处理列
        print('第%d列，第%d行  '%(iColumn,iRow),end='')
        # 设置end=''使得在同一行的数据输出时不产生换行的效果
    print()
    # 在外层循环中，用空的print语句产生换行
print('-'*100)
# 用嵌套循环处理不标准的二维结构
for iRow in range(1,7):
    # 用外层的循环处理行
    for iColumn in range(1,iRow+1):
        # 用内层的循环处理列，列数随着行数的变化而变化
        print('第%d列，第%d行  '%(iColumn,iRow),end='')
        # 设置end=''使得在同一行的数据输出时不产生换行的效果
    print()
    # 在外层循环中，用空的print语句产生换行
print('-'*100)
for iRow in range(1,7):
    for iColumn in range(1,iRow+1):
        print('*',end='')
    print()