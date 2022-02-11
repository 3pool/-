# 一、创建一个猜数游戏，计算机随机生成一个1-9的整数，玩家输入数字，
# 如果猜对，给出正确提示，如果猜错，给出太小或太大的提示，玩家有3次机会，均猜不中，则游戏结束。
import random
num = random.randint(1,10)
for i in range(1,4):
    if i < 3:
        guess = int(input('请输入您猜的数字：'))
        if guess == num:
            print('恭喜您，猜对了！')
            break
        elif guess < num:
            print('太小了')
        else:
            print('太大了')
    else:
        guess = int(input('请输入您猜的数字：'))
        if guess == num:
            print('恭喜您，猜对了！')
            break
        elif guess < num:
            print('太小了')
            print('很遗憾，超过三次仍未猜中，正确答案是：%d,下次继续努力！' % (num))
        else:
            print('太大了')
            print('很遗憾，超过三次仍未猜中，正确答案是：%d,下次继续努力！'%(num))
