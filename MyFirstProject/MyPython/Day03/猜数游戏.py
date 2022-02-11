# -*- coding:utf-8 -*-
# 规则：计算机生成一个1-10的随机整数，用户输入数字，当输入的数字大于计算机生成的数字，提示太大，小于提示太小，等于游戏结束，给出提示
# 1.导入库
import random
# 2.生成随机数
iComputer = random.randint(1,10) # 返回1-10的随机整数
iGuess = int(input('请输入您猜的数字：'))
# # 3.判断
# if iGuess == iComputer:
#     print('猜对了，没有奖励@_@')
# elif iGuess > iComputer:
#     print('太大')
# else:
#     print('太小')
# 循环变量 ：iGuess
# 循环条件 : 没有猜对，iGuess != iComputer
# 循环变量的初值 : input获取
# 循环变量的改变 ：重新input
# 3.循环进行游戏
while iGuess != iComputer :
    # 两者不相等时循环
    if iGuess > iComputer:
        print('太大了')
    else:
        print('太小了')
    iGuess = int(input('请重新输入您猜的数字：'))
    # 在循环中改变循环变量
print('猜对了，没有奖励@_@')
