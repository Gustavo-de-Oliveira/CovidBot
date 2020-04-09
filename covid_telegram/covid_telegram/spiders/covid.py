# -*- coding: utf-8 -*-
import scrapy
from covid_telegram.items import CovidTelegramItem

WORLD_URL = 'https://www.worldometers.info/coronavirus/'

class CovidSpider(scrapy.Spider):
    name = 'covid'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/country/brazil/', 'https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        article = CovidTelegramItem({
            "url": response.url,
	        "cases": response.xpath('//div[@class="maincounter-number"]/descendant::span/text()').extract()[0],
	        "death": response.xpath('//div[@class="maincounter-number"]/descendant::span/text()').extract()[1],
	        "recovered": response.xpath('//div[@class="maincounter-number"]/descendant::span/text()').extract()[2],
	        "controled": response.xpath('//span[@class="number-table"]/text()').extract()[0],
	        "critical": response.xpath('//span[@class="number-table"]/text()').extract()[1]
        })
        return article