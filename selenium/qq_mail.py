from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
from bs4 import BeautifulSoup as bs
import os




if __name__ == '__main__':
    url = 'https://mail.qq.com/'

    # login
    driver = webdriver.Chrome()
    # geturl
    driver.get(url)

    # write form
    driver.switch_to.frame('login_frame')
    email = driver.find_element_by_id("u")
    # 输入QQnumber
    email.send_keys()
    passwd = driver.find_element_by_id("p")
    # 输入QQ密码
    passwd.send_keys()
    login = driver.find_element_by_id("login_button").click()

    # wait time
    time.sleep(1)
    
    # find_target
    # target_url 目标url
    driver.get(target_url)
    driver.switch_to.frame('mainFrame')
    driver.find_element_by_class_name("toarea").click()
    
    # start spider
    for time in range(1,50):
        print("start %s" % time)
        url_list = driver.find_elements_by_class_name("title")
        for url in url_list[::2]:
            page = url.get_attribute("href")
            print(page)
        # time.sleep(1)
        driver.find_element_by_id("nextmail").click()
        print("finish %s" % time)
