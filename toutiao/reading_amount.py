import requests
import io
import sys
import re
import time
import json
import pandas as pd
from pandas import Series, DataFrame
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


def save_file(file_name, frame):
    try:
        frame_old = pd.read_csv(file_name, encoding='gbk', engine='python')
        frame_old.pop('Unnamed: 0')
        # print(frame_x.head(3))
        new_frame = pd.merge(frame_old, frame, how='right', on='title')
        # print(new_frame)
        new_frame.to_csv(file_name, encoding='gbk')
    except:
        frame.to_csv(file_name, encoding='gbk')


if __name__ == '__main__':
    url = 'http://www.toutiao.com/c/user/article/?page_type=1&user_id=65873279866&max_behot_time=0&count=20&as=A1E50949F29FB01&cp=59924F9BC0513E1'
    json = requests.get(url).json()
    data_y_reading = {
        'title': [item['title'] for item in json['data']],
        'reading_amount': [item['go_detail_count'] for item in json['data']]
    }

    data_y_date = {
        'title': [item['title'] for item in json['data']],
        'date_now': [time.strftime("%D %H", time.localtime()) for _ in range(len(json['data']))]
    }

    df1 = DataFrame(data_y_reading, columns=['title', 'reading_amount'])

    df2 = DataFrame(data_y_date, columns=['title', 'date_now'])

    save_file('reading_amount_1.csv', df1)
    save_file('reading_amount_2.csv', df2)

