# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SchoolItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field() 
    address = scrapy.Field()
    rating = scrapy.Field()
    enrollment = scrapy.Field() 
    grade_span = scrapy.Field()
    state = scrapy.Field()    
