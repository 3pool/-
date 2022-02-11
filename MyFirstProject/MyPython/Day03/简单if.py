# -*- coding:utf-8 -*-
# if-elif-else语句，可以针对多种情况进行处理
# 输入成绩，如果成绩>=90，输出优秀，成绩>=80，输出良好，成绩>=60，输出及格，否则输出不及格
score = float(input('请输入成绩：'))
if score >= 90 :
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 60:
    print('及格')
else :
    print('不及格')
print('-'*100)
if score >= 80 :
    print('良好')
elif score >= 60:
    print('及格')
elif score >= 90:
    print('优秀')
else :
    print('不及格')
# if-elif-else结构中，只要某个条件成立，执行完该条件对应的语句后，if结构就结束了，上面的代码问题在于，条件1包含了条件3的内容，因此要注意，在书写if-elif-else的结构中，每个条件要保持互斥的关系，不能有包含的情况
print('-'*100)
if score >= 80 and score < 90:
    print('良好')
elif score >= 60 and score < 80:
    print('及格')
elif score >= 90:
    print('优秀')
else :
    print('不及格')
