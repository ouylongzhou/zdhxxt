from selenium import webdriver
from time import sleep

class getsss():

    def chromes(self):
        driver = webdriver.Chrome()
        driver.get(r'https://www.baidu.com/')
        driver.implicitly_wait(10)
        driver.maximize_window()

        #选择百度输入框
        driver.find_element_by_id('kw').send_keys('乐摇摇')
        # 点击百度
        driver.find_element_by_id('su').click()

        #????

        ele = driver.find_element_by_css_selector('''#content_left>div:nth-child(1) h3 a''')
        print(ele.text)

        sleep(2)
        driver.quit()
