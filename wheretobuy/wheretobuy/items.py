# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    source = 'Amazon'
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_link = scrapy.Field()
    product_image_link = scrapy.Field()
    # seller_name = scrapy.Field()