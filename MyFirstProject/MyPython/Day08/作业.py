import re
# 1、判断字符串是否符合111-1111-1111的形式（电话号码），如：str1="131-1098-4757"，判断结果为True
str1 = "131-1098-4757"
pn1 = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
result = re.match(pn1,str1)
if result:
    print('该字符串是电话号码')
else:
    print('该字符串不是电话号码')


# 2、找出字符串中符合电话号码格式的子字符串，如：str2=”alskdjlaksdjf111-1111-1111dskljfsda”，能返回111-1111-1111
str2="alskdjlaksdjf111-1111-1111dskljfsda"
pn1 = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
result = re.findall(pn1,str1)
print(result[0])