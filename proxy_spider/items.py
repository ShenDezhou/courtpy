# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyItem(scrapy.Item):
    country = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    location = scrapy.Field()
    anonymous = scrapy.Field()
    type = scrapy.Field()
    speed = scrapy.Field()
    time = scrapy.Field()
    pass

class WenshuItem(scrapy.Item):
    abstract = scrapy.Field()
    type = scrapy.Field()
    time = scrapy.Field()
    name = scrapy.Field()
    id = scrapy.Field()
    procedure = scrapy.Field()
    caseid = scrapy.Field()
    courtname = scrapy.Field()
    pass

class NodeItem(scrapy.Item):
    time = scrapy.Field()
    param = scrapy.Field()
    count = scrapy.Field()
    pass