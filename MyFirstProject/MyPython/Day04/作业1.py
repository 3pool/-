s = input('请输入要统计字符的字符串：')
d={}
for i in s:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]=d[i]+1
for j in d.keys():
    print(j,d[j])