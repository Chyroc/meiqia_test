# -*- coding: utf-8 -*-

import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    start_urls = ['https://voice.hupu.com/nba/1']

    def get_next_page(self, response):
        urls = response.xpath('//a[@class="page-btn-prev"]/@href').extract()
        url = urls[1] if len(urls) == 2 else urls[0]
        return response.urljoin(url)

    def parse(self, response):
        next_page = self.get_next_page(response)
        yield scrapy.Request(next_page, callback=self.parse)
