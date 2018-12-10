import pymssql

db = pymssql.connect(server='DEVDB.great-tao.com\GTTOWN_DEV',port='1433',database='GtTown',user='sa',password='P@ssw0rd')
cursor = db.cursor()


sql ="select max(id) from Account"
cursor.execute(sql)
results = cursor.fetchone()
print(results[0])

db.close()