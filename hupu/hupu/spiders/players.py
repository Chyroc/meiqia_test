# -*- coding: utf-8 -*-

import scrapy


class PlayersSpider(scrapy.Spider):
    name = 'players'
    start_urls = ['https://nba.hupu.com/players']

    def parse_players(self, response):
        info = response.xpath('//table[@class="players_table"]/tbody/tr/td[2]')
        name_cn = info.xpath('b/a/text()').extract()
        name_en = info.xpath('p/b/text()').extract()
        with open('name_word.txt', 'a', errors='ignore', encoding='utf-8') as f:
            for i in zip(name_cn, name_en):
                f.write('{},{}'.format(*i))
                f.write('\n')

    def parse(self, response):
        teams_url = response.xpath('//ul[@class="players_list"]/li/span/a/@href').extract()

        for i in teams_url:
            yield scrapy.Request(i, callback=self.parse_players)
