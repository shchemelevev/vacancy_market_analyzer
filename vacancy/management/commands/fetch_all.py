from django.core.management.base import BaseCommand, CommandError

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings

from hh_parser.hh_search_results_spyder import HHSearchResultsSpider


class Command(BaseCommand):
    help = 'Fetch data from all sources'

    def handle(self, *args, **options):
        spider = HHSearchResultsSpider()
        settings = get_project_settings()
        crawler = Crawler(settings)
        crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()
        log.start()
        reactor.run() # the script will block here until the spider_closed signal was sent
