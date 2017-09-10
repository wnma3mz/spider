# !/usr/bin/python
# -*-coding:utf-8 -*-
# author:Lu
import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

def postHtml(url):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    request = Request(url, headers = header)
    #打开网页
    try:
        page = urlopen(request)
        html = page.read()
        html = html.decode('UTF-8')
        return html
    except urllib.error.URLError as e:
        print(e.reason)

def getDetail(html):
    soup = bs(html, 'lxml')
    title = soup.find(class_="post-page-title")
    time = soup.find(class_="post-page-time")
    author = soup.find(class_="post-page-author")
    return title.text, time.text, author.text

def getInfo(html):
    url0 = "http://blog.ncuos.com"
    soup = bs(html, 'lxml')
    # 每个信息分块，分为图片，标题，作者，时间
    part_list = soup.find_all(class_="post-excerpt")
    for part in part_list:
        # 由于该页无时间，所以获取下一个网页
        url = part.find("a")
        url = url0 + url["href"]
        # 访问下一个网页
        html = postHtml(url)
        # 解析网页，返回标题，时间，作者
        title, time, author = getDetail(html)
        # 获取图片链接
        img = part.find("img")["src"]
        print(title, time, author, img)


if __name__ == "__main__":
    url = "http://blog.ncuos.com/"
    # 请求网站，返回html源代码
    html = postHtml(url)
    # 解析html
    getInfo(html)