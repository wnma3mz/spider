import pandas as pd
frame_x = pd.read_csv('data_inc.csv', encoding='gbk', engine='python')
frame_x.pop('Unnamed: 0')
        # print(frame_x.head(3))
# new_frame = pd.merge(frame_x, frame_y, how='right', on='title')
print(frame_x)
# frame_x.to_csv('test.csv', encoding='gbk')
