import os 
import json

name = 'xx'
# Shell命令
command = 'curl -d "s=%s&limit=20&type=1002&offset=0" -b "appver=2.0.2;" http://music.163.com/api/search/get/' % name
# 在python输出运行结果，保留到user中
user = os.popen(command).read()
# 用json打开，处理用户信息
user = json.loads(user)
user = user['result']['userprofiles'][0]
userid, username = user['userId'], user['nickname']
print(userid, username)
