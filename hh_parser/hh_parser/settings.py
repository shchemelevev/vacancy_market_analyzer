# -*- coding: utf-8 -*-

# Scrapy settings for hh_parser project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'hh_parser'

SPIDER_MODULES = ['hh_parser.spiders']
NEWSPIDER_MODULE = 'hh_parser.spiders'
COOKIES_DEBUG = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hh_parser (+http://www.yourdomain.com)'
