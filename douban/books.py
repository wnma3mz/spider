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
    # s = requests.session()
    # response = s.post(posturl, headers = agent)
    # 打开网页
    print(posturl)
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
        try:
            source = book.find(class_="rating_nums").text
            if float(source.strip()) >= 9.0:
                book_url = book.h2.a.get("href")
                # print(book_url)
                getInf1(book_url)
        except AttributeError:
            print("\n")

def getInf1(url):
    html = getHTML(url)
    soup1 = bs(html, 'lxml')
    print(soup1.find("h1").text)
    print(soup1.find(property="v:average").text)
    print("作者：", soup1.find(id="info").a.text.strip())
    print(soup1.find(class_="intro").text)
    print("\n")


def save(data):
    pass

if __name__ == '__main__':
    url_index = 'https://book.douban.com'
    url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    html = getHTML(url)
    soup = bs(html, 'lxml')
    tag_list = soup.find_all(href = re.compile("/tag"))
    for tag in tag_list[1:]:
        tag_url = url_index + tag.get("href")
        # html = getHTML(tag_url)
        print("tag:", tag.get("href")[5:])

        for x in range(100):
            print("第%d页" % (x + 1))
            url0 = tag_url
            url1 = '?start=%d&type=T' % (x*20)
            print(url0 + url1)
            html0 = getHTML(url0 + url1)
            getInf(html0)

