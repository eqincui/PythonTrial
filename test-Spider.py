#! /usr/bin/env python
# coding:utf-8

import requests
from lxml import etree

#我们邀抓取的页面链接
url='http://pagang.mitti.se'

#用requests库的get方法下载网页
r=requests.get(url).text

#解析网页并且定位短评
s=etree.HTML(r)
file=s.xpath('//*[@id="comments"]/ul/li/div[2]/p/text()')

#打印抓取的信息
print(file)