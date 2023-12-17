import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import messagebox
from selenium.common.exceptions import NoSuchElementException

url = "https://l-tike.com/st1/taylorswift2/Tt/Ttg030top/restore"


def click_element(xpath):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(0.75)


def search_element(xpath):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    time.sleep(0.1)
    return driver.find_element(By.XPATH, xpath)


with open('info.txt', 'r') as file:
    lines = file.readlines()

customer_info = []
stride = 2
for i in range(1, len(lines), stride):
    line = lines[i]
    customer_info.append(line)


# 创建ChromeOptions对象
chrome_options = Options()

chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# 使用无痕模式打开浏览器
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--incognito")
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
chrome_prefs = {}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_prefs['chrome.page.customHeaders.referrer'] = url
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# 创建浏览器驱动对象
driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    })
                  """
})
# 打开网页
driver.get(url)
time.sleep(0.2)

driver.find_element(By.ID, 'CONSENT_CHK_BOX').click()
time.sleep(0.2)
driver.find_element(By.ID, 'NEXT').click()
# click_element('//*[@id="ENTRY_DETAIL_BUTTON_0"]')# VIP package
click_element('//*[@id="ENTRY_DETAIL_BUTTON_1"]')# General ticket

time.sleep(0.01)
click_element('//*[@id="sameppfmDateSelectButton"]/a') # Select Date button

time.sleep(0.2)
# click_element('//*[@id="sameppfmModalContents"]/div/div[2]/div[1]') # 2.7 panel
# click_element('//*[@id="sameppfmModalContents"]/div/div[2]/div[2]') # 2.8 panel
# click_element('//*[@id="sameppfmModalContents"]/div/div[2]/div[3]') # 2.9 panel
click_element('//*[@id="sameppfmModalContents"]/div/div[2]/div[4]') # 2.10 panel

time.sleep(0.2)
click_element('//*[@id="pfday"]/div/div[2]/div[2]/div[1]/ul/li[1]/div[2]/div/div/div/div[1]/ul/li/div/ul/li[1]/div') # panel 1, SS seat or vip 1

time.sleep(0.2)
ticket_number_select = search_element('//*[@id="c_PRT_CNT1"]')
select = Select(ticket_number_select)
select.select_by_value('2')

click_element('//*[@id="c_SEL"]')
click_element('//*[@id="addHopeBtn"]')
click_element('//*[@id="pfday"]/div/div[2]/div[2]/div[1]/ul/li[1]/div[1]/ul/li/div')
click_element('//*[@id="pfday"]/div/div[2]/div[2]/div[1]/ul/li[1]/div[2]/div/div/div/div[1]/ul/li/div/ul/li[2]/div') # panel 2
ticket_number_select = search_element('//*[@id="c_PRT_CNT1"]')
select = Select(ticket_number_select)
select.select_by_value('2')

# click_element('//*[@id="c_SEL"]')
# click_element('//*[@id="addHopeBtn"]')
# click_element('//*[@id="pfday"]/div/div[2]/div[2]/div[1]/ul/li[1]/div[1]/ul/li/div')
# click_element('//*[@id="pfday"]/div/div[2]/div[2]/div[1]/ul/li[1]/div[2]/div/div/div/div[1]/ul/li/div/ul/li[3]/div')
# ticket_number_select = search_element('//*[@id="c_PRT_CNT1"]')
# select = Select(ticket_number_select)
# select.select_by_value('2')

click_element('//*[@id="c_SEL"]')

click_element('//*[@id="c_ENTRY_HOPE"]')

# Customer Information Registration
search_element('//*[@id="MAIL_ADDRS"]').send_keys(customer_info[0])
time.sleep(0.1)
search_element('//*[@id="MAIL_ADDRS_CONFIRM"]').send_keys(customer_info[0])
time.sleep(0.1)
search_element('//*[@id="TEL"]').send_keys(customer_info[1])
time.sleep(0.1)
search_element('//*[@id="TEL_CONFIRM"]').send_keys(customer_info[1])
time.sleep(0.1)
click_element('//*[@id="NEXT"]')

# Item Authentication

root = tk.Tk()
root.withdraw()  # 隐藏主窗口
messagebox.showinfo("完成验证码后点击确认后执行后续代码", "完成拖动验证码后点击确认执行后续代码")
# window=messagebox._show()
click_element('//*[@id="NEXT_BUTTON"]')
# window.destroy()

# Applicant's Name
search_element('//*[@id="APLCT_FIRST_NAME"]').send_keys(customer_info[2])
time.sleep(0.1)
search_element('//*[@id="APLCT_LAST_NAME"]').send_keys(customer_info[3])
time.sleep(0.1)
search_element('//*[@id="PWD"]').send_keys(customer_info[4])
time.sleep(0.1)
search_element('//*[@id="PWD_CNF"]').send_keys(customer_info[4])
time.sleep(0.1)
click_element('//*[@id="NEXT_BUTTON"]')

# Please answer this questionnaire
for i in range(1,12):
    click_element(f'//*[@id="q_{i}-Iagree"]')
search_element('//*[@id="q_12"]').send_keys(customer_info[5])
time.sleep(0.1)
search_element('//*[@id="q_13"]').send_keys(customer_info[6])
time.sleep(0.1)
search_element('//*[@id="q_14"]').send_keys(customer_info[7])
time.sleep(0.1)
click_element('//*[@id="NEXT"]')
click_element('//*[@id="NEXT"]')
click_element('//*[@id="ENTRY_FIX"]')

# Credit Card Information Entry
search_element('//*[@id="pan"]').send_keys(customer_info[8])
time.sleep(0.1)

search_element('//*[@id="securityCode"]').send_keys(customer_info[10])
time.sleep(0.1)

expire_month_select = search_element('//*[@id="EXPIRE_MONTH"]')
select = Select(expire_month_select)
select.select_by_value(customer_info[9].split('/')[0])
expire_year_select = search_element('//*[@id="EXPIRE_YR"]')
Select(expire_year_select).select_by_value('20'+customer_info[9].split('/')[1].replace('\n',''))


click_element('//*[@id="NEXT_BUTTON"]')



# todo 验证码填写错误提示
# Entry Details


time.sleep(200)
driver.quit()
