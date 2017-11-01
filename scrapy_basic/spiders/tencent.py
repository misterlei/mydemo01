# -*- coding: utf-8 -*-
import scrapy
from scrapy_basic.items import PositionItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    page = 0
    # 爬虫起始url
    base_url = 'http://hr.tencent.com/position.php?start=%d'
    start_urls = [ base_url % page]

    def parse(self, response):
        #匹配所有的职位tr
        position_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for position in position_list:
            item = PositionItem()
            print position.xpath('.//td[1]/a/text()').extract()[0]
            f = lambda x: x[0] if x else ''

            item['position_name'] = position.xpath('.//td[1]/a/text()').extract()[0]
            item['position_link'] = position.xpath('.//td[1]/a/@href').extract()[0]
            position_type = position.xpath('.//td[2]/text()').extract()
            item['position_type'] = position_type[0] if position_type else ''

            position_num = position.xpath('.//td[3]/text()').extract()
            item['position_num'] = position_num[0] if position_num else ''

            # lambda 匿名函数
            item['location'] = f(position.xpath('.//td[4]/text()').extract())
            item['date_pub'] = f(position.xpath('.//td[5]/text()').extract())

            yield item

        if self.page < 500:
            self.page += 10
            # 构造请求，生成请求，加入队列
            yield scrapy.Request(self.base_url % self.page, callback=self.parse)