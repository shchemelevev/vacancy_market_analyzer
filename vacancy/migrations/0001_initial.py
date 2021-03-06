# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vacancy'
        db.create_table(u'vacancy_vacancy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'vacancy', ['Vacancy'])


    def backwards(self, orm):
        # Deleting model 'Vacancy'
        db.delete_table(u'vacancy_vacancy')


    models = {
        u'vacancy.vacancy': {
            'Meta': {'object_name': 'Vacancy'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['vacancy']