# 三、百元百鸡问题：公鸡3元每只，母鸡5元每只，小鸡1元3只，一百元钱买一百只鸡。请求出公鸡，母鸡和小鸡的数目（每种鸡至少1只）
# 用嵌套循环实现
for a in range(1,32):
    for b in range(1,20):
        for c in range(1,99):
            if 3*a+5*b+c/3 == 100 and a+b+c == 100:
                print('公鸡%d只，母鸡%d只，小鸡%d只'%(a,b,c))

print('-'*100)

# 用单循环实现
for a in range(1,32):
    if 3*a+5*((100-4*a)//7)+((600-3*a)//7)//3 and a+(100-4*a)//7+(600-3*a)//7 == 100 and 100-4*a >= 7 and 600-3*a >= 7:
            print('公鸡%d只，母鸡%d只，小鸡%d只'%(a,(100-4*a)//7,(600-3*a)//7))

print('-'*100)

# 用推导式实现
list1 = [(a,b,c) for a in range(1,32) for b in range(1,20) for c in range(1,99) if 3*a+5*b+c/3 == 100 and a+b+c == 100]
for i in range(0,len(list1)):
    print('公鸡%d只，母鸡%d只，小鸡%d只'%(list1[i][0],list1[i][1],list1[i][2]))