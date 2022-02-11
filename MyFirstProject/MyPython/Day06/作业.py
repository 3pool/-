Stocks = [{'商品名称': 'AA', '价格': 39.48, '日期': '6/11/2007',
         '时间': '9:36am', '幅度': -0.18, '数量': 181800},
        {'商品名称': 'AIG', '价格': 71.38, '日期': '6/11/2007',
         '时间': '9:36am', '幅度': -0.15, '数量': 195500},
        {'商品名称': 'AXP', '价格': 62.58, '日期': '6/11/2007',
         '时间': '9:36am', '幅度': -0.46, '数量': 935000}]

with open('order.txt','w') as Order:
    for i in Stocks[0].keys():
        if i != '数量':
            Order.write(str(i)+',')
        else:
            Order.write(str(i)+'\n')
    for j in Stocks:
        for k in j.keys():
            if k != '数量':
                Order.write(str(j[k])+',')
            else:
                Order.write(str(j[k])+'\n')