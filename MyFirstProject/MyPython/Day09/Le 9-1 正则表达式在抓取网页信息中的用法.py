# -*- coding:utf-8 -*-
import re
# 1.贪婪和非贪婪模式
strHtml = '<ul><li>1234</li><li>2345</li><li>3456</li><li>5678</li></ul>'
# 提取li的信息
pn1 = re.compile(r'<li>.*</li>')
result1 = re.findall(pn1,strHtml)
print('result1:',result1)
print(len(result1))
# 贪婪模式：匹配符合条件的最长子串
# 非贪婪模式：匹配符合条件的最短子串，网页中常用
# 默认是贪婪模式，在量词后面加上？可以改为非贪婪模式
pn2 = re.compile(r'<li>.*?</li>')
result2 = re.findall(pn2,strHtml)
print('result2:',result2)
print(len(result2))

print('-'*100)

# 2.信息的取舍：如何提取需要的信息
# 只返回标签中的文本，不需要标签
pn3 = re.compile(r'<li>(.*?)</li>')
result3 = re.findall(pn3,strHtml)
print('result3:',result3)
print(len(result3))
# 正则表达式中，()的作用是用来设置解析内容的边界，边界之外的信息（标签），只是用来进行定位和匹配，在结果中不会返回

print('-'*100)

# 3.网页中遇到有换行或者不可见字符的情况
strHtml4 = '''
<ul>
    <li>1234</li>
    <li>2345
    </li>   
    <li>3456   
    </li>
    <li>5678</li>
</ul>
'''
pn4 = re.compile(r'<li>(.*?)</li>')
result4 = re.findall(pn4,strHtml4)
print('result4:',result4)
pn5 = re.compile(r'<li>(.*?)</li>',re.S)
result5 = re.findall(pn5,strHtml4)
print('result5:',result5)
# re.S表示.代词可以处理包括换行符\n在内的任意字符串，在网页抓取中非常有用
# 如何解决dotall模式中抓取到的额外的字符（一般都是换行和空格）
print('-'*100)
for item in result5:
    print(item.strip())
    # 方法1：用str.strip()去除两端的空格和不可见字符
    print(re.sub(r'\s+','',item))
    # 方法2：用re.sub将字符串中的不可见字符替换为空字符串，但要注意要抓取的内容中是否有空格