from selenium import webdriver
import time
import requests
url = 'http://www.toutiao.com/c/user/article/?page_type=1&user_id=65873279866&max_behot_time=0&count=20&as=A1E50949F29FB01&cp=59924F9BC0513E1'
json = requests.get(url).json()
article_list = []
for item in json['data']:
    article_list.append(item['item_id'])

for _ in range(10000):
    # driver = webdriver.Firefox()
    driver = webdriver.PhantomJS(executable_path='/root/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')  
    for num in article_list:
        url = 'http://www.toutiao.com/i%s/' % num
        try:
            driver.get(url)
            for dis in range(1000, 5000)[::500]:
                js="document.documentElement.scrollTop=%s" % dis
                driver.execute_script(js)
                time.sleep(3)
        except:
            continue
    driver.quit()

