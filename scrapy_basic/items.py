# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyBasicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TeacherItem(scrapy.Item):
    name = scrapy.Field()
    desc = scrapy.Field()

class PositionItem(scrapy.Item):
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_type = scrapy.Field()
    position_num = scrapy.Field()
    location = scrapy.Field()
    date_pub = scrapy.Field()

class ProxyItem(scrapy.Item):
    addr = scrapy.Field()
    port = scrapy.Field()
    location = scrapy.Field()
    http_type = scrapy.Field()
    speed = scrapy.Field()
    connect_speed = scrapy.Field()
    alive_time = scrapy.Field()
