from selenium import webdriver
import time
url = "https://www.census.gov/construction/bps/uspermits.html?fbclid=IwAR02DAW5FBC-At1R0g8qV_kFxrry7aIK5l1lfb--XDCLehPDUIlQ6r0lz8c"

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': './data'}
options.add_experimental_option('prefs', prefs)

#用chromedriver開啟Chrome
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)


#在網頁中找尋"Download Data並點擊"
driver.find_element_by_xpath("//a[@href='/construction/nrc/xls/permits_cust.xls']").click()
time.sleep(5)
driver.close()