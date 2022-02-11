# 载入库
from selenium import webdriver
import time


# 各城市在携程网对应的代码字典
cityDict = {'北京':'1','上海':'2','广州':'32','深圳':'30','成都':'28','重庆':'4','杭州':'17','武汉':'477','西安':'10',
            '郑州':'559','青岛':'7','长沙':'206','天津':'3','苏州':'14','南京':'12','东莞':'223','沈阳':'451','合肥':'278',
            '佛山':'251','昆明':'34','福州':'258','无锡':'13','厦门':'25','哈尔滨':'5','长春':'158','南昌':'376','济南':'144',
            '大连':'6','贵阳':'38','温州':'491','石家庄':'428','泉州':'406','南宁':'380','金华':'308','常州':'213','珠海':'31',
            '惠州':'299','嘉兴':'571','南通':'82','中山':'553','保定':'185','兰州':'100','台州':'578','徐州':'512','太原':'105',
            '绍兴':'22','烟台':'533','廊坊':'340'}

# 抓取单个城市旅游产品目录页page页面
def get_single_page(cityno):
    # 获取浏览器并打开页面
    browser = webdriver.Chrome()
    url = 'https://vacations.ctrip.com/list/grouptravel/sc'+cityno+'.html?s=2&st=北疆&startcity='+cityno+'&sv=北疆&filter=dc1'
    browser.set_window_size(600, 800)
    browser.get(url)
    time.sleep(10)
    # 点击搜索按钮，以保证数据的准确性
    submitButtonS = browser.find_element_by_xpath('//*[@id="search-box-container"]/div[2]/a')
    submitButtonS.click()
    time.sleep(10)
    submitButtonF = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[6]/div/div[1]/span[2]')
    submitButtonF.click()
    time.sleep(10)
    for pageno in range(3):
        # 获取包含所有信息的div
        response = browser.page_source
        filename = 'pages/' + str(cityno) + '-' + str(pageno+1) + '.txt'
        with open(filename, 'w', encoding='utf-8') as fn:
            fn.write(response)
        if pageno > 1:
            break
        else:
            Page2 = browser.find_element_by_class_name('down')
            Page2.click()
        time.sleep(10)
    browser.close()
    time.sleep(10)

# 遍历城市代码字典，获取所有城市的page页面
def get_all_page():
    for cityname in cityDict:
        get_single_page(cityDict[cityname])

# 调用函数，获取最终信息并写入本地txt文件
get_all_page()


