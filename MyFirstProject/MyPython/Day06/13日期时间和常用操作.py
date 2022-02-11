# time
import time
# 1.获取当前时间
print(time.time())
# 返回当前时间点到1970年1月1日0时0分0秒的时间长度
print(time.localtime())
# 返回当前时间 ，结果是一个结构体时间
# 2.时间和字符串的转换
print(time.asctime(time.localtime()))
# 返回当前时间对应的字符串
print(type(time.asctime(time.localtime())))
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
# 转换为自定义格式的字符串
print(time.strptime('2021/07/10','%Y/%m/%d'))
# 把字符串转换为结构体时间
# 3.暂停
time.sleep(2) # 暂停程序执行2秒
print('结束')


print('-'*100)
# datetime
import datetime
# 1.获得当前的日期时间
print(datetime.datetime.now())
# 返回的结果是一个日期时间对象
print(type(datetime.datetime.now()))
date1 = datetime.datetime.now()
print(date1.year)
print(date1.month)
print(date1.day)
print(type(date1.year))
print(date1.weekday())
# 返回当前是周几，从周一开始计算，周一对应0
print(date1.isoweekday())
# 返回当前是周几，从周一开始计算，周一对应1