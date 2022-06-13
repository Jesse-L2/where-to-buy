# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

"""Scraped Data --> Item Containers --> Pipeline --> SQL or MongoDB database"""
"""Class used to store data in database or some other file. Receives an item and performs action on it."""


class WheretobuyPipeline(object):

    def __init__(self):
        # Automatically create connection and table when pipeline is created
        self.create_connection()
        self.create_table()  # call create table if doesn't exist

    def create_connection(self):
        self.conn = sqlite3.connect("products.db")
        self.curs = self.conn.cursor()

    def create_table(self):
        self.curs.execute("""CREATE TABLE IF NOT EXISTS products_db(
                                product_name text,
                                product_price real,
                                product_link text,
                                product_image_link text)
                            """)

    def store_db(self, item):
        # Only add new products (ignore if already in products)
        self.curs.execute("""INSERT OR IGNORE INTO products_db VALUES (?,?,?,?)""",
                          (item['product_name'][0],
                           item['product_price'][0],
                           item['product_link'][0],
                           item['product_image_link'][0])
                          )

        self.conn.commit()  # Commit and return item in process_item

    def process_item(self, item, spider):
        """adapter = ItemAdapter(item)
        # Check to see if item has a price, reject item if no price
        if adapter.get('product_price'):
            self.store_db(item)
            return item
        else:
            raise DropItem(f"Missing price for {item}")"""
        print(item)
        self.store_db(item)
        return item
