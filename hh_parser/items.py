# -*- coding: utf-8 -*-
from scrapy.contrib.djangoitem import DjangoItem
from vacancy.models import Vacancy


class VacancyItem(DjangoItem):
    django_model = Vacancy
