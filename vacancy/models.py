#-*- coding:utf-8 -*-
import hashlib

from django.db import models


class Vacancy(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(max_length=30)
    checksum = models.TextField(max_length=56)

    def save_if_unique(self, *args, **kwargs):
        if self.description:
            self.checksum = hashlib.sha224(self.description.encode('utf-8')).hexdigest()
        if not Vacancy.objects.filter(checksum=self.checksum).exists():
            return super(Vacancy, self).save(*args, **kwargs)
        else:
            return None
