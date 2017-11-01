# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class CommonPipeline(object):
    # 必须要实现的方法就是,处理item
    def process_item(self ,item, spider):
        self.f.write(json.dumps(dict(item),ensure_ascii=False).encode('utf-8') + '\n')
        return item

    def close_spider(self,spider):
        self.f.close()

class TeacherPipline(object):
    def __init__(self):
        self.f = open('teacher.json' ,'w')

    # 必须要实现的方法就是,处理item
    def process_item(self ,item, spider):
        self.f.write(json.dumps(dict(item)).encode('utf-8') + '\n')
        return item

    def close_spider(self,spider):
        self.f.close()

class TencentPipline(object):
    def __init__(self):
        self.f = open('tencent_position.json' ,'w')

    # 必须要实现的方法就是,处理item
    def process_item(self ,item, spider):
        self.f.write(json.dumps(dict(item),ensure_ascii=False).encode('utf-8') + '\n')
        return item

    def close_spider(self,spider):
        self.f.close()

class ProxyPipline(CommonPipeline):
    def __init__(self):
        self.f = open('proxy.json' ,'w')