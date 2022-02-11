# 载入库
import re
import requests
from bs4 import BeautifulSoup as bs
import xlwt

# 获取网站HTML数据并存储在本地TXT文件中
def get_page(pageno):
    # 构建请求头
    myHeaders = {
        'Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    # 新建本地TXT文件并将获取到的HTML数据写入文件中
    with open('TOP250影片信息汇总.txt','w',encoding='utf-8') as page:
        # 根据每个页面的URL规律，利用循环实现翻页效果，每翻一页，就往文件里写一页
        for pagen in range(0, pageno * 25, 25):
            url = 'https://movie.douban.com/top250?start=' + str(pagen) + '&filter='
            response = requests.get(url, headers=myHeaders)
            response.encoding = 'utf-8'
            page.write(response.text)

# 创建用于存储影片基本信息的列表，方便获取到影片信息后进行存储
# 存储影片排名的列表
MovieNos = []
# 存储影片名称的列表
MovieNames = []
# 存储影片评分的列表
MovieRatings = []
# 存储影片评价人数的列表
MovieVotes = []
# 存储影片一句话短评的列表
MovieInqs = []

# 从本地TXT文件中获取影片的基本信息
def get_movieinfo():
    # 读取文件并创建soup对象
    with open('TOP250影片信息汇总.txt','r',encoding='utf-8') as MovieHtml:
        movie_soup = bs(MovieHtml,'html.parser')
        # 利用em标签读取影片排名信息，写入影片排名列表
        NoTags = movie_soup.find_all('em')
        for NoTag in NoTags:
            MovieNos.append(NoTag.string)
        # 利用span标签和class属性读取影片评分信息，写入影片评分列表
        RatingTags = movie_soup.find_all('span',class_ = 'rating_num')
        for RatingTag in RatingTags:
            MovieRatings.append(RatingTag.string)
        # 利用模糊匹配和正则表达式读取影片评价人数信息，写入影片评价人数列表
        VoteTags = movie_soup.find_all('div', class_='star')
        for VoteTag in VoteTags:
            MovieVotetmp = str(VoteTag.find_all('span',text = re.compile(r'.*?人评价'))[0])
            Votepn = re.compile(r'<span>(.*?)人评价</span>')
            MovieVote = re.findall(Votepn,MovieVotetmp)[0]
            MovieVotes.append(MovieVote)
        # 利用正则表达式获取一句话短评信息，写入一句话短评列表（利用判断语句处理短评为空的情况，当短评为空时，写入空格即可）
        DivTags = movie_soup.find_all('div', class_ = 'info')
        for DivTag in DivTags:
            Inqpn = re.compile(r'<span class="inq">(.*?)</span>')
            InqTags = re.findall(Inqpn,str(DivTag))
            if InqTags == []:
                MovieInqs.append(' ')
            else:
                MovieInqs.append(InqTags[0])
    # 利用正则表达式获取影片名称信息，写入影片名称列表
    with open('TOP250影片信息汇总.txt','r',encoding='utf-8') as MovieHtml2:
        page = MovieHtml2.read()
        pnLi = re.compile(r'<li>(.*?)</li>', re.S)
        reLi = re.findall(pnLi, page)
        for tagLi in reLi:
            pnName = re.compile(r'<img width="100" alt="(.*?)".*?>')
            MovieName = re.findall(pnName, tagLi)[0]
            MovieNames.append(MovieName)

# 利用xlwt将获取到的影片信息列表中的内容写入xls文件中
def savxlsx():
    # 创建对象并设定编码格式
    myBook = xlwt.Workbook(encoding='utf-8')
    # 新建工作表
    mySheet = myBook.add_sheet('TOP250影片信息汇总')
    # 写入标题
    mySheet.write(0, 0, '影片排名')
    mySheet.write(0, 1, '影片名称')
    mySheet.write(0, 2, '影片评分')
    mySheet.write(0, 3, '评论人数')
    mySheet.write(0, 4, '一句话短评')
    # 写入影片排名
    for norow in range(250):
        mySheet.write(norow+1,0,MovieNos[norow])
    # 写入影片名称
    for namerow in range(250):
        mySheet.write(namerow+1,1,MovieNames[namerow])
    # 写入影片评分
    for ratingrow in range(250):
        mySheet.write(ratingrow+1,2,MovieRatings[ratingrow])
    # 写入影片评价人数
    for voterow in range(250):
        mySheet.write(voterow+1,3,MovieVotes[voterow])
    # 写入影片一句话短评
    for inqrow in range(250):
        mySheet.write(inqrow+1,4,MovieInqs[inqrow])
    # 保存表格
    myBook.save('TOP250影片信息汇总.xls')

# 调用函数并执行
get_page(10)
get_movieinfo()
savxlsx()

