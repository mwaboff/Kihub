# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import datetime
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_desc = models.CharField('Short Description', max_length=140)
    long_desc = models.TextField('Long Description')
    tech_used = models.CharField('Technology Used', max_length=140, default='')
    git_link = models.URLField('Github URL', blank=True)
    live_link = models.URLField('Live URL', blank=True)
    img_link = models.URLField('Image Link', blank=True)
    order_int = models.IntegerField('Order (lower is ranked higher)', default=0)

    def __str__(self):
        return self.name