# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter


"""Scraped Data --> Item Containers --> Pipeline --> SQL or MongoDB database"""

class WheretobuyPipeline(object):

    def __init__(self):
        # Automatically create connection and table when pipeline is created
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect("prices.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS prices_db""")
        self.cursor.execute("""create table prices_db(
                                title text,
                                price real,
        
                            """)

    def store_db(self, item):
        self.cursor.execute("""insert into prices_db values (?, ?, ?)"""),
        # needs more code to add item



        self.connection.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
