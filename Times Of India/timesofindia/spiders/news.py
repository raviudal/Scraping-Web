# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from time import sleep

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['timesofindia.indiatimes.com']
    start_urls = ['https://timesofindia.indiatimes.com/topic/rape/news']

    def parse(self, response):
        articles_url = response.xpath('//*[@class="content"]/a/@href').extract()
        for article in articles_url:
            article_url = response.urljoin(article)
            yield Request(article_url, self.parse_one_article)

        next_url = response.urljoin(response.xpath('//*[@id="raquo"]/@href').extract_first())
        sleep(0.5)
        yield Request(next_url, self.parse)

    def parse_one_article(self, response):
        title = response.xpath('//h1/arttitle/text()').extract_first()
        datetime = response.xpath('//section/span/span[2]/time/@datetime').extract_first()
        raw_txt = " ".join(response.xpath('//*[@class="article_content clearfix"]/arttextxml/div/div/text()').extract())

        yield {
        'title' : title,
        'datetime' : datetime,
        'raw_txt' : raw_txt
        }
