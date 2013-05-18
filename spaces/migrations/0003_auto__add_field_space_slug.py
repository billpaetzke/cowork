# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Space.slug'
        db.add_column(u'spaces_space', 'slug',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=63, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Space.slug'
        db.delete_column(u'spaces_space', 'slug')


    models = {
        u'spaces.pendingspace': {
            'Meta': {'object_name': 'PendingSpace'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        },
        u'spaces.space': {
            'Meta': {'object_name': 'Space'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lon': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '31', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['spaces']