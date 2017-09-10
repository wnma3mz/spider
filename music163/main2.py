import requests
import io
import sys
import json
# 解决编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# 用户名
name = "xx"
# 搜索需要上传的数据
params = {
            's': name,
            # 搜索用户是1002，
            'type': 1002,
            'offset': 0,
            'sub': 'false',
            # 限制数量在10个以内
            'limit': 10
}
# 搜索的url
url = "http://music.163.com/api/search/get"
# 添加请求头信息，其中Cookie和Referer必填
headers = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
    "Content-Length":"522",
    "Content-Type":"application/x-www-form-urlencoded",
    "Cookie": "appver=2.0.2",
    "Host":"music.163.com",
    "Referer": "http://music.163.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
}
# 请求信息返回json
user = requests.post(url, data=params).json()
# 处理数据，获得用户id和用户名
user = user['result']['userprofiles'][0]
userid, username = user['userId'], user['nickname']
print(userid, username)
# url = "https://music.163.com/api/user/playlist"
# 用户最近听歌排行url
url = "http://music.163.com/api/v1/play/record"
# 请求数据
params = {
    "uid": userid,
    # "type": 0 所有时间
    "type": 1, # 最近一周
}
# 请求数据
songs_list = requests.post(url, data=params, headers=headers).json()["weekData"]
# 处理数据最近听歌获取前十
for songs in songs_list[:10]:
    # print(songs["song"]["id"])
    print(songs["song"]["name"], songs["song"]["ar"][-1]["name"], '\n')
