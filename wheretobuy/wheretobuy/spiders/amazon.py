import scrapy
from ..items import AmazonItem



class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ["amazon.com"]
    # name and start_urls must have those names for scrapy dependency

    start_urls = [
        'http://www.amazon.com/s?k=tv&crid=IROLYW74A67U&sprefix=tv%2Caps%2C151&ref=nb_sb_noss_1',
    ]

    def parse(self, response):
        item = AmazonItem()  # from items.py
        product_name = response.css('.a-size-medium.a-text-normal::text').get()  # Working
        product_price = response.css('.a-price-whole::text').get() + '.' + response.css('.a-price-fraction::text').get()
        product_link = response.css('.a-size-medium.a-text-normal::attr(href)').get()
        product_image_link = response.css('s-image::attr(src)').get()

        item['product_name'] = product_name
        item['product_price'] = product_price
        item['product_link'] = product_link
        item['product_image_link'] = product_image_link

        print(item)
        yield item

    """Run by <<scrapy crawl amazon>> in terminal"""
