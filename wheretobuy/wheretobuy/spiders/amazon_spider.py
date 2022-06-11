import scrapy
from ..items import WheretobuyItem

class AmazonSpider(scrapy.Spider):
    # name and start_url must have those names for scrapy dependency
    name = 'amazon'
    start_urls = ['https:/www.amazon.com/']

    def parse(self, response):
        items = WheretobuyItem()  # from items.py
        pass
        # must yield a dictionary

    """Run by <<scrapy crawl amazon_spider>> in terminal"""