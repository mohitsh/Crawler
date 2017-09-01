import scrapy

class YahooFinSpider(scrapy.Spider):
    name = "yahooFin"
    def start_requests(self):
        urls = ['https://in.finance.yahoo.com/quote/VEDL.NS?ltr=1']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        divs = response.xpath('//div[contains(@class, "Mt(6px)")]') 
        span = response.xpath('//span[contains(@class, "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")]')
        print("THE PRICE SPAN")
        print(span)
