# -*- coding:utf-8 -*-
# 嵌套的if结构，用来处理更加复杂的情况
# 输入成绩，首先判断成绩是否有效[0-100]为有效，在有效的前提下，如果成绩>=90，输出优秀，成绩>=80，输出良好，成绩>=60，输出及格，否则输出不及格，如果成绩无效，给出对应的提示
score = float(input('请输入成绩：'))
if score >=0 and score <= 100:
    # 判断成绩是否有效
    if score >= 90 :
        print('优秀')
    elif score >= 80:
        print('良好')
    elif score >= 60:
        print('及格')
    else :
        print('不及格')
else:
    print('成绩无效，请查证后输入')