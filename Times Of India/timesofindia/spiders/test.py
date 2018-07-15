# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from time import sleep
class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['timesofindia.indiatimes.com']
    start_urls = ['https://timesofindia.indiatimes.com/searchresult.cms?sortorder=score&searchtype=2&maxrow=1&startdate=2001-01-01&enddate=2001-07-14&article=2&pagenumber=1&isphrase=no&query=rape&searchfield=&section=&kdaterange=1500&date1mm=01&date1dd=01&date1yyyy=2001&date2mm=07&date2dd=14&date2yyyy=2001']

    def parse(self, response):
        title = response.xpath('//*[@style="padding-bottom:20px;font-size:13px;"]/a/text()').extract()
        date = response.xpath('//*[@style="padding-bottom:20px;font-size:13px;"]/span[@style="font-size:11px;color:#6c6c6c;"]/script/text()').extract()
        next_url = response.urljoin(response.xpath('//*[@style="float:right;"]/a/@href').extract()[0])
        for s,d in zip(title,date):
            if 'rape' in s:
                yield {
                'Title' : s,
                'Date' : d
                }
                # print('\n')
                # print(s)
                # print(d[4:15])
                # print('\n')
        # print(next_url)
        # print('\n')


        sleep(0.5)
        yield Request(next_url, self.parse)
