from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument(
'--user-agent=Mozilla/5.0 (Linux; Android 4.4.4; HM NOTE 1LTEW Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.0.0.54_r849063.501 NetType/WIFI')
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://sm.leyaoyao.com/customer/message/t/12200414")
time.sleep(3)
# 找到搜索输入框，输入“Android 4.0.2”

time.sleep(10)
driver.quit()
