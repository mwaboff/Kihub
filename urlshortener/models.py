# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import datetime
# Create your models here.

class URL(models.Model):
    orig_url = models.URLField('original URL')
    short_url = models.CharField('shortened URL', max_length=100, unique=True)
    creation_date = models.DateTimeField('date created', default=timezone.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return "boff.io/" + self.short_url