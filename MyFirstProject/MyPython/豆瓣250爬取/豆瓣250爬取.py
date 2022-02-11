import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
import  time
import numpy as np

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
        'User-Agent' : np.random.choice(agent)
    }
    return random_headers

def get_html(url):
    res = requests.get(url,headers = random_RH(),stream = True)
    res.encoding = 'utf-8'
    return res

def get_one_page(url):
    res =get_html(url)
    soup = bs(res.text , 'html.parser')
    divs = soup.find_all(class_='hd')
    hrefs = [each.a['href'] for each in divs]
    return hrefs

href_data = []
for i in range(10):
    url = f'https://movie.douban.com/top250?start={i*25}&filter='
    hrefs = get_one_page(url)
    href_data+=hrefs

pd.Series(href_data).to_csv('hrefs.csv', mode='a', index=False ,header=False)

def get_detail_page(url):
    data = []
    res = get_html(url)
    soup = bs(res.text, 'html.parser')

    try:
        content_div = soup.find('div', id='content')
    except:
        content_div = ''

    try:
        name = content_div.find('span', property='v:itemreviewed').string.split(' ')[0]
    except:
        name = ''

    try:
        director = content_div.find('a', rel='v:directedBy').string
    except:
        director = ''

    try:
        scriptwriter = content_div.find_all('span', class_='attrs')[1].text.replace(' ', '')
    except:
        scriptwriter = ''

    try:
        actors = content_div.find_all('span', class_='attrs')[2].text.replace(' ', '')
    except:
        actors = ''

    try:
        kind_span = soup.find_all('span', property='v:genre')
        kind_tmp = ''
        for i in range(len(kind_span)):
            kind_tmp += kind_span[i].text + '/'
        kind = kind_tmp[:-1]
    except:
        kind = ''

    try:
        pn_country = re.compile(r'<span class="pl">制片国家/地区:</span> (.*?)<br/>', re.S)
        country = re.findall(pn_country, str(content_div))[0].replace(' ', '')
    except:
        country = ''

    try:
        pn_languege = re.compile(r'<span class="pl">语言:</span> (.*?)<br/>', re.S)
        languege = re.findall(pn_languege, str(content_div))[0]
    except:
        languege = ''

    try:
        releasedate_span = soup.find_all('span', property='v:initialReleaseDate')
        releasedate_tmp = ''
        for i in range(len(releasedate_span)):
            releasedate_tmp += releasedate_span[i].text + '/'
        releasedate = releasedate_tmp[:-1]
    except:
        releasedate = ''

    try:
        runtime = soup.find('span', property='v:runtime').string
    except:
        runtime = ''

    try:
        rating_num = soup.find('strong', class_='ll rating_num').string
    except:
        rating_num = ''

    try:
        rating_people = soup.find('span', property='v:votes').string
    except:
        rating_people = ''

    try:
        tag_div = soup.find('div', class_='tags-body')
        tag_a = tag_div.find_all('a')
        tag_tmp = ''
        for i in range(len(tag_a)):
            tag_tmp += tag_a[i].text + '/'
        tags = tag_tmp[:-1]
    except:
        tags = ''

    data = [name, director, scriptwriter, actors, kind, country, languege, releasedate, runtime, rating_num,
            rating_people, tags]
    return data


def main(start, end):
    df = pd.DataFrame(columns=['电影名称', '导演', '编剧', '演员', '类型', '国家', '语言', '上映日期', '时长', '评分', '评论人数', '标签'])
    for index in range(start, end + 1):
        time.sleep(np.random.uniform(30, 60))
        print(f'正在抓取第{index}部电影的数据')
        url = href_data[index-1]
        data = get_detail_page(url)
        df.loc[index-1] = data
    df.to_csv('豆瓣top50-100.csv', mode='a',index=False ,header=False)
    print('抓取结束')

main(51,100)