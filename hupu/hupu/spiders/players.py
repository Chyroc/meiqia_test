# -*- coding: utf-8 -*-

import scrapy


class PlayersSpider(scrapy.Spider):
    name = 'players'
    start_urls = ['https://nba.hupu.com/players']

    def parse_players(self, response):
        pass
        # TODO

    def parse(self, response):
        teams_url = response.xpath('//ul[@class="players_list"]/li/span/a/@href').extract()

        for i in teams_url:
            yield scrapy.Request(i, callback=self.parse_players)
