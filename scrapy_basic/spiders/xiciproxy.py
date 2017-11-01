# -*- coding: utf-8 -*-
import scrapy
from scrapy_basic.items import ProxyItem

class XiciproxySpider(scrapy.Spider):
    name = 'xiciproxy'
    allowed_domains = ['www.xicidaili.com']
    base_url = 'http://www.xicidaili.com/nt/%d'
    page = 1
    start_urls = [base_url % page]

    def parse(self, response):
        # 过滤th
        ip_list = response.xpath('//table[@id="ip_list"]//tr')[1:]
        f = lambda x : x[0] if x else ''
        for ip in ip_list:
            item = ProxyItem()
            addr = f(ip.xpath('./td[2]/text()').extract())
            port = f(ip.xpath('./td[3]/text()').extract())
            location = f(ip.xpath('./td[4]/a/text()').extract())
            http_type = f(ip.xpath('./td[6]/text()').extract())
            speed = f(ip.xpath('./td[7]/div/@title').extract())
            connect_speed = f(ip.xpath('./td[8]/div/@title').extract())
            alive_time = f(ip.xpath('./td[9]/text()').extract())

            item['addr'] = addr
            item['port'] = port
            item['location'] = location
            item['http_type'] = http_type
            item['speed'] = speed
            item['connect_speed'] = connect_speed
            item['alive_time'] = alive_time

            # print  addr,port.strip().replace('\n',''),location,http_type,speed,connect_speed,alive_time
            yield item
        if self.page < 100:
            self.page += 1

        yield scrapy.Request(self.base_url % self.page,callback=self.parse)
        