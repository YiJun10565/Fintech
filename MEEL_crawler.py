from selenium import webdriver
import time
import csv

ETFS = []
#open the csv file and record column[0] in a dictionary
with open('Materials Equity ETF List (62).csv', newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		ETFS.append(row[0])

#timestamp now
Now = int(time.time())

for i in range(1, len(ETFS)):
	print(ETFS[i])
	#目標網頁的網址
	url1 = "https://finance.yahoo.com/quote/"
	etf = ETFS[i]
	print(etf)
	url2 = "/history?period1=1451491200&period2="
	now = str(Now)
	url3 = "&interval=1d&filter=history&frequency=1d"
	url = url1+etf+url2+now+url3

	#用chromedriver開啟Chrome
	driver = webdriver.Chrome()
	driver.get(url)

	#在網頁中找尋"Download Data並點擊"
	driver.find_element_by_link_text("Download Data").click()

driver.close()