#!C:\Users\PM BHATIYA\AppData\Local\Programs\Python\Python36\python.exe
print("content-type:text/html")
print()

import cgi
form = cgi.FieldStorage()

email= form.getvalue("usr")
psw= form.getvalue("psw")

import pymysql

dbq = pymysql.connect(host='localhost',user='root',password='',db='pattern')

cur = dbq.cursor()

sql = "select *  from `ragister` where `email`='"+email+"' AND `psw`='"+psw+"'"
row=cur.execute(sql)
if(row>0):
	print("Login succssfully")
else:
	print("Invalid Login Detail")
#for result in fetchrow(sql):
#	print(result)
#dbq.commit()
cur.close()
dbq.close()