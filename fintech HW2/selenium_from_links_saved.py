#encoding=utf-8
from selenium import webdriver               
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import datetime
import time
import calendar
import pandas as pd


fp = open('news_link_list.txt', 'r')
#fp_title = open('news_title_list.txt', 'r', encoding='utf-8')
option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('window-size=1200x600')
browser = webdriver.Chrome(options=option)

link = fp.readline()
count = 0
fail_list = []
text_store_list = ['text', 'cont', 'news_content']
while link:

	count += 1
	print(count, ':', link)
	next_file_name = './data/ltn_news' + str((count+1)) + '.txt'
	try:
		test = open(next_file_name, 'r')
		test.close()
	except:
		outputfile_name = './data/ltn_news' + str(count) + '.txt'	
		wfp = open( outputfile_name, 'w', encoding='utf-8')
	#	title = fp_title.readline()
	#	wfp.write(title)
		browser.get(link)
		for t in text_store_list:
			print(t)
			try:
				Text = browser.find_element_by_class_name(t)
				#Text = 	 WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, t)))
			except:
				continue
			else:
				break
		l = Text.find_elements_by_tag_name('p')
		n1 = Text.find_elements_by_class_name('time')
		n2 = Text.find_elements_by_class_name('appE1121')
		n3 = Text.find_elements_by_class_name('ph_b')
		for i in l:
			if i not in n1 and i not in n2 and i not in n3:
				wfp.write(i.text)
				wfp.write('\n')
		link = fp.readline()
		wfp.close()
	else:
		link = fp.readline()
	
	
browser.close()
fp.close()