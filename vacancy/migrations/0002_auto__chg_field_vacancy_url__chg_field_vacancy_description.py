# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Vacancy.url'
        db.alter_column(u'vacancy_vacancy', 'url', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Vacancy.description'
        db.alter_column(u'vacancy_vacancy', 'description', self.gf('django.db.models.fields.TextField')(max_length=30))

    def backwards(self, orm):

        # Changing field 'Vacancy.url'
        db.alter_column(u'vacancy_vacancy', 'url', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Vacancy.description'
        db.alter_column(u'vacancy_vacancy', 'description', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'vacancy.vacancy': {
            'Meta': {'object_name': 'Vacancy'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['vacancy']