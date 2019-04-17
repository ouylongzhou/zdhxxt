# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep

# mobile_emulation = {"deviceName":"Galaxy S5"}
mobile_emulation = {
    "deviceMetrics": { "width": 400, "height": 700, "pixelRatio": 3.0 },
    "userAgent":"Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1"}
option = webdriver.ChromeOptions()
option.add_experimental_option('mobileEmulation',mobile_emulation)
driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=option)
# driver.get('https://sm.leyaoyao.com/customer/login?username=orTHPwkbOE8lljCzx_iAouOmCbiU&password=c096aeb06a9db5439e99acf7dc80ed0d&equipmentId=12200414')
# driver.get('https://sm.leyaoyao.com/customer/message/t/12200414')

driver.get("https://sm.leyaoyao.com/customer/login?username=orTHPwkbOE8lljCzx_iAouOmCbiU&password=c096aeb06a9db5439e99acf7dc80ed0d&equipmentId=32000303")
driver.get("https://sm.leyaoyao.com/pages/start.html?equipmentId=32000303")

print('打开浏览器')
print(driver.title)
sleep(10)
print('关闭')
driver.quit()
print('测试完成')