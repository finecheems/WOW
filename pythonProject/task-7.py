import time
import requests
from lxml import etree
while True:
    url = 'https://www.jin10.com'
    html = requests.get(url)
    content_xpath = '//*[@class="right-content"]/div/text()'
    pages = etree.HTML(html.content)
    t_0 = pages.xpath(content_xpath)
    for i in t_0:
        find1 = "乌克兰"
        if (find1 in i)==True:
            print(i)
            url_1 = 'https://sctapi.ftqq.com/SCT179523TRF3JV8Wmtf78s62sT6JE6SwS.send'
            requests.post(url_1, data={'text': "出现乌克兰新闻", 'desp': i})
            continue
    time.sleep(300)#每五分钟进行一次查看