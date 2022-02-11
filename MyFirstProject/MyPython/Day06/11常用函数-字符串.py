# 转义字符的使用
# 输出带引号的字符串
print("What's your name?")
print('What\'s your name?')
# \'直接识别为单引号而不是字符串的标识
# 输出路径\
print('c:\\n1\\1.csv')
print('c:/n1/1.csv')
# 路径的使用中\/可以互换
print('-'*100)
print('hello'.count('l'))
# 返回l在hello中出现的次数
print('hello'.count('x'))
# 如果没有找到，返回0
# 统计字符串中每个字符出现的次数
str1 = 'Hello world.asdmnfa,sd'
a = []
for char in str1:
    # 遍历字符串中每一个字符
    if char not in a:
        # 不在列表中，说明是首次出现
        print(char,str1.count(char))
        a.append(char)

# 编码和解码
print('-'*100)
str2 = '你好，世界'
bytes2 = str2.encode('utf-8')
# 字符串编码成字节
print(bytes2)
print(bytes2.decode('utf-8'))
print(bytes2.decode('gbk',errors='ignore'))
# 解码时忽略遇到的错误
print('hello')
# 程序一旦遇到异常就会产生中断，后面的代码就无法再执行了
print('-'*100)
# 查找和替换
print('hello'.find('o'))
print('hello'.index('o'))
# 如果找到，返回匹配上的索引位置
print('hello'.find('x'))
# print('hello'.index('x'))
# 如果找不到，find返回-1，index会报错
print('2021-07-10'.replace('-','/'))

print('-'*100)
# 判断字符的类型
print('123'.isdigit())
print('123a'.isnumeric())
# 整数的判断相对容易
print('123.1'.isdigit())
# 判断字符串是否是浮点数
print(isinstance('123.1',float))
print(isinstance(eval('123.1'),float))
# eval是把一个算术运算表达式的字符串转换为运算，并计算出结果
print(eval('3+2'))

print('-'*100)
# 合并和拆分
''' 2021-07-10 '''
print('-'.join(['2021','07','10']))
# 返回的结果是用指定的分隔符把字符串序列中每个子串连接起来之后的长字符串
print('hello world'.split(' '))
# 返回的结果是用指定的分隔符将字符串拆分后的子串构成的列表
strJob = '上海-静安区  |  2年经验  |  本科  |  招2人  |  07-10发布'
# 提取工作城市、工作经验和学历
print(strJob.split('  |  ')[0].split('-')[0]) # 返回城市
print(strJob.split('  |  ')[2]) # 返回学历

print('-'*100)
# 其他常用方法
strSpace = '   hello    wolrd    '
print(strSpace.strip())
# 去掉两边的空格
print(strSpace.replace(' ',''))
# 去除字符串中所有的空格

