#coding=utf-8
#encoding=utf-8
# -
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
base_url = "https://news.ltn.com.tw/search/?keyword=%E6%B4%97%E9%8C%A2&conditions=and"
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

for link in ltn_news_link :	
	print(link)
	browser.get(link)
	# colecting link for a single page of a list 
	while True :
		try:
			WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "tit")))
			
		except:
			print('Can\'t find the title')
			break
		else:
			tmp_list = browser.find_elements_by_class_name("tit")
			
			title_list = []
			for e in tmp_list:
				title_list.append(e.text)
			for t in title_list:
				news_count += 1
				next_file_name = './data/ltn_news-' + str(news_count+1) + '.txt'
				try:
					open(next_file_name, 'r', encoding='utf-8')
				except:
					read_file_name = './data/ltn_news' + str(news_count) + '.txt'
					write_file_name = './data/ltn_news-' + str(news_count) + '.txt'
					rfp = open(read_file_name, 'r', encoding='utf-8')
					wfp = open(write_file_name, 'w', encoding='utf-8')
					wfp.write(t)
					wfp.write('\n')
					line = rfp.readline()
					while line :
						wfp.write(line)
						wfp.write('\n')
						line = rfp.readline()
					print(news_count)
				else:
					continue
			
		try:
			time.sleep(2)
			print("Done?")
			# If next page button is displayed, then click it 
			p_next = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "p_next")))
			p_next.click()
		except:
			break
try:
	browser.close()
except :
	print('Webdriver Closing Error')
else:
	print("done")

