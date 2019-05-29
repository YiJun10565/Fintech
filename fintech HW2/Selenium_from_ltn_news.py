from selenium import webdriver              
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import datetime
import time
import calendar
import pandas as pd

#encoding=utf-8
#option = webdriver.ChromeOptions()
#option.add_argument('headless')
#option.add_argument('window-size=1200x600')
#browser = webdriver.Chrome(chrome_options=option)



# list of link constructing 

keywords = ['洗錢', '金融詐欺', '武器擴散', '毒品走私', '恐怖主義', '毒品犯運', '貪污', '賄賂', '詐欺', '走私', '稅務犯罪', '內線交易', '市場操控', '專業洗錢', '組織犯罪']

base_url = "https://news.ltn.com.tw/search/?keyword=&conditions=and"
#start year part , ...
syp = "&SYear="
smp = "&SMonth="
sdp = "&SDay="
eyp = "&EYear="
emp = "&EMonth="
edp = "&EDay="
now = datetime.datetime.now()

#for y in Year:
#	for i in range(4):
#			print("from ", y, '/', Smonth[i], '/1 to ', y, '/', Emonth[i], '/', Edate[i])

ltn_news_link = []
for y in range(2005, now.year +1):
	for m in range(1, 12+1):
		if(y == now.year and m > now.month):
			break
		url = base_url + syp + str(y) + smp + str(m) + sdp + '1'
		url = url + eyp + str(y) + emp + str(m) + edp
		if(y == now.year and m == now.month):
			url += str(now.day) 
		else:
			url += str( calendar.monthrange(y, m)[1])
		#print(url)
		ltn_news_link.append(url)
#for link in ltn_news_link:
#	print(link)

option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('window-size=1200x600')
browser = webdriver.Chrome(options=option)

news_count = 0

#the file has a "-1" at the end 
#make sure we won't accidentally rewrite the data since it takes really long time
fp_link = open("./news_link_list-1.txt", 'w', encoding='utf-8')
fp_title = open("./news_title_list-1.txt", 'w', encoding='utf-8')

for link in ltn_news_link :	
	print(link)
	browser.get(link)
	break_flag = False
	# colecting link for a single page of a list 
	while not break_flag :
		try:
			time.sleep(5)
#			tmp_list = browser.find_elements_by_class_name("tit")
			WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "tit")))
		except:
			print('Can\'t find the title')
			break
		else:
			tmp_list = browser.find_elements_by_class_name("tit")
			flag = 0
			length = len(tmp_list)
			for e in tmp_list:
			#news_title_list.append(e.text)
			#news_link_list.append(e.get_attribute('href'))
			#print(news_title_list[news_count], ' : ', news_link_list[news_count])
				t = e.text
				l = e.get_attribute('href')
				fp_title.write(t)
				fp_title.write('\n')
				fp_link.write(l)
				fp_link.write('\n')
				news_count += 1
				flag += 1
				print(news_count)
		print(flag, length)	
		try:
			time.sleep(5)
			#make sure that the above processing are all done
			p_next = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "p_next")))
			p_next.click()
			print('Turn Page')
		except:
			break_flag = True
#	tit_list = browser.find_elements_by_class_name('tit')
#	for tit in tit_list:
#		print(tit)
#		print(tit.text)
#	print(tit_list)
#	
try:
	browser.close()
except :
	print('Webdriver Closing Error')
else:
	print("done")

