from django.db import models


class Vacancy(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(max_length=30)
