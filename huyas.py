# -*- coding: utf-8 -*-
import scrapy
from huya.items import HuyaItem


class HuyasSpider(scrapy.Spider):
    name = 'huyas'
    allowed_domains = ['huya.com']
    start_urls = ['https://www.huya.com/g/lol']

    def parse(self, response):
        List = response.xpath("//div[@class='box-bd']//ul[@class='live-list clearfix']/li")
        for z in List:
            zb = HuyaItem()
            zb['title'] = z.xpath('.//a[@title]/text()').extract_first()
            zb['name'] = z.xpath('.//span[@class="txt"]//span[@class="avatar fl"]/i/text()').extract_first()
            yield zb