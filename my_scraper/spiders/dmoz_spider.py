# import scrapy

# class DmozSpider(scrapy.Spider):
#     name = "dmoz"
#     allowed_domains = ["dmoz.org"]
#     start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/", "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]
    
#     def parse(self, response):
#         filename = response.url.split("/")[-2] + '.html'
#         with open(filename, 'wb') as f:
#             f.write(response.body)

#     for sel in response.xpath('//ul/li'):
#         title = sel.xpath('a/text()').extract()
#         link = sel.xpath('a/@href').extract()
#         desc = sel.xpath('text()').extract()
#         print title, link, desc

import scrapy
# from scrapy.contrib.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
# from scrapBib.items import *


class MySpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = "flipkart.com"
    start_urls = ['http://www.flipkart.com/search/a/all?query=mybook']

    def parse(self,response):
        hls = HtmlXPathSelector(response)
        # it = MyItem()
        it = hls.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "fk-display-block", " " ))]').extract()
        # it1 = hls.xpath('//span[@price]/text()').extract()
        print it