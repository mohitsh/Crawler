import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from datetime import datetime

class redditItem(scrapy.Item):
    post = scrapy.Field()
    post_link = scrapy.Field()
    subreddit = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)



class RoachSpider(Spider):
    name = "roach"
    allowed_domains = ["https://www.reddit.com"]
    start_urls = ["https://www.reddit.com/r/Fun/new"]
    def parse(self, response):
        posts = Selector(response).xpath('//div[contains(@class, "entry unvoted")]/div[contains(@class, "top-matter")]/p[contains(@class, "title")]')
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S") 
        for elem in posts:
            post = elem.xpath('.//a[contains(@class, "title may-blank ")]/text()').extract()
            post_link, subreddit = elem.xpath('.//a/@href').extract()
            newpost = redditItem()
            newpost['post'] = post
            newpost['post_link'] = post_link
            newpost['subreddit'] = subreddit
            newpost['last_updated'] = timestamp
            yield(newpost)
        print("LENGTH: {0}".format(len(posts)))
