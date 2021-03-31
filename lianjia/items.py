# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    position = scrapy.Field()
    follow = scrapy.Field()
    time = scrapy.Field()
    total = scrapy.Field()
    unit = scrapy.Field()
    houseIntroduction = scrapy.Field()
    houseRange = scrapy.Field()
    houseDirection = scrapy.Field()
    houseDecorate = scrapy.Field()
    houseHeight = scrapy.Field()
    houseAge = scrapy.Field()
    houseType = scrapy.Field()

