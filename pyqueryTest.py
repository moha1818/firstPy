from pyquery import PyQuery as pq

doc = pq('http://sports.sina.com.cn/nba/',encoding='utf-8')

print(doc('.news-list-a ul li a:contains("詹姆斯")').text())