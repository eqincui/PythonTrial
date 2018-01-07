# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook

class CoolscrapyPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['title', 'location', 'link', 'time'])  # 设置表头

    def process_item(self, item, spider):

        line = [item['title'], item['location'], item['link'], item['time']]  # 把数据中每一项整理出来
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('C:/Python27/examples/PythonTrial/test-Scrapy/mitti.xlsx')  # 保存xlsx文件

        return item