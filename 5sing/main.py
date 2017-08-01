#encoding=utf-8
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import urllib.error
from urllib.request import urlopen, Request
from urllib.request import *
import urllib.request


# 获取下载链接
def getmp3(html, name, url):
    # 解析网页源码
    soup = bs(html, 'lxml')
    # 获取下载链接
    download_url = soup.find("audio", class_="music")
    # 如果没有src链接，则重新访问网页；若有则进行下载
    if download_url["src"] == "":
        getJS(url, name)
    else:
        print(download_url["src"])
        urlretrieve(download_url["src"], "/home/sing/%s.mp3" % name)

# 直接获取网页源码
def getHTML(posturl):
    header={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64;rv:14.0) Gecko/20100101 Firefox/14.0.1'}
    request = Request(posturl ,headers = header)
    #打开网页
    try:
        page = urlopen(request)
        html = page.read()
        html = html.decode('UTF-8')
        return html
    except urllib.error.URLError as e:
        print(e.reason)

# 通过selenium获取Js代码
def getJS(url, name):
    driver = webdriver.PhantomJS()
    driver.get(url)
    # 获取JS代码
    html = driver.page_source
    # 获取下载链接
    getmp3(html, name, url)

# 解析网页获取歌名url
def geturl(html):
    soup = bs(html, 'lxml')
    # 排行榜上的歌曲url
    song_name_list = soup.find_all("a", class_="pc_temp_songname")
    for song_name in song_name_list:
        # 输出歌名
        print(song_name.text)
        getJS(song_name["href"], song_name.text)

if __name__ == '__main__':
    # 5ing排行榜的url
    url = "http://www.kugou.com/yy/rank/home/1-22603.html?from=rank" 
    # 解析网页
    html = getHTML(url)
    # 获取歌名的url
    geturl(html)
