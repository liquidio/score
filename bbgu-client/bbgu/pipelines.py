# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from bbgu.items import Check,SoreData

class BbguPipeline(object):
    def process_item(self, item, spider):
        return item

class ResponseCheckCode(object):
    def process_item(self, Check, spider):
        if Check['secret_code']:
            pass
            #send to server
            #from server get user_info
            #write Check 

class ResponseSoredata(object):
    def process_item(self, SoreData, spider):
        if SoreData :
            pass
            #send to server sore date
            #close

