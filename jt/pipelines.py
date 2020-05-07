# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class JtPipeline(object):
    def __init__(self):
        self.file = open('result.json', 'wb')

    def process_item(self, item, spider):
        line = (json.dumps(dict(item),ensure_ascii=False) + ',\n').encode('utf-8')
        self.file.write(line)
        return item

    def open_spider(self, spider):
        self.file.write('[\n'.encode('utf-8'))

    def close_spider(self, spider):
        self.file.write(']'.encode('utf-8'))
        self.file.close()
