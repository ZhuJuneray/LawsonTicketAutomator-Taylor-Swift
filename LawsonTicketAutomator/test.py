
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

driver = webdriver.Chrome(options=chrome_options)

driver.get('http://www.baidu.com/')  # 打开百度