#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc :
"""
from coolscrapy.items import MittiItem
import scrapy

class MittiSpider(scrapy.Spider):
    name = "AAAmitti"
    allowed_domains = ["http://pagang.mitti.se/"]
    start_urls = [
        "http://pagang.mitti.se"
    ]

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "text/javascript",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        "Referer": "http://pagang.mitti.se/"
    }

    def parse(self, response):
       #filename = response.url.split("/")[-2]#
       #with open(filename, 'wb') as f:
       #    f.write(response.body)


       item = MittiItem()

       for sel in response.xpath('//div[@class="innerContentContainer"]'):
         ##print sel

         item['title'] = sel.xpath('.//div[@class="listTitle"]/text()').extract()
         print(item['title'])

         ##item['link'] = sel.xpath('a[2]')
         #item['link'] = sel.xpath('a[contains(@href, "http")]')
         item['link'] = sel.xpath('a[contains(@href, "http")]/@href')[0].extract().strip()
         print(item['link'])

         item['location'] = sel.xpath('.//div[@class="listLocationDate"]/text()')[2].extract().strip()
         print(item['location'])

         item['time'] = sel.xpath('.//div[@class="listLocationDate"]/text()')[4].extract().strip()
         print(item['time'])
         print('\n')


       next_page = response.xpath('//a[contains(@href, "http://pagang.mitti.se/page/")][last()]/@href').extract()
       print next_page
       print('\n')

       if next_page:
           next_page = next_page[0]
           next_page_url = response.urljoin(next_page)
           yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=True)
       else:
           print(str(next_page))