from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException                
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import datetime
import time
import pandas as pd

#coding=utf-8
#option = webdriver.ChromeOptions()
#option.add_argument('headless')
#option.add_argument('window-size=1200x600')
#browser = webdriver.Chrome(chrome_options=option)



# list of link constructing 
base_url = "https://news.ltn.com.tw/search/?keyword=%E6%B4%97%E9%8C%A2&conditions=and"
#start year part , ...
syp = "&SYear="
smp = "&SMonth="
sdp = "&SDay="
eyp = "&EYear="
emp = "&EMonth="
edp = "&EDay="
now = datetime.datetime.now()

Year = []
for i in range(2005, now.year+1):
	Year.append(i)
Smonth = []
Emonth = []
for i in range(1, 12, 3):
	Smonth.append(i)
	Emonth.append(i+2)
Sdate = [1, 1, 1, 1]
Edate = [31, 30, 30, 31]

#for y in Year:
#	for i in range(4):
#			print("from ", y, '/', Smonth[i], '/1 to ', y, '/', Emonth[i], '/', Edate[i])

ltn_news_link = []
for y in Year:
	for m in range(4):
		if(y == now.year and 3*m >= now.month):
			break
		url = base_url + syp + str(y) + smp + str(Smonth[m]) + sdp + str(Sdate[m])
		if(y == now.year and 3*(m+1) >= now.month):
			url = url + eyp + str(y) + emp + str(now.month) + edp + str(now.day) 
		else:
			url = url + eyp + str(y) + emp + str(Emonth[m]) + edp + str(Edate[m])
		#print(url)
		ltn_news_link.append(url)

option = webdriver.ChromeOptions()
#option.add_argument('headless')
option.add_argument('window-size=1200x600')
browser = webdriver.Chrome(options=option)

news_count = 0
news_title_list = []
news_link_list = []
test_link = []
test_link.append(ltn_news_link[0])
for link in test_link:	
	print(link)
	browser.get(link)
	# colecting link for a single page of a list 
	while True :
		tmp_list = browser.find_elements_by_class_name("tit")
		for e in tmp_list:
			news_title_list.append(e.text)
			news_link_list.append(e.get_attribute('href'))
			#print(news_title_list[news_count], ' : ', news_link_list[news_count])
			news_count += 1
		p_next = browser.find_element_by_class_name('p_next')
		print(dir(p_next))
		if not p_next.is_displayed():
			break
		else:
			p_next.click()
#	tit_list = browser.find_elements_by_class_name('tit')
#	for tit in tit_list:
#		print(tit)
#		print(tit.text)
#	print(tit_list)
#	
for i in range(news_count):
	print( news_title_list[i], ' : ', news_link_list[i])
print(news_count)
try:
	browser.close()
except :
	print('Webdriver Closing Error')
else:
	print("done")
  #  Title_list.append(tit['data-desc'])