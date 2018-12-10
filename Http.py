import requests
import bs4

#要抓取的目标页码地址
url = 'http://gw-api.pinduoduo.com/api/router?type=pdd.order.information.get&order_sn=180820-069827298471542'

#抓取页码内容，返回响应对象
response = requests.post(url,data = {'type':'pdd.order.information.get','order_sn':'180820-069827298471542'})

#查看响应状态码
status_code = response.status_code


#使用BeautifulSoup解析代码,并锁定页码指定标签内容
# content = bs4.BeautifulSoup(response.content.decode("utf-8"), "lxml")
#form = content.find_all(id='fm1')

print(status_code)
print(response.text)