# 写入指定的内容到文本文件
# 1.开启文件对象
txtfile = open('123.txt','w')
# 以写入的方式开启一个文本文件的对象，并将其结果返回给txtfile
# 2.准备写入的内容
x = list(range(0,10))
# 准备一个列表，把列表中的每一行作为文件中的一行
# 3.写入
for item in x:
    txtfile.write(str(item)+'\n')
# write只能写入字符串，所以要把其他类型的数据转换为字符串，写入操作不会自动换行，因此要自己来构建换行
# 4.关闭文件
txtfile.close()