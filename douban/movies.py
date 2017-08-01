from bs4 import BeautifulSoup as bs
import re
import os
import urllib.error
from urllib.request import urlopen, urlretrieve, HTTPCookieProcessor, build_opener, install_opener, Request
from urllib.parse import urlencode
from http.cookiejar import CookieJar
import urllib.request
import requests

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'

def getHTML(posturl):
    request = Request(posturl)
    # 登陆表单
    s = requests.session()
    # response = s.post(posturl, headers = headers)
    # 打开网页
    try:
        page = urlopen(request)
        html = page.read()
        html = html.decode('UTF-8')
        return html
    except urllib.error.URLError as e:
        print(e.reason)


def getInf(html):
    soup = bs(html, 'lxml')
    book_list = soup.find_all(class_="info")
    for book in book_list:
        source = book.find(class_="rating_nums").text
        if float(source.strip()) > 9.0:      
            print(book.h2.a.get("title"))
            print(book.find(class_="pub").text.strip())
            # if book.find("p").text:
                # print(book.find("p").text)
            print("\n")



def save(data):
    pass

if __name__ == '__main__':
    url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85%E7%89%87&type=11&interval_id=100:90&action='
    # print(url0 + url1)
    html = getHTML(url)
    print(html)
    # getInf(html)

