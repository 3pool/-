# 四、用嵌套循环实现九九表
for r in range(1,10):
    for s in range(1,r+1):
        t = str(r*s)
        print('%dx%d=%-2s'%(r,s,t), end=' ')
    print()