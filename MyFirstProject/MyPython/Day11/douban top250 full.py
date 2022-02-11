# -*- coding:utf-8 -*-
# 抓取豆瓣电影top250每部影片的详细信息
'''
思路：
1.抓取影片的目录和目录对应的链接
1.1 处理目录页的翻页：用循环结合url实现
1.2 抓取目录页的内容：requests
1.3 将对应的目录页写入本地文件
1.4 从文件中提取详情页的链接
2.将抓取到的目录和链接写入磁盘文件
3.读取文件获得链接
4.利用链接进入详情页，抓取页面内容，并写入本地文件
5.读取详情页文件，从中提取需要的信息
6.把抓取到的信息写入表格
'''

# 0.预备工作
# 0.1 载入库
import requests
import re
from bs4 import BeautifulSoup as bs
import xlrd
import xlwt
import os
import random

# 0.2 全局设置
linklist = []
# 存放详情页的链接
datalist = []
# 存放影片的所有信息

# 1.抓取影片的目录和目录对应的链接
# 1.1 处理目录页的翻页：用循环结合url实现
'''
https://movie.douban.com/top250?start=0&filter=
https://movie.douban.com/top250?start=25&filter=
https://movie.douban.com/top250?start=50&filter=
'''

# 1.2 抓取目录页的内容：requests
def get_index(pageno):
    # pageno是目录页的页码
    for i in range(0,pageno*25,25):
        # 构建翻页的url
        url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
        # print(url)  # 调试用
        print('正在抓取第',str(i//25+1),'页目录，请稍后...')
        # 抓取目录页内容
        response = requests.get(url,headers = {'User-Agent':'Mozilla / 5.0'})
        response.encoding = 'utf-8'
        # print(response.text)    # 调试用

        # 1.3 将对应的目录页写入本地文件
        # 构建一个用来存放目录页的文件夹
        os.makedirs('top250menu',exist_ok=True)
        # 构建用来写入的文件名，注意文件名中要包含路径
        filename = 'top250menu/index' + str(i//25+1) + '.txt'
        # 将抓取到的页面写入文件
        with open(filename,'w',encoding='utf-8') as tfp:
            tfp.write(response.text)

# 1.4 从文件中提取详情页的链接
def get_links():
    # 抓取链接
    # 文件的读取
    for i in range(1,11):
        # i 是目录页的编码
        # 构建读取的文件名
        filename = 'top250menu/index' + str(i) + '.txt'
        # print(filename)     # 调试用
        # 读取文件
        with open(filename,'r',encoding='utf-8') as tpf:
            # 将读取出来的文件内容转换成BeautifulSoup对象，方便进行链接的提取
            soupIndex = bs(tpf.read(),'html.parser')
            # print(soupIndex)    # 调试用
            # 找出包含所有影片的ol标签
            tagOl = soupIndex.find('ol',class_='grid_view')
            # 找出所有影片对应的li标签
            tagLi = tagOl.find_all('li')
            for tagMovie in tagLi:
                # 遍历每部影片，抓取影片排名、影片名称、影片对应详情页链接
                MovieRank = tagMovie.em.string
                print('影片排名：',MovieRank)
                MovieName = tagMovie.img['alt']
                # 影片名称是li标签中第一个img标签对应的alt属性的值
                print('影片名称：',MovieName)
                MovieLink = tagMovie.a['href']
                # 影片详情页链接是li标签中第一个a标签对应的href属性的值
                print('影片链接：',MovieLink)
                print('-'*100)
                # 将排名、名称和链接添加到linklist中，方便后续写入本地文件
                linklist.append((MovieRank,MovieName,MovieLink))

# 2.将抓取到的目录和链接写入磁盘文件
def save_menu():
    myBook = xlwt.Workbook(encoding='utf-8')
    # 创建工作簿
    mySheet = myBook.add_sheet('目录信息')
    # 创建工作表

    # 写表头
    title = ('影片排名','影片名称','影片链接')
    for iCol in range(len(title)):
        # 用索引遍历列表
        mySheet.write(0,iCol,title[iCol])
        # 在第一行指定的列写入title中对应的信息，注意，iCol既是列索引也是列表索引

    # 写数据
    for iRow in range(len(linklist)):
        # 外层循环处理行，行数就是linklist中的元素数量（影片数量）
        for iCol in range(len(linklist[iRow])):
            # 内层循环处理列，列数由每部影片的特征数量决定
            mySheet.write(iRow+1,iCol,linklist[iRow][iCol])
            # 在指定的位置写入对应的内容

    # 将工作簿写入磁盘文件
    myBook.save('目录信息.xls')

# 3.读取文件获得链接
def read_links_from_file():
    # 开启xls文件，获取链接
    linkBook = xlrd.open_workbook('目录信息.xls')
    # print(linkBook)     # 调试用
    linkSheet = linkBook.sheets()[0]
    # 先返回所有工作表的集合，再用索引返回指定的表
    # print(linkSheet)    # 调试用
    # print(linkSheet.col_values(0))
    # 返回指定的列，0是列的索引
    ranks = linkSheet.col_values(0)[1:]
    # 返回第一列，用切片去掉表头，返回全部的排名
    names = linkSheet.col_values(1)[1:]
    # 电影名称
    links = linkSheet.col_values(2)[1:]
    # 电影的链接
    # print(ranks,names,links)    # 调试用
    return ranks,names,links

# 构建随机的请求头
def random_RH():
    agent = [
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
        'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
        'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
    ]
    random_headers = {
        'Connection' : 'keep-alive',
        'User-Agent' : random.choice(agent)
    }
    return random_headers

# 4.利用链接进入详情页，抓取页面内容，并写入本地文件
def get_full_page():
    MovieRank,MovieName,MovieLink = read_links_from_file()
    # print(MovieLink)  # 调试用
    # 构建一个文件夹，用来存放影片详情页
    os.makedirs('top250full',exist_ok=True)
    for i in range(0,10):
        # 为了避免被豆瓣封IP，一次不宜抓取过多的详情页
        response = requests.get(MovieLink[i],headers = random_RH())
        response.encoding = 'utf-8'
        # print(response.text)    # 调试用
        filename = 'top250full/' + str(MovieRank[i]) + '_' + str(MovieName[i]) + '.txt'
        # print(filename)   # 调试用
        with open(filename,'w',encoding='utf-8') as tpf:
            tpf.write(response.text)

# 5.读取详情页文件，从中提取需要的信息
def get_fulldata():
    # 5.1 获取所有要抓取内容的影片文件名：用os.walk遍历指定的文件夹
    for root,dirs,files in os.walk('top250full'):
        # 获取文件夹对应的根目录、子目录和目录中的文件名，其中files对应的目录中的文件名列表
        pass
    # print(files)    #  调试用
    # print(len(files))   # 调试用
    # 5.2 开启影片对应的文本文件
    for MovieFile in files:
        # 遍历影片文件的列表，测试的时候先取一部分进行，测试完毕再抓取所有的文件内容
        with open('top250full/' + MovieFile,'r',encoding='utf-8') as mf:
            page = mf.read()
            # 获得页面内容
            # print(type(page))   # 调试用
            MovieSoup = bs(page,'html.parser')
            # 转成soup对象
            # print(MovieSoup)    # 调试用
            # 5.3 抓取数据
            # 5.3.1 找出包含影片所有信息的div标签
            try:
                MovieContent = MovieSoup.find('div', id = 'content')
            except:
                MovieContent = ''
            # print(MovieContent)     # t调试用
            # 5.3.2 电影排名
            try:
                MovieRank = MovieContent.find('span', class_='top250-no').string[3:]
            except:
                MovieRank = ''
            print('影片排名：',MovieRank)

            # 5.3.3 电影名称
            try:
                MovieName = MovieContent.find('span', property='v:itemreviewed').string
                MovieName1 = MovieContent.find('span', property='v:itemreviewed').string.split(' ')[0]
            except:
                MovieName = ''
            print('影片名称：',MovieName1)

            # 5.3.4 上映年份
            try:
                MovieYear = MovieContent.find('span', class_='year').string[1:-1]
                # 用切片去掉首尾的空格
            except:
                MovieYear = ''
            print('上映年份：',MovieYear)

            # 5.3.5 演职人员
            MovieInfo = MovieContent.find('div', id='info')
            # 先找到包含从导演到IMDB信息的所有内容的div标签，再提取演职人员信息
            MovieAttrs = MovieInfo.find_all('span',class_='attrs')
            # 包含导演、编剧和演员的span标签
            # print(MovieAttrs)     # 调试用
            # print(len(MovieAttrs))     # 调试用
            # print(MovieAttrs[2])   # 调试用
            # 5.3.5.1 导演
            try:
                MovieDirector = MovieAttrs[0].string
                MovieDirector1 = MovieAttrs[0].text
            except:
                MovieDirector = ''
                MovieDirector1 = ''
            print('导演：',MovieDirector1)

            # 5.3.5.2 编剧
            try:
                MovieScript = MovieAttrs[1].string
                MovieScript1 = MovieAttrs[1].text
                # text是返回标签内所有的文本，当标签内有其他标签时，用text优于string
            except:
                MovieScript = ''
                MovieScript1 = ''
            print('编剧：',MovieScript1)

            # 5.3.5.3 演员
            try:
                MovieActor = MovieAttrs[2].text
                # text是返回标签内所有的文本，当标签内有其他标签时，用text优于string
            except:
                MovieActor = ''
            print('演员：',MovieActor)

            # 5.3.6 影片类型
            try:
                MovieTypes = MovieInfo.find_all('span', property='v:genre')
                # print(MovieTypes)   # 调试用
                MovieType = ''
                for item in MovieTypes:
                    # 遍历类型中所有的span标签
                    MovieType += ' / ' + item.string
                MovieType = MovieType[3:]
                # 切掉前面多余的分隔符
            except:
                MovieType = ''
            print('影片类型：',MovieType)

            # 5.3.7 国家、地区 用正则表达式抓取
            try:
                pnCA = re.compile(r'<span class="pl">制片国家/地区:</span> (.*?)<br/>',re.S)
                MovieArea = re.findall(pnCA,str(MovieInfo))[0]
                # 正则表达式只能针对字符串或字节进行搜索，所以要把tag对象转换为字符串
            except:
                MovieArea = ''
            print('国家/地区：',MovieArea)

            # 5.3.8 语言
            # 因为语言没有特定的唯一的标签进行定位，所以先找info的文本，再设法提取片长
            try:
                TextInfo = MovieInfo.text
                # print(TextInfo)
                MovieLanguage = TextInfo.split('语言: ')[1].split('上映日期:')[0].strip()
                # 找前面后面的分隔符，用 split进行分割提取，再去掉两端的不可见字符
            except:
                MovieLanguage = ''
            print('语言：',MovieLanguage)

            # 5.3.9 片长
            # 因为语言没有特定的唯一的标签进行定位，所以先找info的文本，再设法提取片长
            try:
                TextInfo = MovieInfo.text
                # print(TextInfo)
                MovieLong = TextInfo.split('片长: ')[1].split('又名:')[0].strip()
                # 找前面后面的分隔符，用 split进行分割提取，再去掉两端的不可见字符
            except:
                MovieLong = ''
            print('片长：', MovieLong)

            # 5.3.10 评分
            try:
                MovieRating = MovieContent.find('strong', class_='ll rating_num').string
            except:
                MovieRating = ''
            print('评分：',MovieRating)

            # 5.3.11 评论人数
            try:
                MovieVP = MovieContent.find('span', property='v:votes').string
            except:
                MovieVP = ''
            print('评论人数：',MovieVP)

            # 5.3.12 简介
            try:
                MovieSummary = re.sub(r'\s{2,}','\n    ',MovieContent.find('span', property='v:summary').text.strip())
            except:
                MovieSummary = ''
            print('影片简介：',MovieSummary)

            # 5.3.13 tags
            try:
                MovieTags = re.sub(r'\s+',' / ',MovieContent.find('div', class_='tags-body').text.strip())
            except:
                MovieTags = ''
            print('影片标签：',MovieTags)
            print('-'*100)

            # 5.4 将抓取到的信息添加到datalist中
            datalist.append((MovieRank,MovieName1,MovieYear,MovieDirector1,MovieScript1,MovieActor,MovieType,MovieArea,MovieLanguage,MovieLong,MovieRating,MovieVP,MovieSummary,MovieTags))

# 6.把抓取到的信息写入表格
def save_fulldata():
    fBook = xlwt.Workbook(encoding='utf-8')
    # 创建工作簿
    fSheet = fBook.add_sheet('top250full')
    # 创建工作表

    # 写表头
    title = ('影片排名','影片名称','上映年份','导演','编剧','演员','影片类型','国家/地区','语言','片长','评分','评论人数','影片简介','影片标签')
    for iCol in range(len(title)):
        # 遍历title序列的索引（同时也是列的索引）
        fSheet.write(0,iCol,title[iCol])
        # 在第一行指定的列写入对应的标题信息

    # 写数据
    for iRow in range(len(datalist)):
        # 外层循环处理行，行数是datalist的元素数量（影片数量）
        for iCol in range(len(datalist[iRow])):
            # 内层循环处理列，列数是每部影片的指标（字段）数
            fSheet.write(iRow+1,iCol,datalist[iRow][iCol])
            # 在指定的位置写入对应的内容

    fBook.save('top250full.xls')


# 测试函数
# get_index(10)   # 1.抓取目录页，写入本地文件
# get_links()     # 抓取目录页的链接和其他信息
# save_menu()     # 将目录页信息和链接写入本地文件
# get_full_page()     # 抓取详情页，写入文件
get_fulldata()
save_fulldata()
