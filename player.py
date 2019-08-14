from selenium import webdriver
import bs4
from time import sleep


def player(url):
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    sleep(2)
    htmlstr=driver.page_source
    driver.quit()
    return htmlstr

def listfunction(url):
    str=player(url)
    str=bs4.BeautifulSoup(str,"lxml")
    content = str.find_all(class_='show')

    title = str.select('.players thead tr td')

    ballteam = str.select('.current span')[0].string

    list=[]
    for idx, ti in enumerate(title):
        if idx != 0:
            list.append(ti.text)


    data_list = []
    data = {}
    for idx, tr in enumerate(content):
        tds = tr.find_all('td')
        data_list.append({
            '头像': tds[0].find('img')['src'],
            list[0]: tds[1].find('a').text,
            list[1]: tds[2].find('a').text,
            list[2]: tds[3].text,
            list[3]: tds[4].text,
            list[4]: tds[5].text,
            list[5]: tds[6].text,
            list[6]: tds[7].text,
            list[7]: tds[8].text
        })
        if len(content) == idx+1:
            data = {
                'team':ballteam,
                'playerCount':idx+1,
                'data':data_list
            }
    print(data)




for i in range(30):
    url = 'http://nba.stats.qq.com/player/list.htm#teamId='
    url = url + str(i+1)
    listfunction(url)
    
    