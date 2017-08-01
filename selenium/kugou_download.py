from bs4 import BeautifulSoup as bs
import re
import os
import urllib.error
from urllib.request import urlopen, urlretrieve, HTTPCookieProcessor, build_opener, install_opener, Request
from urllib.parse import urlencode
from http.cookiejar import CookieJar
import urllib.request


# 获取下载链接
def getmp3(html, name, url):
    # 解析网页源码
    soup = bs(html, 'lxml')
    # 获取下载链接
    download_url = soup.find("audio", class_="music")
    # 如果没有src链接，则重新访问网页；若有则进行下载
    if download_url["src"] == "":
        getHTML(url, name)
    else:
        print(download_url["src"])
        urlretrieve(download_url["src"], "/home/sing/%s.mp3" % name)

def getHTML(url, name):
    header={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64;rv:14.0) Gecko/20100101 Firefox/14.0.1'}
    # header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
     # AppleWebKit/537.36 (KHTML, like Gecko)'}
    request = Request(url + name ,headers = header)
    #打开网页
    try:
        page = urlopen(request)
        html = page.read()
        html = html.decode('UTF-8')
        # getmp3(html, name, url)
        return html
    except urllib.error.URLError as e:
        print(e.reason)


def getInfor(html):
    soup = bs(html, 'lxml')


name = "一人饮酒醉"
url = "http://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord="
html = getHTML(url, name)
print(html)