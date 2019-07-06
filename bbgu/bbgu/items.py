# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BbguItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Check(scrapy.Item):
    username = scrapy.Field()
    passwd = scrapy.Field()
    secret_code = scrapy.Field()
    code_img = scrapy.Field()

class SoreData(scrapy.Item):
    data = scrapy.Field()