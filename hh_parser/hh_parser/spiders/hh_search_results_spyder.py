#-*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request

from BeautifulSoup import BeautifulSoup

from hh_parser.items import VacancyItem



class HHSearchResultsSpider(CrawlSpider):
    name = 'headhunter_search_results'
    allowed_domains = ['hh.ru', 'tyumen.hh.ru']
    start_urls = ['http://tyumen.hh.ru/search/vacancy?text=django&clusters=true&area=113&page=0']
    rules = [
                Rule(SgmlLinkExtractor(allow=[r'search/vacancy\?text=django.+page=\d+']), follow=True),
                Rule(SgmlLinkExtractor(allow=[r'vacancy.+query=django$']), callback='parse_vacancy_page')
            ]

    def parse_vacancy_page(self, response):
        soup = BeautifulSoup(response.body_as_unicode())
        vacancy = VacancyItem()
        vacancy['description'] = soup.find("div", {"id": "hypercontext"})
        vacancy['url'] = response.url
        return vacancy

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies={'regions': '113', 'redirect_host': 'tyumen.hh.ru'})
