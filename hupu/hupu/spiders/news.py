# -*- coding: utf-8 -*-

import datetime

import scrapy

from hupu.items import ContentItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    start_urls = ['https://voice.hupu.com/nba/1']

    def get_next_page(self, response):
        urls = response.xpath('//a[@class="page-btn-prev"]/@href').extract()
        url = urls[1] if len(urls) == 2 else urls[0]
        return response.urljoin(url)

    def is_time_before_30_days(self, news_time):
        time_cmp = datetime.datetime.now() - datetime.datetime.strptime(news_time, '%Y-%m-%d %H:%M')
        return time_cmp.days > 30

    def get_title_url_time(self, response):
        news_list = response.xpath('//div[@class="news-list"]/ul/li')
        urls = filter(lambda k: k is not None, [i.xpath('div[1]/h4/a/@href').extract_first() for i in news_list])
        news_time = response.xpath('//div[@class="news-list"]/ul/li[1]/div[2]/span[1]/a/@title').extract()[0]
        return urls, news_time

    def parse_content(self, response):
        title = response.xpath('//h1[@class="headline"]/text()').extract_first().strip()
        content = response.xpath('//div[@class="artical-main-content"]/p/text()').extract()
        time = response.xpath('//span[@id="pubtime_baidu"]/text()').extract_first().strip()
        return ContentItem({'title': title, 'content': ' '.join(content), 'time': time})

    def parse(self, response):
        urls, news_time = self.get_title_url_time(response)
        for i in urls:
            yield scrapy.Request(i, callback=self.parse_content)

        if not self.is_time_before_30_days(news_time):
            next_page = self.get_next_page(response)
            yield scrapy.Request(next_page, callback=self.parse)
