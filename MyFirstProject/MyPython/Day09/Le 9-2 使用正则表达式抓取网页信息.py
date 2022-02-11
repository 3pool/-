# -*- coding:utf-8 -*-
# 1.抓取百度首页的title
'''
<title>百度一下，你就知道</title>
'''
# 1.1 载入库
import urllib.request
import re
# 1.2 开启页面抓取内容
url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
strHtml = response.read().decode('utf-8')
# print(strHtml) # 调试用
# 1.3 使用正则表达式提取所需要的的内容
pn1 = re.compile(r'<title>(.*?)</title>',re.S)
result1 = re.findall(pn1,strHtml)
print('result1:',result1)
print('title:',result1[0])

print('-'*100)

# 2.提取以下字符串中的城市
strHtml2 = '''
<div class="li">
       <a target="_blank" href="//www.51job.com/beijing/">北京</a>
<a target="_blank" href="//www.51job.com/shanghai/">上海</a>
<a target="_blank" href="//www.51job.com/guangzhou/">广州</a>
<a target="_blank" href="//www.51job.com/shenzhen/">深圳</a>
<a target="_blank" href="//www.51job.com/wuhan/">武汉</a>
<a target="_blank" href="//www.51job.com/xian/">西安</a>
<a target="_blank" href="//www.51job.com/hangzhou/">杭州</a>
<a target="_blank" href="//www.51job.com/nanjing/">南京</a>
<a target="_blank" href="//www.51job.com/chengdu/">成都</a>
<a target="_blank" href="//www.51job.com/chongqing/">重庆</a> 
</div>

'''
# 2.1 构建正则表达式
pn2 = re.compile(r'<a target="_blank" href="//www.51job.com/beijing/">(.*?)</a>',re.S)
pn3 = re.compile(r'<a target="_blank" href="//www.51job.com/.*?/">(.*?)</a>',re.S)
# 正则表达式中，凡是变化的部分都可以用代词进行处理，但只有放在()里的部分会被返回
pn4 = re.compile(r'<a target="_blank" href="//www.51job.com/(.*?)/">(.*?)</a>',re.S)
# 如果一个正则表达式中，有多组()，那么返回的结果会是所有的()中的元素构成的元组，再由这些元组构成列表
pn5 = re.compile(r'<a target="_blank" href="//(.*?)/">(.*?)</a>',re.S)

# 2.2 信息提取
result2 = re.findall(pn2,strHtml2)
result3 = re.findall(pn3,strHtml2)
result4 = re.findall(pn4,strHtml2)
result5 = re.findall(pn5,strHtml2)

# 2.3 输出提取到的信息
print('result2:',result2)
print('result3:',result3)
print('result4:',result4)
print('result5:',result5)

#同时返回城市的链接和城市的名称
'''
[('www.51job.com/beijing','北京')...]
'''
