# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class eyouItem(scrapy.Item):
    region = scrapy.Field()
    order = scrapy.Field()
    loc = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()
    legal = scrapy.Field()
    locdetail = scrapy.Field()
    contact = scrapy.Field()
    phone = scrapy.Field()
    certiCode = scrapy.Field()
    issueDate = scrapy.Field()
    effectiveDate = scrapy.Field()
    businessScope =scrapy.Field()
