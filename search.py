#!C:\Users\PM BHATIYA\AppData\Local\Programs\Python\Python36\python.exe
print('content-type:text/html')
print()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numpy as np
import pandas as pd
import os
import cgi
form = cgi.FieldStorage()

cn= form.getvalue("search");
cn.upper();
CHROMEDRIVER_PATH = 'C:\webd\chromedriver.exe'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
#chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

chrome_options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\xampp\htdocs\Pattern\csv",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
#chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                         )
driver.get('https://nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+cn)

name = driver.find_element_by_css_selector('#companyName').text;
symbol = driver.find_element_by_css_selector('#symbol').text;
address = driver.find_element_by_css_selector('#isinCode').text;


#chrome_options.binary_location = CHROME_PATH
driver.get('https://www.nseindia.com/products/content/equities/equities/eq_security.htm')

sy = driver.find_element_by_xpath('//*[@id="symbol"]')
sy.send_keys(cn)

se = driver.find_element_by_id('series')
se.send_keys('EQ')

day= driver.find_element_by_id('dateRange')
day.send_keys('365 Days')

bt= driver.find_element_by_xpath('//*[@id="get"]')
bt.click()
time=10
try:
    WebDriverWait(driver,time).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="historicalData"]/div[1]/span[2]/a')))
except:
    print("nothing")

bt1= driver.find_element_by_xpath('//*[@id="historicalData"]/div[1]/span[2]/a')
bt1.click()
a=os.listdir(r'C:\xampp\htdocs\Pattern\csv');




df = pd.read_csv(r'C:/xampp/htdocs/Pattern/csv/'+a[0]);

trace1 = go.Scatter(
                    x=df['Date'], y=df['Open Price'], # Data
                    mode='lines', name='Open price' # Additional options
                   )
trace2 = go.Scatter(x=df['Date'], y=df['Close Price'], mode='lines', name='close price' )
trace3 = go.Scatter(x=df['Date'], y=df['High Price'], mode='lines', name='High Price')

layout = go.Layout(title='',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

# Plot data in the notebook
plot(fig, filename='my.html')

print("<!doctype html><html lang='en'><head>");
print("<meta charset='utf-8'> <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'><meta name='description' content=''><meta name='author' content=''>   <link rel='icon' href='img/logo.png'><title>Pattern</title><!-- Bootstrap core CSS --><link rel='stylesheet' href='css/css/bootstrap.min.css'>	<link rel='stylesheet' href='css/css/bootstrap-grid.css' > </head>  <body class='container-fluid bg-light'> <nav class='navbar navbar-expand-md fixed-top navbar-dark bg-dark'><a class='navbar-brand' href='#'>Pattern analysis</a>    <div class='navbar-collapse offcanvas-collapse' id='navbarsExampleDefault'><ul class='navbar-nav mr-auto'><li class='nav-item active'>   <a class='nav-link' href='#'>Home<span class='sr-only'>(current)</span></a>    </li>  <li class='nav-item'> <a class='nav-link' href='about.html'>AboutUs</a>  </li> <li class='nav-item'><a class='nav-link' href='contact.html'>ContactUs</a>  </li> <li class='nav-item'> <a class='nav-link' href='login.html'>Login</a></li><li class='nav-item'>  <a class='nav-link' href='signup.html'>SignUp</a>    </li>  <li class='nav-item dropdown'>            <a class='nav-link dropdown-toggle' href='' id='dropdown01' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false'>Settings</a><div class='dropdown-menu' aria-labelledby='dropdown01'><a class='dropdown-item' href='#'>Action</a><a class='dropdown-item' href='#'>Another action</a><a class='dropdown-item' href='#'>Something else here</a>  </div></li> </ul> <form class='form-inline my-2 my-lg-0'><input class='form-control mr-sm-2' type='text' placeholder='Search' aria-label='Search'><button class='btn btn-outline-success my-2 my-sm-0' type='submit'>Search</button>  </form> </div>   </nav></div> "); 
print("<div class='container-fluid' style='margin-top:100px;'><table><tr><td style='padding:10px;'><div class='row'><div class='col'>	<div class='col-xs-4'><div class='card'>	<div class='card-header bg-primary'>	Company Info</div><div class='card-body'><p>");

print("<h4>Name:</h4>");print(name);
print("<h4>Symbol:</h4>");print(symbol);
print("<h4>ISIN:</h4>");print(address);

print("</p></div></div>	</div></div></td><td rowspan='2' style='width:900px;padding:10px;'><div class='col'>    <div class='col-xs-12'><div class='card'><div class='card-header bg-success'>Company Share prices</div><div class='card-body'>");
print(" <iframe src='my.html' width ='900px' height ='500px'></iframe>");
print("</div></div>	</div></div>	</div></td></tr><tr><td style='padding:10px;'><div class='row'><div class='col'><div class='col-xs-12'><div class='card'><div class='card-header bg-danger'>Company News</div><div class='card-body'><p>hello pm!!!!</p></div></div></div></div>	</div>	</div></td>	</tr>	</table>	<!-- Footer -->	<div style='background-color:#95b2d0;margin-top:100px;'><footer class='page-footer font-small blue'> <!-- Copyright --><div class='footer-copyright text-center py-3'> &copy 2019 Copyright:<a href='https://www.pattern.com'> WWW.PATTERN.COM</a></div> <!-- Copyright --></footer></div><!-- Footer --></body></html>");
driver.service.stop();
driver.close();


