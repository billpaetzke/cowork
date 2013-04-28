# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Space'
        db.create_table(u'spaces_space', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=31, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'spaces', ['Space'])

        # Adding model 'PendingSpace'
        db.create_table(u'spaces_pendingspace', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'spaces', ['PendingSpace'])


    def backwards(self, orm):
        # Deleting model 'Space'
        db.delete_table(u'spaces_space')

        # Deleting model 'PendingSpace'
        db.delete_table(u'spaces_pendingspace')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '31', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['spaces']