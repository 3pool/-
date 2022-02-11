# -*- coding:utf-8 -*-
# 引入库
import easygui
a = easygui.enterbox('请输入第一个数字')
print(a)
print(type(a))
# enterbox返回的是字符串
b = int(easygui.enterbox('请输入第二个数字'))
c = int(a) # 把a转换为整数
# 使用easygui进行输出
easygui.msgbox(b+c,b-c)
# easygui.msgbox只能输出一个字符串，当需要输出多行内容时，要自己构建出一个完整的字符串
result = '%d+%d=%d'%(b,c,b+c)+'\n'+'%d-%d=%d'%(b,c,b-c)+'\n'+'%d*%d=%d'%(b,c,b*c)+'\n'+'%d/%d=%d'%(b,c,b/c)
# 格式化字符串并不是只能在print中使用，它实际上是一种对字符串的处理方法，'\n'代表的是换行
easygui.msgbox(result)