# -*- coding: utf-8 -*-

import scrapy

class StackexItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    pass
