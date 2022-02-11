# -*- coding:utf-8 -*-
# 利用函数对一组数字求和
# 使用容器对象实现
def AddList(x):
    total = 0
    # 和
    for item in x:
        total += item
    print(total)

AddList([1,2,3])
AddList((1,2,3,4))
# 传入的参数必须用容器对象进行包装（列表元组）
# AddList(1,2,3)
# 报错，因为AddList只有一个参数
print('-'*100)
# 利用不定长参数实现
# 1.*args
def AddItem(*additem):
    # 定义一个不定长参数
    total = 0
    # 和
    print(additem)
    # 函数中调用不定长参数时，不需要加*
    print(type(additem))
    for item in additem:
        total += item
    print(total)

AddItem(1,2,3)
# 调用有不定长参数的函数时，所有传入的不定长参数*additem实质上是在函数中生成了一个元组，函数是在对元组进行操作
AddItem(1,2,3,4,5)
print('-'*100)
# 2.字典类型的不定长参数 **kwargs
def funcDictArgs(**kwargs):
    print(kwargs)
    print(type(kwargs))

# funcDictArgs(1,2,3,4)
# 不能用默认的参数传递方式，必须用关键字调用的方式进行传递
funcDictArgs(a=1,b=2,c=3,d=[1,2,3])
# 使用关键字调用处理**kwargs的时候，传入的所有参数会形成一个字典，关键字调用表达式的关键字成为字典的键，值成为字典的值
print('-'*100)
# 3.在函数中同时使用两种不定长参数
def funcTwoArgs(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)

funcTwoArgs('张三',1,2,3,4,'hello',a=123,b='hello1')
# 使用非关键字调用的参数会传递到args中，使用关键字调用的参数会传递到kwargs中，两者的顺序不能交叉
# funcTwoArgs('张三',1,2,3,a=1,b=2,234,'hello',c=111)