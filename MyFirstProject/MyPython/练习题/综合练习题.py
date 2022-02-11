# 第一题：有一个操场圈了32个区域，在第一个区域里面放1个球，重量是0。1KG，第二个李阿敏放2个球，第三个里面放4个球，以此类推，球操场上放的所有球的重量
#方法一
h = 0
s = 0
while s < 32:
    h = h+0.1*2**s
    s+= 1
print(f"所有球的重量为：{h}KG")

#方法二
weight = 0.1
list1 = []
for i in range(32):
    list1.append(2**i)
print(list1)
print(f"所有球的重量为：{weight*sum(list1)}KG")


# 第二题：百元百鸡问题：公鸡3元每只，母鸡5元每只，小鸡1元3只，一百元钱买一百只鸡，请求出公鸡，母鸡和小鸡的数目

for a in range(0,34):
    for b in range(0,21):
        for c in range(0,101):
            if 3*a+5*b+c/3 == 100 and a+b+c == 100:
                print(f'公鸡{a}只，母鸡{b}只，小鸡{c}只')

# 第三题：一个小孩买了价值少于1美元的糖，并将1美元的钱交给售货员，售货员希望用数目最少的硬币找给小孩，假设提供了数目不限的，
# 面值为25美分，10美分，5美分及1美分的硬币，写一个算法让售货员用最少的硬币数找给小孩
#方法一(该写法逻辑有问题，比如糖果价格=5或者55时,所以该方法不合适)
# pay = input(f'请输入糖果的价格：')
# back = 100-int(pay)
# back25 = int(back/25)
# back10 = int((back-int(back/25)*25)/10)
# if back%10 >=5:
#     back5 = 1
# else:
#     back5 = 0
# back1 = back%5
# print(f'找了{back25}个25美分，{back10}个10美分，{back5}个5美分，{back1}个1美分')

#方法二
#a个25美分，b个10美分，c个5美分，d个1美分
#25美分最多3个，10美分最多2个，5美分最多1个，1美分最多4个
x = 55
for a in range(4):
    for b in range(3):
        for c in range(2):
            for d in range(5):
                if 25*a+10*b+5*c+d+x == 100:
                    print(a,b,c,d)

#方法三
#硬币数量越少越好，也就是大额的硬币数量越多越好，优先选择大额的硬币
for a in range(3,-1,-1):
    for b in range(2,-1,-1):
        for c in range(1,-1,-1):
            for d in range(4,-1,-1):
                if 25*a+10*b+5*c+d+x == 100:
                    print(a,b,c,d)

# 第四题：小猴第一天摘下若干枣子，当即吃掉了一半，不过瘾又多吃了一个，第二天吃了剩下的一半又多吃了一个；
# 以后每一天都吃了前一天剩下的一半多一个。到第10天小猴再想吃时，捡到只剩下一只枣子了，问第一天这堆枣子有多少个？

zao = 1
for i in range(10):
    zao = (zao+1)*2
    i+=1
print(f'第一天这堆枣子有{zao}个')

# 第五题：打印九九乘法表
# 第一种九九乘法表
for m in range(1,10):
    for n in range(1,10):
        j=m*n
        if j < 10:
            print(j,end='      ')
        else:
            print(j,end='     ')

        if n == 9:
            print('\n')

# 第二种九九乘法表
for r in range(1,10):
    for s in range(1,r+1):
        print(f'{s}x{r}={r*s}',end=' ')
    print()
#用格式化字符串%-2s来对其，占2个位置，靠左对齐
for r in range(1,10):
    for s in range(1,r+1):
        print(f'%-2sx %-2s= %-2s'%(s,r,s*r),end=' ')
    print()
#格式化字符串，是可以多次嵌套使用的
for r in range(1,10):
    for s in range(1,r+1):
        str1 = f'{s}x{r}={r*s}'
        print(f'%-7s'%str1,end=' ')
    print()

#自然数求和
he = 0
for i in range(100):
    he+=i
    if he >=1000:
        print(i,he)
        break