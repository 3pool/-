# 鸡兔同笼问题：35个头，94条腿，用穷举法解方程
for chick in range(1,36):
    # 鸡的数量
    for rabbit in range(1,36):
        # 兔的数量
        if chick + rabbit == 35 and chick * 2 + rabbit * 4 == 94:
            # 判断是否同时满足头和脚的数量
            print('鸡的数量：',chick,'\n兔的数量：',rabbit)