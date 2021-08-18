#!C:\Users\PM BHATIYA\AppData\Local\Programs\Python\Python36\python.exe
print("content-type:text/html")
print()

import cgi
form = cgi.FieldStorage()

email= form.getvalue("email")
psw= form.getvalue("psw")
fname=form.getvalue("usrf")
lname=form.getvalue("usrl")
city=form.getvalue("city")
gender=form.getvalue("gender")
country=form.getvalue("country")

print(email,psw,fname,lname,city,gender,country)
import pymysql
dbq = pymysql.connect(host='localhost',user='root',password='',db='pattern')

cur = dbq.cursor()

sql = "INSERT INTO `ragister` (`fname`, `lname`, `email`, `psw`, `city`, `country`, `gender`) VALUES ('"+fname+"', '"+lname+"', '"+email+"', '"+psw+"', '"+city+"', '"+country+"', '"+gender+"');"
cur.execute(sql)
dbq.commit()
cur.close()
dbq.close()