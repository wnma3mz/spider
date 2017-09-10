from bs4 import BeautifulSoup as bs
import re
import os
import urllib.error
from urllib.request import urlopen, urlretrieve, HTTPCookieProcessor, build_opener, install_opener, Request
from urllib.parse import urlencode
from http.cookiejar import CookieJar
import urllib.request


def getHTML(posturl):
    header={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64;rv:14.0) Gecko/20100101 Firefox/14.0.1'}
    # header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     # AppleWebKit/537.36 (KHTML, like Gecko)'}
    request = Request(posturl ,headers = header)
    #打开网页
    try:
        page = urlopen(request)
        html = page.read()
        html = html.decode('UTF-8')
        return html
    except urllib.error.URLError as e:
        print(e.reason)


def getInfor(html):
    soup = bs(html, 'lxml')


    with open('text.txt', 'a+') as f:
        print("爬取中......")
        # 小说内容
        title = soup.find_all("h1")
        f.write(title[1].text)
        f.write("\n")
        data = soup.find_all("p")
        f.write(data[1].text)
        f.write("\n")
        f.write("\n")
        f.write("\n")
        print("爬取完毕")





url = 'http://www.laifudao.com/wangwen/'
url0 = 'http://www.laifudao.com'
# 小说第一章
# url = 'http://read.qidian.com/chapter/WVfRBg3f0Rqt-wSl2uB4dQ2/POrenFOevQj6ItTi_ILQ7A2'
html = getHTML(url)

# i = 1
soup = bs(html, 'lxml')
print(soup)
# hreflist = soup.find_all("h1")
# for href in hreflist[1:-3]:
#     # print(url0 + href.a["href"])
#     html = getHTML(url0 + href.a["href"])
#     getInfor(html)
# for tag in href[20:130]:
#     url = "http:" + tag["href"]
#     # print(url)
#     html = getHTML(url)
#     getInfor(html)
#     # i += 1
#     # print(html)
