import requests
import io
import sys
import re
import time
import json
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

url = 'http://www.toutiao.com/c/user/article/?page_type=1&user_id=65873279866&max_behot_time=0&count=20&as=A1E50949F29FB01&cp=59924F9BC0513E1'
json = requests.get(url).json()
data_y = {'title':[], 'reader_counts':[], 'comments_counts':[]}
text = ''
for item in json['data']:
    text += item['title'] + '\n'
    text += "阅读数：" + str(item['go_detail_count']) + "评论数:" + str(item['comments_count'])  + "\n" + "\n"

with open('content.txt', 'w') as f:
    f.write(text)
command = "mail -s \"阅读量定时邮件\" 1462273301@qq.com 1003324213@qq.com<content.txt"
os.system(command)
