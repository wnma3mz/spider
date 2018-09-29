import requests
import time
url = 'http://www.toutiao.com/c/user/article/?page_type=1&user_id=65873279866&max_behot_time=0&count=20&as=A1E50949F29FB01&cp=59924F9BC0513E1'
json = requests.get(url).json()
article_list = []
for item in json['data']:
    article_list.append(item['item_id'])

for _ in range(100000):
    for num in article_list:
        url = 'http://www.toutiao.com/i%s/' % num
        html = requests.get(url).content
        time.sleep(1)
