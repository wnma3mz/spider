# 百度百科爬虫

### 文件夹存放的是爬取Python的百度百科，遍历网页中的关键词深度爬取，最后将全部内容输出到一个简单网页上。本代码是在imooc课程的基础上改写而来[imooc地址](http://www.imooc.com/learn/563)，代码采用自定义一个爬虫框架进行爬取。

**__init__.py**

初始化目录为一个模块

**spider_main.py**

项目的控制中心，由它启动整个爬虫项目

- craw

  count控制爬取链接数，从url收集器中获取url，传递给下载器接收源码，再传给解析器进行解析获取数据，传递数据给输出器

**url_manager.py**

收集网页中的url，避免重复爬取

- add_new_url

  确保当前url有效且出现过，就添加至待爬取url集合

- add_new_urls

  添加新获取到的url

- has_new_url

  检验新获取到的url有效

- get_new_url

  从待爬取url集合中取出url，放到已爬取url集合中，并进行爬取

**html_download.py**

网页下载器，主要用requests库实现

- download

  使用get方法获取网页源码并且用utf8编码格式进行解码

**html_parser.py**

数据下载完成之后，对网页源码进行解析，提取所需内容

- parse

  用bs解析网页源码，分别传给`_get_new_urls`、`_get_new_data`函数

- _get_new_data

  获取网页url、网页标题、网页概要

- _get_new_urls

  获取网页中所有链接（/item/\w+）

**html_outputer.py**

数据收集完成后，将所有内容输出到网页

- collect_data

  确保接收的数据不为空才添加进datas列表

- ouput_html

  遍历datas列表，格式化输出到ouput.html中

**output.html**

内容展示页

- <h1>标题
- <h2>链接
- <h4>概要

