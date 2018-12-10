import pymysql
import json

j = open("facebook.json",encoding='utf-8')
data = json.load(j)
db = pymysql.connect("192.168.2.203","greatTao","greatTao.1314","gtcp_app")
cursor = db.cursor()
# 执行SQL语句
cursor.execute("select * from activity")
# 获取所有记录列表
results = cursor.fetchall()
print(results)
img = data[1]['image_list']
mysqlAttachment = "INSERT INTO activity_attachment(account_id,activity_id,url,type) VALUES (%s,%s,%s,%s);"
l = []
if (len(img)>0):
    for m in range(0,len(img)):
        l .append([1,1,img[m],1])



db.commit()
db.close()


