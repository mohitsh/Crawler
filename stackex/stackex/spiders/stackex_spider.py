from scrapy import Spider
from scrapy.selector import Selector

class StackexSpider(Spider):
    name = "stackex"
    allowed_domains = ["https://www.reddit.com"]
    start_urls = ["https://www.reddit.com/new/"]

    def parse(self, response):
        posts = Selector(response).xpath('//div[contains(@class, "entry unvoted")]/div[contains(@class, "top-matter")]/p[contains(@class, "title")]')
        first_post = posts[0]
        for elem in posts:
            post_text = elem.xpath('.//a[contains(@class, "title may-blank ")]/text()').extract()
            comment, subreddit = elem.xpath('.//a/@href').extract()
            print('-'*20)
            print(post_text)
            print(comment)
            print(subreddit)
            print('-'*20)
            print('\n')
        print("LENGTH: {0}".format(len(posts)))
