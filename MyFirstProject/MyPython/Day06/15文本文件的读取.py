# 开启文件，准备进行读取
with open('123.txt','r') as fp:
    # 以只读模式开启123.txt并赋予fp对象
    # 读取文件内容,返回结果是字符串
    print(fp.read())

with open('123.txt','r') as fp1:
    # print(fp1.readlines())  读取文件内容,返回结果是所有行构成的序列
    for line in fp1.readlines():
        print(line,end='')