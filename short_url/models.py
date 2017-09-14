# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.urls import reverse


class Url(models.Model):
    url = models.URLField(max_length=2047, null=True, blank=True)
    created_date = models.DateTimeField(default=datetime.now, verbose_name=u"Data utworzenia")

    def get_absolute_url(self):
        return reverse('short_url:url_add')


class ShortUrl(models.Model):
    url = models.ForeignKey('Url', verbose_name = u"Pierwotny url", null = True, blank = True, related_name='urls')
    short_url = models.CharField(max_length=255, unique=True, null=True, blank=True)