import json
import pymssql
import pymysql
import time

dbmysql = pymysql.connect("192.168.2.203","greatTao","greatTao.1314","gtcp_app")
cursormy = dbmysql.cursor()

db = pymssql.connect(server='DEVDB.great-tao.com\GTTOWN_DEV',port='1433',database='GtTown',user='sa',password='P@ssw0rd')
cursor = db.cursor()

j = open("facebook.json",encoding='utf-8')
data = json.load(j)

on = "set identity_insert Account on"
cursor.execute(on)

for n in range(0,10):
    '''mssql'''
    sql ="select max(id) from Account"
    cursor.execute(sql)
    results = cursor.fetchone()
    maxId = results[0]
    beginId = maxId+1

    nowstr = time.strftime('%Y%m%d%H%M%S')
    userName = "trade_in"+nowstr+str(n)
    email = nowstr+str(n)+'@egtcp.com'
    sql ="INSERT INTO Account(id,UserName,PasswordHash,AccessFailedCount,TimeZone,Email,Status,origin,accountType,enterpriseType,disabled,activateOrigin,complete,activated,waterArmy) VALUES (%d,%s,%s,%d,%d,%s,%d,%s,%d,%d,%d,%s,%d,%d,%d)"
    cursor.execute(sql,(beginId,userName,'AI+VIirBZoLfJzTPy2tWMTIv39qWkWonlXggqHp5dRSxAep5uuQztYACyiP9C4Fr6g==',0,288000000000,email,9,'trade_in',1,1,0,'trade_in',0,1,1))

    sqlp = "INSERT INTO AccountProfile(AccountId,Country,Avatar,PhoneNumberVisibility,NickName) VALUES (%d,%s,%s,%d,%s)"
    cursor.execute(sqlp,(beginId,'AU',data[n]['avatar'],2,data[n]['nickname']))

    sqlpl1 = "INSERT INTO AccountProfileLocale(AccountId,LocaleId) VALUES (%d,'en')"
    cursor.execute(sqlpl1,(beginId))
    sqlpl2 = "INSERT INTO AccountProfileLocale(AccountId,LocaleId) VALUES (%d,'zh-CN')"
    cursor.execute(sqlpl2,(beginId))

    '''mysql'''
    maxActivityIdsql ="select max(id) from activity"
    cursormy.execute(maxActivityIdsql)
    resultsmysql = cursormy.fetchone()
    maxActivityId = resultsmysql[0]+1

    local = time.localtime(int(data[n]['lasttime']))
    pub_time = time.strftime('%Y-%m-%d %H:%M:%S',local)
    mysqlActivity = "INSERT INTO activity(id,account_id,account_name,account_avatar,content,type,account_auth_status,status,account_country,create_time,jing_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursormy.execute(mysqlActivity,(maxActivityId,beginId,data[n]['nickname'],data[n]['avatar'],data[n]['text'],1,3,1,'AU',pub_time,pub_time))

    mysqlAttachment = "INSERT INTO activity_attachment(account_id,activity_id,url,type) VALUES (%s,%s,%s,%s)"
    imgList = []
    imgData = data[n]['image_list']
    if (len(imgData)>0):
        for m in range(0,len(imgData)):
            imgList.append([maxId,maxActivityId,imgData[m],1])
        cursormy.executemany(mysqlAttachment,imgList)

    db.commit()
    dbmysql.commit()


off = "set identity_insert Account off"
cursor.execute(off)
db.close()
dbmysql.close()