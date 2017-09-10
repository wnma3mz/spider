# -*- coding: UTF-8 -*-
# scrapy.py
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re
class ScrapyMusic163(object):
    # 网易云音乐WEB端的爬取
    # GET_ID:获取用户的ID号码
    # GET_INFO:获取用户信息
    def GET_ID(self, name):
        # 获取用户id号
        # 获取JS加载的页面
        driver = webdriver.Chrome()
        driver.get("http://music.163.com/#/search/m/?s=%s&type=1002" % name)
        driver.switch_to.frame("g_iframe")
        html = driver.page_source
        driver.close()

        # 解析页面
        soup = bs(html, 'lxml')
        # print(soup)
        # 获取ID
        user = soup.find_all(title=name)
        # print(user)
        # 匹配ID
        url = re.findall(r'/user/home\?id=.+ti', str(user[1]))
        url = str(url)[2:-6]
        return url


    def JUDGE_SEX(self, soup):
        sex = soup.find_all("i")
        if sex[1]["class"][2][-1:] == "1":
            return "性别：男"
        elif sex[1]["class"][2][-1:] == "2":
            return "性别：女"
        else:
            return "unknown"

    def GET_INFO(self, name):
        # 获取用户听歌信息
        # 获取JS加载的用户信息
        self.id = ScrapyMusic163.GET_ID(self, name)
        driver = webdriver.PhantomJS()
        driver.get("http://music.163.com/#%s" % self.id)
        driver.switch_to.frame("g_iframe")
        html = driver.page_source
        # 解析页面
        soup = bs(html, "lxml")
        all_li = soup.find_all('li')
        # 三个数据：歌名、歌手、歌曲链接
        self.song = []
        self.author = []
        self.url = []
        self.sex = ScrapyMusic163.JUDGE_SEX(self, soup)
        for li in all_li:
            # 用户听歌信息
            li_song = li.find(class_="song")
            if li_song:
                # 歌名
                title = li_song.find("a")
                self.song.append(title.text)
                # 作者
                author = li_song.find(class_="s-fc8")
                self.author.append(author.text)
                # 歌曲地址
                self.url.append("http://music.163.com/#" + title["href"])

        return self.song, self.author, self.url, self.sex
