# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RoachItem(scrapy.Item):
    post = scrapy.Field()
    post_link = scrapy.Field()
    subreddit = scrapy.Field()
    pass
