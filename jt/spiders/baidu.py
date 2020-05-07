# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['https://www.baidu.com']
    start_urls = ['http://https://www.baidu.com/']

    def parse(self, response):
        pass

