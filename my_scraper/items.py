import scrapy

from scrapy.item import Item, Field

class MyScraperItem(scrapy.Item):
    title = Field()
    link = Field()
    location = Field()
    original_price = Field()
    price = Field()
    end_date = Field()
    
    