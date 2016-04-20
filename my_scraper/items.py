import scrapy

from scrapy.item import Item, Field

class DmozItem(scrapy.Item):
    title = Field()
    link = Field()
    desc = Field()