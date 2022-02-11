# 一、用函数实现求100以内的质数（即只能被1和自身整除的数，一般认为从2开始）。
listnum = []
for num in range(2,100):
    for i in range(2,num-1):
        if num%i == 0:
            break
    else:
        listnum.append(num)
print('100以内所有的质数为：',listnum)