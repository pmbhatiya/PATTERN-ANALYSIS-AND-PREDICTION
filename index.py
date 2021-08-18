#!C:\Users\PM BHATIYA\AppData\Local\Programs\Python\Python36\python.exe
print('content-type:text/html')
print()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



from selenium.webdriver.chrome.options import Options
import os

CHROMEDRIVER_PATH = 'C:\webd\chromedriver.exe'
WINDOW_SIZE = "1920,1080"

chrome_options = webdriver.ChromeOptions()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                         )


driver.get('https://www.indiainfoline.com/top-news')
bt = driver.find_elements_by_xpath('//*[@id="search-list"]/ul/li/div/div/p[1]/a')
href=[x.get_attribute("href") for x in bt]
#print(href)

p=0;
bt1 = driver.find_elements_by_xpath('//*[@id="search-list"]/ul/li/div/div/p[1]/a')
aval=[xy.text for xy in bt1]
#print(aval)

bt2=driver.find_elements_by_xpath('//*[@id="search-list"]/ul/li/div/div/p[3]')
time=[xz.text for xz in bt2]
bt3=driver.find_elements_by_xpath('//*[@id="search-list"]/ul/li/div/div/p[2]')
inv=[xx.text for xx in bt3]
print("<!doctype html> <html lang='en'>   <head>     <meta charset='utf-8'>     <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>     <meta name='description' content=''>     <meta name='author' content=''>     <link rel='icon' href='img/logo.png'>      <title>Pattern</title> 	     <!-- Bootstrap core CSS -->     <link rel='stylesheet' href='css/css/bootstrap.min.css' > 	  <link rel='stylesheet' href='css/css/bootstrap.css' > 	  <link rel='stylesheet' href='css/css/bootstrap-grid.css' > 	  <script src='css/js/bootstrap.min.js'></script>  <script src='js/jquery/jquery-ui.min.js'></script>     <!-- Custom styles for this template -->     <link href='style.css' rel='stylesheet'>   </head>   <body class='bg-light'>      <nav class='navbar navbar-expand-md fixed-top navbar-dark bg-dark'>       <a class='navbar-brand' href='#'>Pattern analysis</a>           <div class='navbar-collapse offcanvas-collapse' id='navbarsExampleDefault'>         <ul class='navbar-nav mr-auto'>           <li class='nav-item active'>             <a class='nav-link' href='#'>Home<span class='sr-only'>(current)</span></a>           </li>           <li class='nav-item'>             <a class='nav-link' href='about.html'>AboutUs</a>           </li> 		  <li class='nav-item'>             <a class='nav-link' href='contact.html'>ContactUs</a>           </li>           <li class='nav-item'>             <a class='nav-link' href='login.html'>Login</a>           </li>           <li class='nav-item'>             <a class='nav-link' href='signup.html'>SignUp</a>           </li>           <li class='nav-item dropdown'>             <a class='nav-link dropdown-toggle' href='' id='dropdown01' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false'>Settings</a>             <div class='dropdown-menu' aria-labelledby='dropdown01'>               <a class='dropdown-item' href='#'>Action</a>               <a class='dropdown-item' href='#'>Another action</a>               <a class='dropdown-item' href='#'>Something else here</a>             </div>           </li>         </ul>         <form action='search.py' method='POST' class='form-inline my-2 my-lg-0'>           <input class='form-control mr-sm-2' type='text' name='search' placeholder='Search' aria-label='Search'>           <button class='btn btn-outline-success my-2 my-sm-0' type='submit'>Search</button>         </form>       </div>     </nav> <!-- home -->	");
print(" <div  data-spy='scroll' style='position:absolute;width:20%;margin-top:80px;' class='col-md-2' data-offset='30'>");
for n,h,v,l in zip(aval,href,time,inv):
	p=p+1;
	if(p<4):
		print("<p>  <a href='"+h+"'>"+n+"</a></p><p>"+l+"</p><p>"+v+"</p>");
	elif(p==4):
		print("</div><div class='row justify-content-center' style='margin-top:100px;width:100%;position:absolute;'> <div class='col-md-6'> <div class='card'> <header class='card-header'> 	<a href='login.html' class='float-right btn btn-outline-primary mt-1'>Log in</a> 	<h4 class='card-title mt-2'>Sign up</h4> </header> <article class='card-body'> <form> 	<div class='form-row'> 		<div class='col form-group'> 			<label>First name </label>   		  	<input type='text' class='form-control' placeholder=''> 		</div> <!-- form-group end.// --> 		<div class='col form-group'> 			<label>Last name</label> 		  	<input type='text' class='form-control' placeholder=' '> 		</div> <!-- form-group end.// --> 	</div> <!-- form-row end.// --> 	<div class='form-group'> 		<label>Email address</label> 		<input type='email' class='form-control' placeholder=''> 		<small class='form-text text-muted'>We'll never share your email with anyone else.</small> 	</div> <!-- form-group end.// --> 	<div class='form-group'> 			<label class='form-check form-check-inline'> 		  <input class='form-check-input' type='radio' name='gender' value='option1'> 		  <span class='form-check-label'> Male </span> 		</label> 		<label class='form-check form-check-inline'> 		  <input class='form-check-input' type='radio' name='gender' value='option2'> 		  <span class='form-check-label'> Female</span> 		</label> 	</div> <!-- form-group end.// --> 	<div class='form-row'> 		<div class='form-group col-md-6'> 		  <label>City</label> 		  <input type='text' class='form-control'> 		</div> <!-- form-group end.// --> 		<div class='form-group col-md-6'> 		  <label>Country</label> 		  <select id='inputState' class='form-control'> 		    <option> Choose...</option> 		      <option>Uzbekistan</option> 		      <option>Russia</option> 		      <option selected=''>United States</option> 		      <option>India</option> 		      <option>Afganistan</option> 		  </select> 		</div> <!-- form-group end.// --> 	</div> <!-- form-row.// --> 	<div class='form-group'> 		<label>Create password</label> 	    <input class='form-control' type='password'> 	</div> <!-- form-group end.// -->      <div class='form-group'>         <button type='submit' class='btn btn-primary btn-block'> Register  </button>     </div> <!-- form-group// -->          <small class='text-muted'>By clicking the 'Sign Up' button, you confirm that you accept our <br> Terms of use and Privacy Policy.</small>                                          </form> </article> <!-- card-body end .// --> <div class='border-top card-body text-center'>Have an account? <a href='login.html'>Log In</a></div> </div> <!-- card.// --> </div> <!-- col.//-->  </div> <!-- row.//-->   </div> 	<!-- end home --> 	 <div  data-spy='scroll' style='position:absolute;width:20%;margin-top:80px;margin-left:1200px;'  class='col-md-2' data-offset='30' >");
	elif(p<8):
		print("<p>  <a href='"+h+"'>"+n+"</a></p><p>"+l+"</p><p>"+v+"</p>");
	else:
		print();
print("</div>	 	 	 	 	  	<!-- Footer --> 	<div style='position:absolute;margin-top:900px;background-color:#95b2d0;width:100%;'>     <footer class='page-footer font-small blue'>    <!-- Copyright -->   <div class='footer-copyright text-center py-3'>&copy; 2019 Copyright:     <a href='https://www.pattern.com'> WWW.PATTERN.COM</a>   </div>   <!-- Copyright -->  </footer> </div> <!-- Footer -->  </body> </html>");


driver.service.stop();