# -*- coding: utf-8 -*-
import scrapy


class VacancyItem(scrapy.Item):
    url = scrapy.Field()
    description = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()
