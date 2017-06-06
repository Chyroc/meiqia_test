# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os


class SaveContentPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        content = item['content']
        time = item['time']

        if not os.path.exists('data'):
            os.mkdir('data')

        with open('data/[{}]{}.txt'.format(time.replace(':', '-'), title), 'w', errors='ignore') as f:
            f.write(' '.join([title, content]))
        return item
