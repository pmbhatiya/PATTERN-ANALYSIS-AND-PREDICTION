#!C:\Users\PM BHATIYA\AppData\Local\Programs\Python\Python36\python.exe
print("content-type:text/html")
print()
import urllib3
from bs4 import BeautifulSoup
print("hiii pm")from bs4 import BeautifulSoup
import datetime
from tinydb import TinyDB, Query
import urllib3
import xlsxwriter

http = urllib3.PoolManager()

url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=TCS'
response = http.request('GET', url)
soup = BeautifulSoup(response.data,'lxml')
print(soup.text)
#soup = BeautifulSoup(response.data)
#soup = BeautifulSoup(response.content, "html.parser")
#soup = BeautifulSoup(response.data.decode('utf-8'))
#soup = BeautifulSoup(response.content, "html.parser")

#events = soup.find('ul', {'class': 'stock'}).findAll('span').text
#events = soup.find('ul').findAll('li')
#e2=soup.select('ul li span')
#print(soup.companyName').text)
#e2=soup.select('companyName').text
#print(soup.text)
