import os

command = "ps -aux | grep python"

out = os.popen(command).read()
count = 0
for x in out:
    if '\n' == x:
        count += 1

command = "mail -s \"检查python程序运行情况\" 1003324213@qq.com < ps.txt"
if count < 7:
    with open('ps.txt', 'w') as f:
         f.write(out)
    os.system(command)
