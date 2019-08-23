from selenium import webdriver
import bs4
from time import sleep
import requests
import json

data_list = []

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
    content = str.find_all(class_='list-item')
    #data_list = []
    for idx, tr in enumerate(content):
        area = tr.select('.details-item .comm-address')[0].string
        price = tr.select('.pro-price .unit-price')[0].string
        arealist = area.split('\xa0\xa0\n')
        area = arealist[1]
        pricelist = price.split('元')
        price = pricelist[0]

        url = 'http://api.map.baidu.com/geocoding/v3/?address=宁波市{}&output=json&ak=ki10ALGLwC9NzO053yjcsu7oU1oyt5GA'.format(area)

        response = requests.get(url)
        lng = json.loads(response.text)['result']['location']['lng']
        lat = json.loads(response.text)['result']['location']['lat']
        loop = 0
        for data in data_list:
            if data['lng'] == lng and data['lat'] == lat :
                he = (data['count'] + int(price.strip()))/2
                data['count'] = he
                loop = 1

        if loop == 0:
            data_list.append({
                'lng': lng,
                'lat': lat,
                'count': int(price.strip())
            })




for i in range(1,21):
    url = 'https://nb.anjuke.com/sale/p{}-t105/#filtersort'
    url = url.format(i)
    listfunction(url)

print(data_list)


# 
# <!DOCTYPE html>
# <html>
# <head>
# <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
# <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
# <script type="text/javascript" src="//api.map.baidu.com/api?v=2.0&ak=您的密钥"></script>
# <script type="text/javascript" src="//api.map.baidu.com/library/Heatmap/2.0/src/Heatmap_min.js"></script>
# <title>热力图功能示例</title>
# <style type="text/css">
# ul,li{list-style: none;margin:0;padding:0;float:left;}
# html{height:100%}
# body{height:100%;margin:0px;padding:0px;font-family:"微软雅黑";}
# #container{height:500px;width:100%;}
# #r-result{width:100%;}
# </style>
# </head>
# <body>
# <div id="container"></div>
# <div id="r-result">
# <input type="button"  onclick="openHeatmap();" value="显示热力图"/><input type="button"  onclick="closeHeatmap();" value="关闭热力图"/>
# </div>
# </body>
# </html>
# <script type="text/javascript">
# var map = new BMap.Map("container");          // 创建地图实例
# 
# var point = new BMap.Point(121.556686,29.880177);
# map.centerAndZoom(point, 12);             // 初始化地图，设置中心点坐标和地图级别
# map.enableScrollWheelZoom(); // 允许滚轮缩放
# 
# var points = ;
# if(!isSupportCanvas()){
# alert('热力图目前只支持有canvas支持的浏览器,您所使用的浏览器不能使用热力图功能~')
# }
# //详细的参数,可以查看heatmap.js的文档 https://github.com/pa7/heatmap.js/blob/master/README.md
# //参数说明如下:
# /* visible 热力图是否显示,默认为true
# * opacity 热力的透明度,1-100
# * radius 势力图的每个点的半径大小
# * gradient  {JSON} 热力图的渐变区间 . gradient如下所示
# *	{
#     .2:'rgb(0, 255, 255)',
#     .5:'rgb(0, 110, 255)',
#     .8:'rgb(100, 0, 255)'
# }
# 其中 key 表示插值的位置, 0~1.
# value 为颜色值.
# */
# heatmapOverlay = new BMapLib.HeatmapOverlay({"radius":20});
# map.addOverlay(heatmapOverlay);
# heatmapOverlay.setDataSet({data:points,max:40000});
# //是否显示热力图
# function openHeatmap(){
#     heatmapOverlay.show();
# }
# function closeHeatmap(){
#     heatmapOverlay.hide();
# }
# closeHeatmap();
# function setGradient(){
#                       /*格式如下所示:
# {
#     0:'rgb(102, 255, 0)',
#     .5:'rgb(255, 170, 0)',
#     1:'rgb(255, 0, 0)'
# }*/
# var gradient = {};
# var colors = document.querySelectorAll("input[type='color']");
# colors = [].slice.call(colors,0);
# colors.forEach(function(ele){
#     gradient[ele.getAttribute("data-key")] = ele.value;
# });
# heatmapOverlay.setOptions({"gradient":gradient});
# }
# //判断浏览区是否支持canvas
# function isSupportCanvas(){
#     var elem = document.createElement('canvas');
# return !!(elem.getContext && elem.getContext('2d'));
# }
# </script>
    