# -*- coding: utf-8 -*-

import datetime

import scrapy


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

    def get_time(self, response):
        # TODO
        news_time = response.xpath('//div[@class="news-list"]/ul/li[1]/div[2]/span[1]/a/@title').extract()[0]
        return news_time

    def parse(self, response):
        news_time = self.get_time(response)

        if not self.is_time_before_30_days(news_time):
            next_page = self.get_next_page(response)
            yield scrapy.Request(next_page, callback=self.parse)
