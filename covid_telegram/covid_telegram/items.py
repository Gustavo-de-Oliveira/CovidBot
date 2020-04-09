# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CovidTelegramItem(scrapy.Item):
    url = scrapy.Field()
    cases = scrapy.Field()
    death = scrapy.Field()
    recovered = scrapy.Field()
    controled = scrapy.Field()
    critical = scrapy.Field()
    pass
